n = input("Number of rows:")
def printPascal(n) :
     
    # Iterate through every line
    # and print entries in it
    for line in range(0, n) :
         
        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                " ", end = "")
        print()
     
 
# https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/ 
# for details about this function
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res
 
printPascal(int(n))
 
 
# This code was based on a code made by Nikita Tiwari