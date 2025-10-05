def fib(n):
    if n in {0, 1}:
        return num
    else:
        location = 2
        two_before = 0
        one_before = 1
        total_sum = 0
        while location <= n:
            total_sum = two_before + one_before
            two_before = one_before
            one_before = total_sum
            location += 1

        return total_sum 

    i = 0 
    while i < 10:
        