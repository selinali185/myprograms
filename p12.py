# code cleaning crew to find only upper and postiive int

unclean = input("enter product code: ")
lowercase = ""
uppercase = ""
non_letters = ""
for item in unclean: 
    if item.isalpha() and item.islower(): 
        
