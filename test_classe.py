#!/usr/bin/env python3

class Protein : 
    def __init__(self,name):
        self.name = name
        self.folded = True

    def unfold (self): 
        self.folded = False

    def fold (self):
        self.folded= True


prot1 = Protein ('hemoglobin')
prot2 = Protein ('cytochrome')
prot3 = Protein ('ovalbumin')

proteome = [prot1,prot2,prot3]

print('before')
for prot in proteome: 
    print(prot.name+ 'is folded:', prot.folded)

for prot in proteome: 
    prot.unfold()

print ('after')
for prot in proteome: 
    print(prot.name + 'is folded' ,prot.folded)

