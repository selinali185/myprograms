# sum of 6

# method 1: brute force

a_list = [1,1,2,3,4,5,6,9]
target = 6

for i in range(len(a_list)):
    for j in range(len(a_list)):
        if i != j and (a_list[i] + a_list[j]) == target:
            print(f"{target happens at ({i}, {j})}")

# method 2
for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)-1):
        if i != j and (a_list[i] + a_list[j]) == target:
            print(f"{target happens at ({i}, {j})}") # prevents repetitive additions 

# method 3 (linear search)
for i in range(len(a_list) -1):
    diff = target - a_list[i]
    for j in range(i + 1, len(a_list)):
        if a_list[j] == diff:
            print("target sum is possible")

# method 3.5 (binary search)
for i in range(len(a_list) -1):
    diff = target - a_list[i]
    for j in range(i + 1, len(a_list)): # to be determined...

# method 5
def two_pointer(array,goal):
    left = 0
    right = len(array) - 1
    while left < right: 
        total = array[left] + array[right]
        if total == goal:
            return True
        else: 
            if total< goal:
                left += 1
            else: 
                right -= 1
    return False
