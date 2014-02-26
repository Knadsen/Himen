#imports argv module
from sys import argv

#'Unpacks' argv, assigning variable 'input_file' as the first (second after script) argument
#This is the name of the file which we will be using
script, input_file = argv

#defines a function 'print all' with one argument
#It utilizes the read() function, wchich will print the text of our file, eventually, when the function is called
def print_all(f):
	print f.read()

#Another function is made, this one to seek out the first line in our file
#Using 0 instead of 1 will be important, as it would otherwise seek the second line of text
def rewind(f):
	f.seek(0)

#A third function, this one to print a single line and now with two arguments
#We would like to display the line number, therefor require that information
#Printing both the line count and the line itself; using a readline() function
def print_a_line(line_count, f):
	print line_count , f.readline()

#Opens the file and prepares for use
#Again, using the argument from our initial function
#Assigns it's content to a variable for practical use
current_file = open(input_file)

print "First let's print the whole file:\n"

#Our print all function used to print the files' content
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#We're now at the top of our file (or actually our variable 'current_file')
rewind(current_file)

print "Let's print three lines:"

#Kind of tedious, but consistant non the less
#Increases the value of 'current_line' by one for every entry. Thus changing the number which our function will print
#Does this three time, with three different lines
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
