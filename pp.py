# String Checklist 

# create an empty string 
 empty_string = ""
 ver2 = ''

 # determine if a string is empty 
 # method 1:
 if not str_var:
    print("str_var is empty!")

if len(str_var) == 0:
    print("str_var is empty!")


# Format a string to contain dynamic data
name = "Fluffington"
str_var = f"Hello{name}!"


# Access individual characters/items in a string
print(name[0]) # --> F
print(name[-2]) # --> o


# Access the first, access the last item in a string
print(name[0]) #zero index is always first
print(name[len(name)-1]) # this gives last
print(name[-1]) # this also gives last


# Join two/multiple strings together
a = "poo"
b = "poo"
c = a + b
print(c) # we expect poopoo


# Reversing a string
temp = "park"
reversed_temp = temp[::-1]
v2 = ''.join(reversed(temp)) #haven't learned yet


# create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp

# Compare strings for equality
a = "marshal"
b = "dog"
status = a == b

# determine the minimum and maximum value within a stirng 
temp = "hydroflask"
print(max(temp))
print(min(temp))
print(max('hello', 'goodbye'))
print(min('1','2','3','!')) 

# determine if an item or a pattern exists within a string 
word = "poopooplatter"
if "poo" in word:
    print("there is poo!")

# locate the index of an item or a pattern within a string 
poop_location = word.find("poo")
poop_location = word.index("poop")

# count how often an item or a pattern occurs within a string 
poop_count = word.count("poo")

# convert all items in a string to uppercase/lowercase
yell_hydroflask = "hydroflask".upper()
calm_hydroflask = yell.hydoflash.lower()

# determine if the string can be converted to an integer 
# convert a string to an integer
str_num = "67"
num = 0
if str_num.isdigit():
    num = int(str_num)

# determine if a string only contains alphabetical char
word = shsm.isalpha()

#remove non-alphabetical characters from a string 
# sometimes it is easier to create than remove 
gibberish = "!@#Ebsdiieabiudu"
clean = ""
i = 0 
while i < len(gibberish):
    if gibberish[i].isalpha: 
       clean += gibberish
    i += 1

#remove all alphabetical characters from a string
gibberish = "!@#Ebsdiieabiudu"
clean = ""
i = 0 
while i < len(gibberish):
    if gibberish[i].isalpha == False:
       clean += gibberish
    i += 1

# remove all whitespaces from a string 
example = "h h h h h e        l l o"
example = example.replace(" ", "")

# sort a string in ASCII order or reverse-ASCII order


# determine if a string follows a ruleset 
    # a. Ex. proper email address ; proper password 
