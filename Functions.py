# Function returning multiple values

def calculation(a,b):
    return a+b, a-b,a*b,a/b


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
n = calculation(a,b)
for x in n:
    print(x,end=',')

