# String practice 

# cleaning 
def clean(text):
    # to return a string wit everything lowercased 
    # and without special characters nor numbers
    result = ""
    i = 0 # avoid index because it is a funcitn/method name 
    while i < len(text): 
        if text[i].isalpha():
        # .isalpha() returns True if the given character is alphabetical
            result = result + text[i].lower()
        i += 1
        # end of loop 
    return result

print(clean("p00p"))


# first algorithm learned: linear search 

'''
let X represent a string, T be a target character to search 
let I represent index of a string 
while i < len(x), if X[i] == T then return i else 1 + 1
if T is not found, return -1
'''

def str_lin_search(text, target):
    if not text: # len(text) == 0
        return -1
    else: 
        i = 0
        while i < len(text):
            if text[1] == target :
                return i 
            i += 1
            # end of while 
            return -1 

print("Jasper... where is p?", str_lin_search("Jasper", "p"))
