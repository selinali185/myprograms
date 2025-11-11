# dictionaries exercise

def factors(x):
    result = []
    for v in range(1,x+1):
        if x % v == 0:
            result.appened(v)
    return result 

num = int(input())
table={}
for n in range(2, num+1):
    table[n] = factors(n)