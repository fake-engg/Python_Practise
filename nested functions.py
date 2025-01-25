""" def manager():
    def employee(name,sal):         #nested function
        print("Name of the employee: ",name)
        print("Salary of the employee: ",sal)
        print()

    employee('Shivam',25000)            #outer function is calling the inner functions 
    employee('Abhishek',45000)
    employee('Ankit',70000)

manager()
 """

def outer():
    print("Inside outer function..")
    global inner
    def inner():
        print("Inside Inner function..")
    print("Outer function returns inner function...")
    return inner

f1 = outer()        # inner function is returned and not executed
f1()                # this will execute the inner function
print(globals())
inner()