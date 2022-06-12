import math

#f(x) = ax²+bx+c    delta = b²-4.a.c  bas= (-b+-rot.square(delta))/ 2.a

print("f(x) = ax²+bx+c")

a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))
c = int(input("Enter the value of c\n"))

delta = b*b-4*a*c
print(f"The value of Delta is  {delta}")

bas0 =  (-b+math.sqrt(delta))/(2*a)
print(f"The value of X1 is {bas0}")

bas1 =  (-b-math.sqrt(delta))/(2*a)
print(f"The value of X2 is {bas1}")

yv = (-delta)/4*a
print(f"The value of Yv is {yv}")

xv = -b/2*a
print(f"The value of Xv is {xv}")

if (a > 0):
    print("The parabola opens upwards")
elif a < 0:
    print("The parabola opens downwards")
