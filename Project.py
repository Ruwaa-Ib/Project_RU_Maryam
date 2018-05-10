import re

filename=input('Enter The Name of Your Fasta File with Full Directory. ')
file=open(filename)
file=file.readlines()
class Fasta_File:
#the class takes an opened, read fasta file that contains a single protein.
    def __init__(self,file):
        self.parse(file)
    #parse the file
    def parse(self,file):
        seq=' '
        self.DB='No DB in the given file'
        self.AccNum='No accession number in the given file'
        self.EntryName='No entry name in the given file'
        self.ProtName='No protein name in the given file'
        self.organism='No organism name in the given file'
        self.seq=seq
        for line in file:
            if line[0]==">":
                line=line.lstrip(">")
                line=line.split("|")
                self.DB=line[0]
                self.AccNum=line[1]
                line[2]=line[2].split()
                self.EntryName=line[2][0]
                del line[2][0]
                line[2]=" ".join(line[2])
                line[2]=line[2].split("OS")
                self.ProtName=line[2][0]
                organism=line[2][1].split("(")
                organism=organism[0]
                organism=organism.lstrip("=")
                self.organism=organism
            else:
                seq+=line
        seq="".join(seq)
        self.sequence=seq
        if self.sequence==' ':
            self.sequence='No sequences in the given file'
    def __repr__(self):
        return (self.sequence)
    def __str__(self):
        return(self.sequence)

#NLS=#contain all the NLS consensus sequences (will be a list or dict idk yet)

file=Fasta_File(file)
def find_NLS(seq):
    macth=re.search("SOME NLS SEQ",self.sequence)
    if match=='None':
        return(match)
    else:
        start=match.start()
        end=match.end()
        matchseq=self.sequence[start:end]
        return('NLS sequence found form ', start,' to ',end,' is: ',matchseq)
    
    


        
