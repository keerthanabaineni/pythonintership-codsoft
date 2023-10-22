TASK-2
import math as m
def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x):
    return x**x
def squareroot(n):
    return m.sqrt(n)
def log(x):
    return m.log(x)
def sin(x):
    return m.sin(x)
def cos(x):
    return m.cos(x)
def tan(x):
    return m.tan(x)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power")
print("6.sqareroot")
print("7.logarithm")
print("trignometric values")
print("8.sinvalue,9.cosvalue,10.tanvalue")

while True:
     choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    # check if choice is one of the four option
     if choice in ('1', '2', '3', '4' ,'5','6','7','8','9','10'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            n=float(input(" enter the value"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice =='5':
            print( n," pow",power(n))
        elif  choice ==' 6':
            print( n," squareroot of",squareroot(n))
        elif  choice ==' 7':
            print( n," logarithm of",m.log(n))
        elif  choice =='8':
            print( n," sin value of",m.sin(n))
        elif  choice =='9':
            print( n," cos value of",m.cos(n))
        elif choice == '10':
            print(n, " tan value of", m.tan(n))
        
     else:
        print("Invalid Input")
