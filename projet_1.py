#!/usr/bin/env python3

import sys, utils

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    print("usage:")
    print("> projet_1.py file.pdb>")
    exit()

pdb_name = sys.argv[1]

RNA = utils.parsePDB(pdb_name)
utils.generate_dot_bracket(RNA) 