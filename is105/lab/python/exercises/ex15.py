#Imports the argv module
from sys import argv

#Assigns the argument to variable "filename"
script, filename = argv

#Uses the "open" function with variable "filename" in the paratheses and puts it in variable "txt"
txt = open(filename)

#simple print line
print "Here's your file %r:" % filename
#Uses the "read" function to print the content of "filename"
print txt.read()


print "Type the filename again:"
#same idea as before, but this time instead of using the argument from the command prompt when executung the file, we as for a raw input, and assign it to variable "file_again"
file_again = raw_input("> ")

#another open function
txt_again = open(file_again)

#another read function, same as above
print txt_again.read()

