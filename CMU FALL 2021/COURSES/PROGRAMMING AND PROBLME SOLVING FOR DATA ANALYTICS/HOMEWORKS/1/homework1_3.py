"""
Author: Jean Paul Nishimirwe
Andrew Id: jnishimi
Date created: On 14th Sept 2021

About a program
---------------
A program is all about solving a quadratic equation.
A program uses two libraries:
    math: useful while finding square root of numbers and power of numbers
    cmath: Useful while working with complex numbers
A program uses 3 functions: 
    read_coefficient(): That prompts user to enter coefficients (a,b,c) and returns a tuple of them (a,b,c)
    
    compute_roots(t): That takes a tuple parameter resulted from read_coefficient()
                      Calculate roots of the equation (x1,x2)
                      returns a tuple of roots (x1,x2)
                      
    main() : That calls read_coefficient(), compute_roots(t) and print the results(x1,x2) as returned by compute_roots(t) function
"""
import math
import cmath
def read_coefficient():
    a=float(input("Enter a: ")) # Enter coefficient a
    b=float(input("Enter b: ")) # Enter coefficient b
    c=float(input("Enter c: ")) # Enter coefficient c
    r=tuple(int(i) for i in [a,b,c]) 
    return r # Return a tuple of read values(coefficients)

def compute_roots(t):
    a,b,c=t[0],t[1],t[2] # Extract a,b,c from passed tuple
    delta=(math.pow(b,2) - (4*a*c)) # computing delta
    if delta >= 0:
        numerator1=((-b)+math.sqrt(delta)) # numerator for root1
        numerator2=((-b)-math.sqrt(delta)) # numerator for root2
        denominator=2*a # denominator for both root1 and root2
        x1=numerator1/denominator # compute root1
        x2=numerator2/denominator # compute root2
        return (x1,x2) # returning an tuple of roots

    # if delta < 0
    x1=((-b)+cmath.sqrt(delta))/(2*a) # formatting the way I want to 

    x2=((-b)-cmath.sqrt(delta))/(2*a) # use cmath library to store a value in form of complex number
    #format my complex root value
    return (x1,x2) # return two complex roots
        
    

def main():
    t=read_coefficient() # reading coefficients and assign their tuple to t
    print(f"Roots: {compute_roots(t)}") # computing both roots and show them on the screen
    
if __name__=='__main__':
    main() # Calling a function to do our job