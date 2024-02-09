import pandas as pd
import numpy as np

# Your existing code for reading the file and creating raw_list

# Safe splitting function
def safe_split(source, separator, index, default=None):
    parts = source.split(separator)
    return parts[index] if len(parts) > index else default

# Parse out the desired information with safety checks
PDB_id_lst = [safe_split(x, '_', 0) for x in raw_list]
PDB_chain_lst = [safe_split(safe_split(x, '_', 1, ''), ' ', 0, '').lower() for x in raw_list]
PDB_type_lst = [safe_split(safe_split(x, 'mol:', 1, ''), ' ', 0) for x in raw_list]
PDB_seq_lst = [safe_split(x, '###', 1) for x in raw_list]
PDB_seq_len_lst = [len(x) for x in PDB_seq_lst]

# Your existing code for creating the DataFrame and saving it to CSV

print('Step 0 is finished by generating two files : pdb_pep_chain & pdbid_all_fasta!')
