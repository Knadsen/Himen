#Defines the function and takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

print "We can just give the function numbers directly:"
#Directly initializes the arguments, gives them values, and runs the script
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
#assigns the variables values for further use
amount_of_cheese = 10
amount_of_crackers = 50

#We can now put our values to good use
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#Two simple math statements, seperated by a comma
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#A combination of the two
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def waysToFunction(x, y):
	print "This is x: %d" %x
	print "This is y: %d \n" %y

v1 = 12
v2 = 8

waysToFunction (10, 5)
waysToFunction (10 + 3, 4 + 8)
waysToFunction (v1, v2)
waysToFunction (v1 + v2, v2)
waysToFunction (v2, v1 + 5)
waysToFunction (int(raw_input("?")), v2)
waysToFunction (v2 + (v1*30), 11)
