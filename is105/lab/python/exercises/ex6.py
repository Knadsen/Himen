#Assigns the variable x to a string, the ending number deciding what %d represents
x = "There are %d types of people." % 10
#variable binary to string
binary = "binary"
#The same with this
do_not = "dont"
#The same as the first line, only with multiple format characters
y = "Those who know %s and those who %s." % (binary, do_not)

#The next two lines simply print their strings
print x
print y

#And these two extend on those strings..kind of puts a string within another
print "I said: %r." % x
print "I also said: %s." % y

#hilarious boolean set to False
hilarious = False 
#This string would need something to assign %r to work
joke_evaluation = "Isnt that joke so funny?! %r"

#Well..
print joke_evaluation % hilarious 

#Every line, really?
w = "This is the left side of..."
e = "a string with a right side."

#Self explainatory
print w + e
