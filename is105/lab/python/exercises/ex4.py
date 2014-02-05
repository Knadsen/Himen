#We have 100 cars
cars = 100
#Every car can contain 4 people
space_in_a_car = 4.0
#There are only 30 drivers, assumely 1 per car
drivers = 30
#And 90 passangers
passengers = 90
#With only 30 drivers on 100 cars, 70 of these must be undriven
cars_not_driven = cars - drivers
#The driven cars equals the number of drivers
cars_driven = drivers
#The total capacity of the carpool lane is the number of cars over space in said cars
carpool_capacity = cars_driven * space_in_a_car
#To find the avarege number of used car space, we divide number of passangers with the number of cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


print "Exercise 4, study drill 6:"
x = 5
y = 25
j = 43
k = 89

print "Calculator test:"
print float(k/j*x)
