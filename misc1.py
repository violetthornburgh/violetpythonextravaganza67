'''
a = 5
b = 10

a,b = b,a

print(a)
print(b)
---------------------------------------------------------------------
strlng = input("gimme astring ")

print(strlng[::-1])
---------------------------------------------------------------------
numbs = [3, 5, 9, 10, 6, 7, 2]

min = numbs[0]
max = numbs[0]

for num in numbs:
    if min < num:
        min = num
        
    if max > num:
        max = num
        
        
print(min)
print(max)
---------------------------------------------------------------------
numbs = [3, 5, 9, 3, 10, 6, 6, 7, 2]

a = set(numbs)
b = list(a)

print(b)
---------------------------------------------------------------------
numbs = [3, 5, 9, 3, 10, 6, 6, 7, 3]

var = len(numbs)

def tf():
    if numbs[0] == numbs[var-1]:
        print("true")
    else:
        print("false")
        
tf()
---------------------------------------------------------------------
numbs = [3, 5, 9, 3, 10, 25, 6, 6, 7, 3]

prn = ""
    
for num in numbs:
    if num%5 == 0:
        prn = prn+str(num) +", "
    
print(prn)
----------------------------------------------------------------------

'''
