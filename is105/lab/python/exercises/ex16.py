#imports the argv module
from sys import argv

#assigns the first argument (second after script file) to variable "filename"
script, filename = argv

print "We're going to erase %r" %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."


raw_input("?")

print "Opening the file..."
#assigns variable "target" to function open with the "filename"(which would be the first argument) as the target, and adds string 'w' wchich would write the file in the command prompt
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#empties the file using the truncate function
target.truncate()

print "Now I'm going to ask you for three lines."

#asks for three different string inputs, one for each variable
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
#Close and save
target.close()
