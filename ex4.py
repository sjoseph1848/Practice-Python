cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are"), print(cars), print("cars available")
print ("There are only"), print(drivers), print("drivers available")
print ("We can transport"),print(carpool_capacity), print("people today.")
print("We have"),print(passengers),print("to carpool today")
print("We need to put about"), print(average_passengers_per_car), print("in each car")
