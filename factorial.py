import math

#factorial is n!=n*(n-1)*(n-2)....3.4.5

n = int(input("Enter de value of n\n"))

y = n 

if n == 0:
    print("The value of n is 1")
elif n < 0:
    print("Sorry, there is no factorial for negative numbers")
else:
    while y > 1:
        y = y -1
        n = n * y
    print(f"The value of n is {n}")
    