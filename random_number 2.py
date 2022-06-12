# Open a txt file and write as many random numbers as you want

import random

f = open("random_number.txt", "a+")

x = input("How many numbers do you want?")

for i in range(0,int(x)):
    y = random.randint(-99,99)
    f.write("%a\n" % (y))

f.close()