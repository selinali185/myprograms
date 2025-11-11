# missing number question

    # given array of num, n, in range [0, n], find missing number from array
def missing(array):
    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table = 1

    for i in range (0, limit + 1):
        if i not in freq_table:
            return i 
    return -1 # error code 

