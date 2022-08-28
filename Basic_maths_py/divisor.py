
# A Better (than Naive) Solution to find all divisors
import math
 
# method to print the divisors
def printDivisors(n) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                print (i,end=" ")
            else :
                # Otherwise print both
                print (i , int(n/i), end=" ")
        i = i + 1
 
# Driver method
print ("The divisors of 100 are: ")
printDivisors(100)
 
#This code is contributed by Nikita Tiwari.