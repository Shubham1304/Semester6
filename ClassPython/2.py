#29th January class
#Operators continued
import sys
import os

print (10 in [20,[10,30],40])
#false because 10 is not a separate element. It is as a pair with 30

print ([10,30] in [20,[10,30],40])
#true
a=1
b=1.0
print(1==1.0)
#true because binary value is same of both

print(id(sys.getsizeof(1)),sys.getsizeof(1))

print(id(sys.getsizeof(1.0)),sys.getsizeof(1))

#identity operators are used to match the id of the values
print (a is b) #false because the id is not the dame and identity operators will not check the values but
print (a==b) #true it only checks the value not the id
#the identity of the variables

a=b=1
print (a is b)
#true because now the id of both the variables is same



#short circuit evaluation - means that interpreter stops evaluating the expression as soon as it
#guesses the answer, in case of logical operators
#employs the lazy programming techniques
print (5>2 or 20/0)
#this is true because as soon as it sees 5>2 is true it terminates

#------------------------------------operators end------------------------------------------------------------

'''
Assignment 1 - WAP to swap two numbers using bitwise Operators
a=a^b
b=a^b
a=a^b
'''
#-------------------------------------------------------------------------------------------------------------
import random as r
#dir(random)
print(r.randrange(1,7))
print(r.randrange(10)) #atleast one parameter should be there which is treated as the stip value
# and the start value is 0 by default
#(start,stop,step) - start is inclusive stop is exclusive and interval/step is for multiples
##help (r.seed())
r.seed(2) #if we want our random numbers to be generated in a particular sequence we use
# seed, used in many ml algorithms, makes it predictable
print (r.randrange(1,10))

r.seed() #this resets the seed value
