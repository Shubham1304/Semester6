#30th January class

import random as r
print(r.random())   #between 0 and 1 random value is generateed

print(r.uniform(1,10))


dice = [1,2,3,4,5,6];
print(r.choice(dice))
print(r.choice([1,2,3,4,5,6]))

print (r.sample(dice,2)) # population and size it takes
 #it will take 2 values from the dice

r.shuffle(dice)
print (dice)
#shufffe modifies the original data itself, does not return any value

#-----------------------------------------Strings begin---------------------------------------------


'''There are three kinds of strings - 1) "" or '' must be in a single line the whole string
because the python interpreter treats the nerw line character as a end of string
'''
#2)d =  ''' this is
#a multiline string '''

d= ''' this
is  a
multi line string'''
print (d)


#3) Documentation string - __doc__ will store the first triple quote string in the programming

print(__doc__)
print (r.seed.__doc__)

#4)Raw String - does not interpret a new kine character

s='abc\ndef'
print (s) # simple string will treat \n as new line character

s=r'abc\ndef'
print(s)

#operations --
#length - len()
#concatenate - +
#replicate - *
#access : indexing - 0 based indexing
'''
_0_1_2_3_4_5_6________
|G|o|o|d|b|y|e|
'''
#slicing -

s='Goodbye'
print(len(s)) #len is a free function - free function is a function which is available to all the
#objects i.e. it can be used for any collection of data


print (s[1:5],s) #slicing
print (s[1:5:2],s) #extended slicing str[start:stop:step]

print(s[5:1:-2],s) #negaitve step
#if the step is not given in the avve exapmle then it will print an empty string


#negative indexing
print(s[-1]) #print(s[len(s)-1])
print ("Hello")
print(s[-1:-5:-1]) #give the reverse string
print(s[::-1]) #reverse the entire string, start as -1 and end as -8
