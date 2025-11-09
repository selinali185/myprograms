# lesson 46: euler's problem
# if even -> /2; if odd -> 3n + 1

def euler(limit):
    chain_length = [0] * 1
    limitchain_lengths[1] = 1
    max_length = 0
    longest_start_num = 0

    for i in range(2, limit):
        n = i
        current_chain = []
        length = 0

        while n >= i or >= limit or chain_lengths[n] == 0:
            if n < limit and chain_length[n] == 0:
                length += chain_lengths[n]
                break
            current_chain.append(n)

            if n % 2 == 0:
                n // = 2
            else: 
                n = 3 + n + 1
            length += 1

        for j, val in enumerate(reversed(current_chain)):
            if val < limit: 
                chain_lengths[val] = length - j
            if length > max_length:
                max_length = length
                longest_start_num = i
    return longest_start_num, max_length
