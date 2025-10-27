# selection sorting list: non-destructive  

def select(a_list):
    if len(a_list) <= 1:
        return a_list
    else: 
        i = 0
        while j < len(a_list):
            smallest = a_list[i] # then prove if it is or not 

        # start of hunt
            j = i + 1 # search from i + 1 onwards
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value
                    new_location = j

                j += 1
        # end of hunt

            # then swap smallest into proper location 
        temporary = a_list[i]
        a_list[i] = smallest
        a_list[new_location] = temporary

        # python way: 
        # a_list[i], a_list[new_location] = a_list[new_location], a_list[i]

        i += 1 # access each value in a_list within current_value
