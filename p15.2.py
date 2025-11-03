# test prep question 1: mean and median of elements 

def mean(a_list):
    total = 0
    for item in a_list:
        total += item
    average = total / len(a_list)
    return average
result = mean(DATA)
print(f"the mean is {result}")

def median(a_list):
    i = 1
    while 1 < len(a_list):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else: 
                break
            j -= 1
        i += 1
    if len(a_list) % 2 == 1: # odd num
        median_index = len(a_list) // 2
        return a_list
    else: # even num
        middle_index = (len(a_list) // 2) - 1
        middle_also_index = len(a_list) // 2
        result = (a_list[middle_index]) + a_list[middle_also_index] / 2
        return result

result = median(DATA)
print(f"the median is {result}")



