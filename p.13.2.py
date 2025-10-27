# selection sort pt. 2 : biggest to smallest

def select(poolist):
    if len(poolist) <= 1:
        return poolist
    else: 
        i = 0
        while i < len(poolist) - 1: 
            biggest = poolist[i] # then prove if not biggest or yes
            b = i + 1



