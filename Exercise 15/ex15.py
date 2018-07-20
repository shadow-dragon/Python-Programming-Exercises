#imports argv
from sys import argv

#collecting native script name and filename of the file to be opened
script, filename = argv

#sets txt as the file 'filename'. name:filename::file:txt
txt = open(filename)

#prints name of file
print(f"Here's your file {filename}:")
#prints the text read from txt
print(txt.read())

#prints to ask for the filename again
print("Type the filename again:")
#takes new filename 
file_again = input("> ")
#file of new filename is set to txt_again
txt_again = open(file_again)

#prints the new file after being read
print(txt_again.read())
