### This is the main file
import NLS_seq_module as ns
import brute_force as bf
import MM
NLS_list = ns.NLS_list

def find_NLS(fasta_object):
    # loop over NLS_list and apply brute force for each
    possible_hits = []
    for pattern in NLS_list:
        best_match = bf.brute_force(fasta_object.sequence,pattern)
        possible_hits.append(best_match)
    return (possible_hits)

import os
import fasta_parsing as fp
files = []
P_files = os.listdir('DataSet/NLSP')
N_files = os.listdir('DataSet/NLSN')
for file in P_files:
    files.append('DataSet/NLSP/' + file)
for file in N_files:
    files.append('DataSet/NLSN/' + file)

for path in files:
    query = fp.Fasta_File(open(path).readlines())
    hits = find_NLS(query)
    score_list = []
    for i in range(len(hits)):
        percent_score = MM.protein_score(NLS_list[i],hits[i][0])
        score_list.append(percent_score)
    max_score = max(score_list)
    max_idx = score_list.index(max_score)
    query.nls = hits[max_idx][0]
    query.trueNLS = NLS_list[max_idx]
    query.nls_score = max_score
    query.folder = path.split('/')[1]
    #tt = (path, NLS_list[max_idx],hits[max_idx][0],int(max_score))
##    print(path)
##    print(NLS_list[max_idx])
##    print(hits[max_idx][0])
##    print(max_score)
    #print(tt)
    print(query.folder, query.AccNum, int(query.nls_score), query.nls, query.trueNLS, sep='\t')

