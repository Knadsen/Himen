def inches_to_meters(inches, feet):
	a = float(inches * 0.0254)
	b = float(feet * 0.3048)
	return a + b

	
	
def meters_to_feet(meters):
	feet = meters * 3.2808399 
	inches = (feet * 12) % 12
	return int(feet), inches



test = inches_to_meters(2, 53)
test2 = inches_to_meters (84, 53)
test3 = meters_to_feet(1.82)
test4 = meters_to_feet(2.01)
test5 = meters_to_feet(1.45)
print test
print test2
print test3, test4, test5


