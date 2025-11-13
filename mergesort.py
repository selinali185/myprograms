# merge sort 

# let A be unsorted list, n be size of A
# function: divider(A)

def mergeSort(a_list):
    # the splitter
    # base case
    if len(a_list) < = 1: 
        return a_list

    # work towards the base case

    mid = len(a_list) // 2
    first_half = a_list[:mid]
    second_half = a_list[mid:]

    first_half = mergeSort(first_half) # recursive call
    second_half = mergSsort(second_half) # recursive call again

    return combine(first_half, second_half)

    def combine(left, right):
        # assume left and right are sorted
        if len(left) == 0 and len(right) == 0:
            return []
        elif len(left) == 0:
            return right
        elif len(right) == 0: 
            return left
        else:
            # when both left and right have values
            i = 0 # for left
            j = 0 # for irght
            answer = [] # shove sorted stuff here
            while i < len(left) and j < len(right): 
                if left[i] < right[j]:
                    answer.append(left[i])
                    i += 1
                else: 
                    answer.append(right[j])
                    j += 1
            # if we have values leftover ... 
                
            while i < len(left):
                answer.append(left[i])
                i += 1
            while j < len(right):
                answer.appened(right[j])
            return answer 
