import math

class TertiaryCoordinates:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
class atom :
    def __init__(self, atom_name, res_name, position, chain_id, x, y, z):
        self.atom_name = atom_name
        self.res_name = res_name
        self.position = position
        self.chain_id = chain_id
        self.coord = TertiaryCoordinates(x, y, z)

class nucleotide :
    def __init__(self, res_name, position, chain_id):
        self.res_name = res_name
        self.position = position
        self.chain_id = chain_id
        self.atoms = []
class HydrogenBond :
    def __init__(self, atom1, atom2, distance):
        self.atom1 = atom1
        self.atom2 = atom2
        self.distance = distance
class BasePair :
    def __init__(self, nucleotide1, nucleotide2, h_bonds):
        self.nucleotide1 = nucleotide1
        self.nucleotide2 = nucleotide2
        self.h_bonds = h_bonds

class RNA :
    def __init__(self, nucleotide):
        self.nucleotide = nucleotide
    
    def get_sequence(self):
        sequence = ""
        for n in self.nucleotide:
            sequence += n.res_name
        return sequence

def calculer_distance(coord1, coord2):
    partie_x = (coord2.x - coord1.x) ** 2
    partie_y = (coord2.y - coord1.y) ** 2
    partie_z = (coord2.z - coord1.z) ** 2
    distance = math.sqrt(partie_x + partie_y + partie_z)
    return distance

def parsePDB(file_name):
    dico_nucleotide = {}
    with open(file_name,'r') as file:
        line = file.readline()
        while line [0:6].strip() != "TER":
            if line[0:6].strip() == "ATOM":
                atom_name = line[12:16].strip()
                res_name = line[17:20].strip()
                position = line[22:26].strip()
                chain_id = line[21:22].strip()
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                print(f"{atom_name:<4} {position:<4} {res_name:<3} {chain_id:<2} {x:>12f} {y:>12f} {z:>12f}")
                if position not in dico_nucleotide:
                    dico_nucleotide[position] = nucleotide(res_name, position, chain_id)
                nouveau_atom = atom(atom_name, res_name, position, chain_id, x, y, z)
                dico_nucleotide[position].atoms.append(nouveau_atom)        
            line = file.readline()
    list_nucleotide = list(dico_nucleotide.values())
    mon_rna = RNA(list_nucleotide)
    return mon_rna                        

def generate_dot_bracket(model):
    print("dot-bracket notation of the "+ str(model))
    print(" LA SÉQUENCE :", model.get_sequence()) 

    list_nucleotide = model.nucleotide
    taille = len(list_nucleotide) 

    structure = ["."] * taille
    for i in range(taille):
        for j in range(i+1, taille):
            nucleotide1 = list_nucleotide[i]
            nucleotide2 = list_nucleotide[j]
            for atom1 in nucleotide1.atoms:
                for atom2 in nucleotide2.atoms:
                    distance = calculer_distance(atom1.coord, atom2.coord)
                    if distance < 3:
                        structure[i] = "("
                        structure[j] = ")"
    structure_str = "".join(structure)
    print(" LA STRUCTURE :", structure_str)