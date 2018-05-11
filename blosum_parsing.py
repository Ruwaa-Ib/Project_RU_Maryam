# Blosum Parsing
AA = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X']
blosum62Table = open('BLOSUM62.txt').readlines()
blosum62Table = blosum62Table[1:-1]
blosum =[]
for line in blosum62Table:
    line = line.rstrip()
    line = line.split(' ')
    newline = []
    for e in line[1:]:
        if e != '':
            newline.append(e)
    blosum.append(newline)   
length = len(blosum)
BLOSUM62 = []
for i in range(length):
    BLOSUM62.extend(blosum[i][:i+1])
#BLOSUM_1D = open("BLOSUM_1D.txt",'w').write('\t'.join(BLOSUM62))

### The output of this module is BLOSUM62,,, which is a 1D Array of the blosum lower triangular matrix
### use the access function for A[i,j] = BLOSUM62[(i*(i-1)/2)+j]
