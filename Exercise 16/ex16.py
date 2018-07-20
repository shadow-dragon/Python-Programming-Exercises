#importing argv
from sys import argv

#taking the script name and file name
script, filename = argv

#printing intro instructions
print(f"We're going to erase {filename}")
print("If you don't want thar, hit CTRL-C (^C).")
print("If you do want that, hit RETURN. ")

#taking user input for actions
#to be done on the file
input("?")

#printing opening the file
print("Opening the file...")
#opening the file
target = open(filename, 'w')

#print truncating the file
print("Truncating the file. Goodbye!")
target.truncate()

#taking three lines of input
print("Now I'm gonna ask you for three lines to put in the file")

line1 = input("line 1: ") 
line2 = input("line 2: ") 
line3 = input("line 3: ") 

#compiling the three lines into a single message
message = line1 + "\n" + line2 + "\n" + line3 + "\n"

#printing that these lines will be added to the file
print("I'm going to write these to the file.")

#writing the compiled message into the file
target.write(message)
#printing that the file is going to get closed now
print("And finally, we close it.")

#closing the file
target.close()

print("Goodbye!")
