### This is the main file
#####   #####    ##### File Parsing #####   #####    ##### Maryam
import NLS_seq_module as ns
NLS_list = ns.NLS_list

def find_NLS(fasta_object):
    # loop over NLS_list and apply brute force for each
    pass

import os
import fasta_parsing as fp
P_files = os.listdir('DataSet/NLSP')
N_files = os.listdir('DataSet/NLSN')

for file in P_files:
    path = 'DataSet/NLSP/' + file
    query = fp.Fasta_File(open(path).readlines())
    find_NLS(query)
    print(file, '\n', query)
    print()
    
for file in N_files:
    path = 'DataSet/NLSN/' + file
    query = fp.Fasta_File(open(path).readlines())
    find_NLS(query)
    print(file, '\n', query)
    print()
    
#####   #####    ##### Machine Learning #####   #####    ##### Maryam & RU


#####   #####    ##### Markov Model #####   #####    ##### RU
import MM


#####   #####    ##### Decesion #####   #####    ##### RU
