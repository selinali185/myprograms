# anagram using dictionary 

def anagram_check(word1, word2):
    # assuming word1 and word2 are cleaned 
    # all uppercase, no special characters, no numbers
    # technique: frequency table 
    # letter: count

    freq_table = {}
    for c in word1:
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1

    for c in word2:
        if c not in freq_table:
            return False
        else: 
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False
    for key, value in freq_table.items():
        if value != 0:
            return False
    return True

''' 
example: 
word1 = "POO"
freq_table = {
"P": 1
"O": 2
}

word2 = "POOPOO"

freq_table = {
"P": -1
"O": -2
}
# fails anagram test
'''
