class Fasta_File:
#the class takes an opened, read fasta file
#that contains a single protein.
    def __init__(self,file):
        self.DB = 'No DB in the given file'
        self.AccNum = 'No accession number in the given file'
        self.EntryName = 'No entry name in the given file'
        self.ProtName = 'No protein name in the given file'
        self.organism = 'No organism name in the given file'
        self.seq = []
        self.parse(file)

    def parse(self,file):
        seq = []
        for i in range(len(file)):
            line = file[i]
            if line[0]!=">":
                seq.append(line.rstrip())
                if ((i+1) == len(file)):
                    seq = "".join(seq)
                    self.sequence = seq
                    seq = []
                elif (file[i+1][0] == ">"):
                    seq = "".join(seq)
                    self.sequence = seq
                    seq = []
            else:
                line = line.lstrip(">")
                line = line.split("|")
                self.DB = line[0]
                self.AccNum = line[1]
                line[2] = line[2].split()
                self.EntryName = line[2][0]
                del line[2][0]
                line[2] = " ".join(line[2])
                line[2] = line[2].split("OS")
                self.ProtName = line[2][0]
                organism = line[2][1].split("(")
                organism = organism[0]
                organism = organism.lstrip("=")
                self.organism = organism

        if self.sequence == '':
            self.sequence = 'No sequences in the given file'
    def __repr__(self):
        return (self.sequence)
    def __str__(self):
        return(self.sequence)

#for testing    
##filename = input('Enter The Name of Your Fasta File with Full Directory: ')
##file = open(filename).readlines()
##myFile=Fasta_File(file)
##print(myFile, myFile.AccNum)

        
