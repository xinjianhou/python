#1
print('hello world!')
print("hello again")
print("I like typing this.")
print("This is fun.")
print("Yay,printing.")
print("I'd much rather you 'not' .")
print('I "said" do not touch this.')
#4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven

print("There are ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to transport today")
print("We need to put about", average_passengers_per_car, "in each car.")
#5
my_name = 'Zed A. Shaw'
my_age = '35 # not a lie'
my_height = 175  # centimeter
my_weight = 60  # kilogram
my_eyes = 'black'
my_teech = 'white'
my_hair = 'black'

print(f"Let's talk about {my_name}.")
print(f'he is {my_height}cm heigh.')
print(f'he is {my_weight}kg weight')
print(f"he's got a {my_eyes} eyes and {my_hair} hair")
#7
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said {x}")
print(f"I also said {y}")

hilarious = False
jock_evalution = "Isn't that jock  so funny?! {}"

print(jock_evalution.format(hilarious))

w = "this is a left side of ..."
e = "a string with a righ side."

print(w + e)
