def parsePDB(file_name):
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
            line = file.readline()
    RNA = "RNA found in " + file_name 
    return RNA                        

def generate_dot_bracket(model):
    print("dot-bracket notation of the " + model) 