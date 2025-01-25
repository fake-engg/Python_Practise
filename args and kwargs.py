def calculation(a,b):
    return a+b, a-b,a*b,a//b


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
n = calculation(a,b)
print(type(n))
for x in n:
    print(x)


def calc(*n):
    #print(n)
    sum=0
    for x in n:
        sum = sum + int(x)

    print("Inside calc function....")    
    print("Sum of tuple values are: ",sum)


calc(n)


""" t = (2,5,8,3)

def sum(*t):
    result = 0
    print(t)
    for x in t:
        print(type(x))
        print(x)

    print(x)

sum(t)
 """