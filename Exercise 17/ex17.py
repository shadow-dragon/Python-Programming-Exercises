#Code is altered as per Study drills

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.") 

# we could do these two on one line, how?

print(f"The input file is {len(open(from_file).read())} bytes long")

#print(f"Does the output file exist? {exists(to_file)}.")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#The code as been condensed
open(to_file, 'w').write(open(from_file).read())

print("Alright, all done.")

#out_file.close()
#in_file.close()
