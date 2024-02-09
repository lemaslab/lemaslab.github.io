import pandas as pd
import numpy as np

# Safe splitting function
def safe_split(source, separator, index, default=None):
    parts = source.split(separator)
    return parts[index] if len(parts) > index else default

# Step 0: parse the fasta file downloaded from the RCSB PDB
# INPUT : pdb_seqres.txt
# OUTPUT: pdb_pep_chain, pdbid_all_fasta

# Initialize an empty string to accumulate the lines
raw_str = ''

# Read the file and accumulate the lines into raw_str
with open(r'C:\Users\danmo\Downloads\pdb_seqres.txt\pdb_seqres.txt', 'r') as f:
    for line in f.readlines():
        raw_str += line.replace('\n', '###')

# Split the accumulated string into a list, remove the first empty entry
raw_list = raw_str.split('>')
del raw_list[0]

# Parse out the desired information with safety checks
PDB_id_lst = [safe_split(x, '_', 0) for x in raw_list]
PDB_chain_lst = [safe_split(safe_split(x, '_', 1, ''), ' ', 0, '').lower() for x in raw_list]
PDB_type_lst = [safe_split(safe_split(x, 'mol:', 1, ''), ' ', 0) for x in raw_list]
PDB_seq_lst = [safe_split(x, '###', 1) for x in raw_list]
PDB_seq_len_lst = [len(x) for x in PDB_seq_lst]

# Create a DataFrame from the parsed lists
df_fasta_raw = pd.DataFrame(list(zip(PDB_type_lst, PDB_seq_len_lst, PDB_seq_lst, PDB_id_lst, PDB_chain_lst)),
                            columns=['PDB_type', 'PDB_seq_len', 'PDB_seq', 'PDB_id', 'chain'])

# Filter the DataFrame based on sequence length and type
df_fasta = df_fasta_raw[(df_fasta_raw.PDB_seq_len <= 50) & (df_fasta_raw.PDB_type == 'protein')]

# Save the DataFrames to TSV files
df_fasta_raw.to_csv(r'C:\Users\danmo\Downloads\pdbid_all_fasta.tsv', encoding='utf-8', index=False, sep='\t')
df_fasta.to_csv(r'C:\Users\danmo\Downloads\pdb_pep_chain.tsv', encoding='utf-8', index=False, sep='\t')

# Print a completion message
print('Step 0 is finished by generating two files: pdb_pep_chain & pdbid_all_fasta!')
