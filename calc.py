def sum(a, b):
    return (a + b)
    
def sub(a, b):
    return (a - b)

def prod(a, b):
    return (a*b)
    
def quo(a, b):
    return (a/b)
    
def mod(a, b):
    return (a % b)

    
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

if (a % 2 == 0):
    print (f'{a} is even')
else:
    print (f'{a} is odd')
    
if (b % 2 == 0):
    print (f'{b} is even')
else:
    print (f'{b} is odd')

print(f'product of {a} and {b} is {prod(a, b)}')

print(f'Sum of {a} and {b} is {sum(a, b)}')

print(f'remainder of {a} and {b} is {mod(a, b)}')


#if (a*b <= 1000):
    #print(f'product of {a} and {b} is {prod(a, b)}')
#else:
    #print(f'Sum of {a} and {b} is {sum(a, b)}')
#-------------------------------------------------------------------------------------------------
'''
prevnum = 0

for i in range (0, 10):
    sum = prevnum + i
    print(f'current number is {i}, previous number is {prevnum}, sum is {sum}')
    prevnum = i

------------------------------------------------------------------------------------------------------
string = input("give a string ")

print(string[0::2])

for i in range(len(string)):
    if (i%2 == 0):
        print(string[i])

    
'''
