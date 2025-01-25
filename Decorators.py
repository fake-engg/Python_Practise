""" def newFunctionality(wish):
    def nameCheck(name):
        if name == 'Anna':      # this is the added functionality i.e. conditional check
            print("Bad morning ",name)
        else:
            wish(name)
    return nameCheck

@newFunctionality           # whenever we call the wish(), it's the nameCheck() that is executed. this is due to the decorator anotation used in the code.
def wish(name):
    print("Good morning ",name)

wish('Shivam')
wish('Abhishek')
wish('Ankit')
wish('Anna') """


""" #Instead of anotation, we can explicitily declare the link


def newFunctionality(wish):
    def nameCheck(name):
        if name == 'Anna':
            print("Bad morning ",name)
        else:
            wish(name)
    return nameCheck

def wish(name):
    print("Good morning ",name)


addedFeature = newFunctionality(wish)  #after declaring this, we can use wish() and addedFeature() separately with and without extended finctionality respectively.

wish('Shivam')
wish('Abhishek')
wish('Ankit')
wish('Anna')            # w/o added functionality 
addedFeature('Anna')    #with added functionality """

# Use case of decorators for checking the denominator value

""" def decor(func):
    def checkDenominator(a,b):
        if b == 0:
            print("b cannot be ",b)
        else:
            func(a,b)
    return checkDenominator

@decor
def division(a,b):
    print("Division of {} and {} is: {}".format(a,b,(a/b)))

division(13,9)
division(13,0) """


# Syntax of using a decorator function -- to understand the control flow when decorator is used

""" def outer(f1):
    print("Inside outer function...")
    def inner():
        print("Inside the inner function...")
        f1()
    print("outer returning the inner function.... ")
    return inner

@outer
def f1():
    print("Inside the f1 function...")

f1()
 """


# Decorators chaining control flow

def outer(f1):
    print("Inside outer function...")
    def inner():
        print("Inside the inner function...")
        f1()
    print("outer returning the inner function.... ")
    return inner

def outer1(f1):
    print("Inside outer 1 function..")
    def inner():
        print("Inside inner of outer1 decor")
        f1()
    print("outer 1 function returing inner function...")
    return inner

@outer1
@outer
def f1():
    print("Inside the f1 function...")

f1()

""" 
**Note: We noticed that the f1() is called only once. When f1() is called, it executes the outer() and then the inner function is returned.
This inner() is not passed as an argument to outer1() and then the inner() of outer1() returns the f1(), due to which the actual f1() is called and executed. """