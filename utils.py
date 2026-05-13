def parsePDB(file_name):
    with open(file_name,'r') as file:
        line = file.readline()
        while line [0:6].strip() != "TER":
            if line[0:6].strip() == "ATOM":
                atom_name = line[12:16].strip()
                res_name = line[17:20].strip()
                chain_id = line[21:22].strip()
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                print(f"{atom_name} {res_name} {chain_id} {x} {y} {z}")
            line = file.readline()
    RNA = "RNA found in " + file_name 
    return RNA                        

def generate_dot_bracket(model):
    print("dot-bracket notation of the " + model) 