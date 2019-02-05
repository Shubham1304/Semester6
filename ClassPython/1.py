#28th January class
#operators
import os


print ("hey!")

#Operators
#arithmetic Operators : + - * / ** (this is power)

s = 2**3**2 #R to L associativity
print (s,type(s))

# + is polymorphic means have different meanings when we use differently

s=2.3+4
print (s,type(s))
 # s=1+'2'  this is an error because both operands of + should be same if different they should be numeric
s='1'+'2'
print (s,type(s))

s=[3,4,5] + [5,6,7]   #list
print (s,type(s))
# list are mutable that is they can grow or shrink in size whereas tuples is immutable
s=(3,4,5) + (5,6,7)   #this is tuple
print (s,type(s))

#this concatenation gives us indexes from 0 to 5

#we can't concatenate two dictionaries because in list and tuole we trust interpreter to provide indexing
#but in dictionaries we index ourself and dont trust interpreter to index
#hence dictionaries can not be concatenated
'''
this is an error because of the explanation given above
s= {1:'a',2:'b'} + {1:'c',2:'d'}
print (s,type(s))
'''
s= {1:'a',2:'b'}
print (s,type(s))

#this will replicate the string the number of times it is mentioned in the expression
s= 3 * '4'
print (s,type(s))

s= 3 * [1,2,3]
print (s,type(s))


#can not use * on dictionaries because keys cannot be replicated
#string behaves as primitive character and as a collection of character as well

# / - true division will always give you float answer
# // - integer, truncation or floor division, return data type based on the data types of operands - the higher
# one is the final data type for ex 5//2.0 will first perform floor division i.e. 2 and then convert it into
# float i.e. 2.0

s=5/2
print (s)

s=5//2
print (s)

s=5//2.0
print (s)

''' the round of function is ambiguous near .5  so the bankers rule in applied according to which the
value to the closest even number is rounded off
for ex - round(2.5) will return 2
round(3.5) will return 4... above and below will be treated as treated in maths
'''

num = int (input ("enter the value"))


sum =(num%10) + (num//100) + ((num%100)//10)

print (sum)

'''
Bitwise operantors


& and
| or
^ xor
left shift and right shift
<<
>>
~ n = -(n+1)
'''


a=3
b=4
c=1
print (a>b>c)
print (a>b and b>c)

l= [1,2,3]
print ([1,2] in l) #outputs false because it treats it as an independent value and matches

print (1 in l)  #true


#Assignment 1- Implement caesar cipher to circle back xyz to abc
#Assignment 2- Swap two numbers using bitwise operators



# and, or, not are used as the logical operators and not the symbols && and all
