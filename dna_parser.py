"""
DNA File Parser
Supports: AncestryDNA, 23andMe, MyHeritage, FamilyTreeDNA, and generic formats
"""

import pandas as pd
import zipfile
import io
from typing import Optional


def parse_dna_file(file_obj, file_path: str) -> Optional[pd.DataFrame]:
    """
    Parse DNA files from various providers
    Returns standardized DataFrame with columns: rsid, chromosome, position, genotype
    """
    try:
        # Handle ZIP files
        if file_path.endswith('.zip'):
            content = extract_zip_content(file_obj)
        else:
            content = file_obj.read()
            if isinstance(content, bytes):
                content = content.decode('utf-8', errors='ignore')

        if not content:
            return None

        # Parse content
        lines = content.strip().split('\n')

        # Skip comment lines and find data start
        data_start = 0
        for i, line in enumerate(lines):
            if not line.startswith('#') and not line.startswith('/') and line.strip():
                data_start = i
                break

        # Detect provider
        provider = detect_provider(lines[:30])

        # Parse based on provider
        if provider == 'ancestry':
            return parse_ancestry_dna(lines[data_start:])
        elif provider == '23andme':
            return parse_23andme_dna(lines[data_start:])
        elif provider == 'myheritage':
            return parse_myheritage_dna(lines[data_start:])
        elif provider == 'ftdna':
            return parse_ftdna(lines[data_start:])
        else:
            return parse_generic_dna(lines[data_start:])

    except Exception as e:
        print(f"Parse error: {e}")
        return None


def extract_zip_content(file_obj) -> Optional[str]:
    """Extract DNA data from ZIP archive"""
    try:
        with zipfile.ZipFile(file_obj) as z:
            for filename in z.namelist():
                if filename.endswith(('.txt', '.csv')) and not filename.startswith('__'):
                    with z.open(filename) as f:
                        return f.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"ZIP extraction error: {e}")
    return None


def detect_provider(header_lines: list) -> str:
    """Detect DNA data provider from file header"""
    header_text = ' '.join(header_lines).lower()

    if 'ancestrydna' in header_text or 'ancestry' in header_text:
        return 'ancestry'
    elif '23andme' in header_text:
        return '23andme'
    elif 'myheritage' in header_text:
        return 'myheritage'
    elif 'ftdna' in header_text or 'familytreedna' in header_text:
        return 'ftdna'
    else:
        # Try to detect by format
        for line in header_lines:
            if not line.startswith('#'):
                parts = line.strip().split('\t')
                if len(parts) >= 5:  # AncestryDNA format
                    return 'ancestry'
                elif len(parts) == 4:  # 23andMe format
                    return '23andme'
                break
        return 'generic'


def parse_ancestry_dna(lines: list) -> pd.DataFrame:
    """Parse AncestryDNA format (tab-separated, 5 columns)"""
    data = []

    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue

        parts = line.strip().split('\t')
        if len(parts) >= 5:
            rsid = parts[0].strip()
            chrom = parts[1].strip().replace('chr', '')
            pos = parts[2].strip()
            allele1 = parts[3].strip()
            allele2 = parts[4].strip()

            # Skip header
            if rsid.lower() == 'rsid' or rsid.startswith('#'):
                continue

            # Validate
            if not (rsid.startswith('rs') or rsid.startswith('i')):
                continue

            # Clean chromosome
            if chrom == 'MT':
                chrom = 'M'

            try:
                position = int(pos)
            except ValueError:
                continue

            # Skip missing alleles
            if allele1 in ['0', '-', 'N', 'D', 'I'] or allele2 in ['0', '-', 'N', 'D', 'I']:
                continue

            data.append({
                'rsid': rsid,
                'chromosome': chrom,
                'position': position,
                'genotype': allele1 + allele2
            })

    return pd.DataFrame(data) if data else None


