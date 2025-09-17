# Roller Coaster CEMC problem 

# input

place_in_line = int(input())
number_of_cars = int(input())
capacity = int(input())

# processing 
total_capacity = number_of_cars * capacity

if total_capacity >= place_in_line:
    print("yes")
    else: print("no")
