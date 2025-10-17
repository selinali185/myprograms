# list skills checklist 

# create an empty list 
a_list = []
b_list = ()

# determine if a string is empty 
if not a_list:
    print("empty")

if len(a_list) == 0: 
    print("empty")

# what does len(), sum(), min(), max() do when a list is an argument? 
c_list = [3,1,4,1,5,9]
print(len(c_list)) # = 6
print(sum(c_list)) # = 23
print(min(c_list)) # = 1
print(max(c_list)) # = 9

# access the individual items in a list 
d_list = list("hello, world!") # each characters, inclding "," and " " will be an item --> 13 individual strings
print(d_list[0]) # = "h"
print(d_list[-1]) # = "!"
print(d_list[1:4]) # = "e", "l", "l"

# join two/multiple lists togetehr 
a = [3,1,4]
b = ["Marshall", "Freya", "Joy"]
c = a + b # creates new list of a and b joined 
a.extend(b) # mutates a to give contents of b
a = [3,1,4]
for item in b:
    a.append(item) #add end 

# reverse a list (two ways)


# create a copy of a list (two ways)

# compare lists for equality 
