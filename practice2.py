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
