# Program to try to simulate the generation of car plates number

import random
import string

# The pattern of plate in Brazil ABC1D23

f = open("plates.csv", "a")

a = random.choice(string.ascii_uppercase) #generante a random letter in uppercase
b = random.choice(string.ascii_uppercase)
c = random.choice(string.ascii_uppercase)
d = random.choice(string.ascii_uppercase)

w = random.randint(0,9) #random.randint(a, b) generante a number a <= N <= b
y = random.randint(0,9)
z = random.randint(0,9)

final_plate = a + b + c + str(w) + d + str(y) + str(z) #I'm defining a number (w, y, z) as a string
#python can only concatenate string with string, int with int, etc...

#write the numbers in a csv file
f.write(f"{final_plate}\n")