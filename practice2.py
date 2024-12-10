# for loop
i = 1
n = 10
for x in range(i, n + 1):  
    if x % 2 == 0 and x % 3 == 0: 
        print(x)

    else:
        print("This number is not divisible by any 2 or 3") 

# prob 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# prob 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# prob 3
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python")) 

# prob 4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  

# prob 5
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(prime_numbers_in_range(10, 20))  
