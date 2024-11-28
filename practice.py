# DAY 1

print("Hello, World!")


# DAY 2
#  Example of variables
age = 10      
height = 4.5  
name = "Tom"  
is_student = True 

print(age, height, name, is_student)

# Example of a constant
PI = 3.14
GRAVITY = 9.8
print("Value of PI:", PI)
print("Value of Gravity:", GRAVITY)


# Python data types
# 1 
age = 15
print(age)

# 2
price = 19.99
print(price)

# 3
name = "Alice"
print(name)

# 3
is_sunny = False
print(is_sunny)


# finding data types
# 1
age = 20
print(type(age)) 

# 2
num = "25"  
num = int(num)  
print(num, type(num))

# 3
name = input("Enter your name: ")
print("Hello, " + name + "!")

# 4
age = 10
print("You are", age, "years old.")

# 5
result = 2 + 3 * 4  
print("Result:", result)

# 6
result = 5 ** 2 ** 3  
print("Result:", result)


# Addition of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
marks = int(input("Enter your marks: "))


if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 3 or 5.")


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")