def parse_23andme_dna(lines: list) -> pd.DataFrame:
    """Parse 23andMe format (tab-separated, 4 columns)"""
    data = []

    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue

        parts = line.strip().split('\t')
        if len(parts) >= 4:
            rsid = parts[0].strip()
            chrom = parts[1].strip().replace('chr', '')
            pos = parts[2].strip()
            genotype = parts[3].strip()

            # Skip header
            if rsid.lower() == 'rsid':
                continue

            # Skip internal IDs for now (can enable if needed)
            if rsid.startswith('i'):
                continue

            if chrom == 'MT':
                chrom = 'M'

            # Skip no-calls
            if genotype in ['--', 'NC', 'no call', 'DD', 'II']:
                continue

            try:
                position = int(pos)
            except ValueError:
                continue

            data.append({
                'rsid': rsid,
                'chromosome': chrom,
                'position': position,
                'genotype': genotype.replace(' ', '')
            })

    return pd.DataFrame(data) if data else None


def parse_myheritage_dna(lines: list) -> pd.DataFrame:
    """Parse MyHeritage format (CSV)"""
    data = []
    header_found = False

    for line in lines:
        if not line.strip():
            continue

        if not header_found:
            if 'rsid' in line.lower() or 'snp' in line.lower():
                header_found = True
                continue

        if header_found:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                rsid = parts[0].strip('"').strip()
                chrom = parts[1].strip('"').strip().replace('chr', '')
                pos = parts[2].strip('"').strip()
                result = parts[3].strip('"').strip()

                if chrom == 'MT':
                    chrom = 'M'

                if len(result) != 2:
                    continue

                try:
                    position = int(pos)
                except ValueError:
                    continue

                data.append({
                    'rsid': rsid,
                    'chromosome': chrom,
                    'position': position,
                    'genotype': result
                })

    return pd.DataFrame(data) if data else None


def parse_ftdna(lines: list) -> pd.DataFrame:
    """Parse FamilyTreeDNA format"""
    data = []

    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue

        # Try CSV first, then tab
        if ',' in line:
            parts = [p.strip('"').strip() for p in line.strip().split(',')]
        else:
            parts = line.strip().split('\t')

        if len(parts) >= 4:
            rsid = parts[0].strip()
            chrom = parts[1].strip().replace('chr', '')
            pos = parts[2].strip()

            # Handle different formats
            if len(parts) >= 5:
                genotype = parts[3].strip() + parts[4].strip()
            else:
                genotype = parts[3].strip()

            if rsid.lower() == 'rsid' or not (rsid.startswith('rs') or rsid.startswith('i')):
                continue

            if chrom == 'MT':
                chrom = 'M'

            try:
                position = int(pos)
            except ValueError:
                continue

            if len(genotype) == 2:
                data.append({
                    'rsid': rsid,
                    'chromosome': chrom,
                    'position': position,
                    'genotype': genotype
                })

    return pd.DataFrame(data) if data else None


def parse_generic_dna(lines: list) -> pd.DataFrame:
    """Generic parser for unknown formats"""
    data = []

    # Detect delimiter
    delimiters = ['\t', ',', ' ', ';']
    delimiter = '\t'

    for line in lines:
        if line.strip() and not line.startswith('#'):
            for delim in delimiters:
                if delim in line and line.count(delim) >= 2:
                    delimiter = delim
                    break
            break

    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue

        parts = line.strip().split(delimiter)

        # Try to identify columns
        if len(parts) >= 3:
            rsid_col = None
            chrom_col = None
            pos_col = None
            geno_col = None

            valid_chroms = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           'X', 'Y', 'M', 'MT']

            for i, part in enumerate(parts):
                part = part.strip('"').strip()
                if part.startswith('rs'):
                    rsid_col = i
                elif part in valid_chroms:
                    chrom_col = i
                elif part.isdigit() and len(part) > 4:
                    pos_col = i
                elif len(part) in [1, 2] and part.replace('A', '').replace('C', '').replace('G', '').replace('T', '') == '':
                    geno_col = i

            if rsid_col is not None and chrom_col is not None and pos_col is not None:
                try:
                    chrom = parts[chrom_col].strip('"').strip().replace('chr', '')
                    if chrom == 'MT':
                        chrom = 'M'

                    genotype = parts[geno_col].strip('"').strip() if geno_col is not None else 'NN'

                    data.append({
                        'rsid': parts[rsid_col].strip('"').strip(),
                        'chromosome': chrom,
                        'position': int(parts[pos_col].strip('"').strip()),
                        'genotype': genotype
                    })
                except (ValueError, IndexError):
                    continue

    return pd.DataFrame(data) if data else None
