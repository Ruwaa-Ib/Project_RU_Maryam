### Markov Model
AA = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X']
# X stands for any amino acid

##import blosum_parsing as b
##BLOSUM62 = b.BLOSUM62
BLOSUM62 = open('BLOSUM_1D.txt').read().split('\t')

def AA_score(A1, A2):
    # This function returns the score of 1 amino acid
    i = AA.index(A1)
    j = AA.index(A2)
    if j > i:
        i,j = j,i
    x = sum(range(1, i+1))+ j
    return int(BLOSUM62[x])

def protein_score(NLS, seq):
    score = 0
    trace = 0
    L = len(NLS)
    for i in range(L):
        score = score + AA_score(NLS[i], seq[i])
        trace = trace + AA_score(NLS[i], NLS[i])
    percent_score = score/trace*100
    return percent_score

