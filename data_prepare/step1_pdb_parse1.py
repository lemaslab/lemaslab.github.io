import pandas as pd
import numpy as np

# Step 0: parse the fasta file downloaded from the RCSB PDB
# INPUT : pdb_seqres.txt
# OUTPUT: pdb_pep_chain, pdbid_all_fasta

raw_str = ''
with open(r'C:\Users\danmo\Downloads\pdb_seqres.txt\pdb_seqres.txt', 'r') as f:
    for line in f.readlines():
        raw_str += line.replace('\n', '###')
raw_list = raw_str.split('>')
del raw_list[0]

# Updated code with additional checks
PDB_id_lst = [x.split('_')[0] for x in raw_list if '_' in x]  # Ensuring underscore is present

PDB_chain_lst = []
for x in raw_list:
    parts = x.split('_')
    if len(parts) > 1 and ' ' in parts[1]:
        PDB_chain_lst.append(parts[1].split(' ')[0].lower())
    else:
        PDB_chain_lst.append('unknown')  # Placeholder for missing or incorrectly formatted chain info

PDB_type_lst = []
for x in raw_list:
    parts = x.split('mol:')
    if len(parts) > 1 and ' ' in parts[1]:
        PDB_type_lst.append(parts[1].split(' ')[0])
    else:
        PDB_type_lst.append('unknown')  # Placeholder for missing or incorrectly formatted type info

PDB_seq_lst = []
for x in raw_list:
    parts = x.split('###')
    if len(parts) > 1:
        PDB_seq_lst.append(parts[1])
    else:
        PDB_seq_lst.append('unknown')  # Placeholder for missing sequence

PDB_seq_len_lst = [len(seq) for seq in PDB_seq_lst if seq != 'unknown']  # Only calculate length if sequence is known

# Creating the DataFrame
df_fasta_raw = pd.DataFrame(list(zip(PDB_type_lst, PDB_seq_len_lst, PDB_seq_lst, PDB_id_lst, PDB_chain_lst)),
                            columns=['PDB_type', 'PDB_seq_len', 'PDB_seq', 'PDB_id', 'chain'])

# Filtering the DataFrame for sequences <= 50 and type 'protein'
df_fasta = df_fasta_raw[(df_fasta_raw['PDB_seq_len'] <= 50) & (df_fasta_raw['PDB_type'] == 'protein')]

# Saving the DataFrames to TSV
df_fasta_raw.to_csv(r'C:\Users\danmo\Downloads\pdbid_all_fasta.tsv', encoding='utf-8', index=False, sep='\t')
df_fasta.to_csv(r'C:\Users\danmo\Downloads\pdb_pep_chain.tsv', encoding='utf-8', index=False, sep='\t')

print('Step 0 is finished by generating two files: pdb_pep_chain & pdbid_all_fasta!')
