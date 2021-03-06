#!/usr/bin/env python

class Atom:
    def __init__(self,name,x,y,z):
        self.name = name;
        self.x = x;
        self.y = y;
        self.z = z;

def parse_a_segment(f,atom_list):
    try:
        count = int( f.readline().split()[0])
    except:
        return False
    else:
        f.readline()  # the comment line
        for i in range(count):
            try:
                segs = f.readline().split()
                xyzs = (float(segs[i]) for i in range(1,4))
                atom = Atom(segs[0],*xyzs)
                atom_list.append(atom)
            except:
                return False
        return True


def parse_file(file_name,atom_list):
    try:
        f = open(file_name,'r')
    except:
        print("Can't open file "+str(file_name))
    else:
        while(parse_a_segment(f,atom_list)):
            pass

import sys
atoms = []
for i in range(1,len(sys.argv)):
    parse_file(sys.argv[i],atoms)

print(" %d" % len(atoms))
print("Generated by xyzcat.py")
for i in atoms:
    print("%s %.8f %.8f %.8f" % (i.name, i.x, i.y, i.z) )

    
