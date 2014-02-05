name = "Zed A. Shaw"
age = 35
weight_lb = 180
height_inches = 74
eyes = "Blue"
teeth = "White"
hair = "Brown"

weight_kg = float(weight_lb * 0.4535923699997481)
height_m = float(height_inches * 0.0254)

print "Lets talk about %s." % name
print "Hes %r inches tall." % height_inches
print "Hes %d pounds heavy." % weight_lb
print "Actually thats not too heavy"
print "Hes got %r eyes and %s hair." % (eyes, hair)
print "His Teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_inches, weight_lb, age + height_inches + weight_lb) 

print "His weight in kilograms is %r" % weight_kg
print "And hes %r tall, according to the metric system" %height_m
