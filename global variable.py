a = 10
print(a)
def f1():
    global a
    a = 20
    print("a Inside f1: ",a)
def f2():
    print("Inside f2...")
    print("a:", a)

""" 
f1()
f2() """

f2()
f1()
print(globals())