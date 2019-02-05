#Class of 4th February 


#while-else loop

while i<n//2:
	if n%i==0
		print ("not prime")
		break 
	i+=1
else:
	print ("prime")

''' While has to naturally terminate in order to execute else part for ex in abbove case because of break the else will not be executed if the break statement is encountered '''

# while and else are both same commands i.e. they are compound statements 



#for loop concepts

''' in c and java both for and while are isomorphic, i.e. they can be interchanged for loops areuse  th enumber of iterations are always fixed in for loops. iterable is a collection of values 
which are physically or conceptuallly in order string is conceptually organized in memory 
ecah of them is a collection of characters, lists are physically organized 
for <target_var> in <iterablee>:
	<suite>

each time for executes it is going to extract the value
i does not point to it but the value of the iterable is copied in the i iterabel sends a signal to for thsat there are no values to caopy oin so for naturally exits form the loop

l=[1,2,3]
for i in l:
	print (i)

'''

for i in 'hello':
	print(i)

#why is it not required to have a variable = 'hello' and then for i in variable : ? Because we are only accessing the memory location and not the variable 

num = input("Enter a 3 digit number")
s=0 
#list tuples strings dictionaries can be used as iterables in for loop 

for a in num :
	s+=int(a)
print (s)
'''range is a lazy function in python ie it doenot print the value but stores it in there. In python2 range was eager function ie it printed the value as soon as you enter the command
range(start,stop ,range)
''' 
n = input ("Enter the limit")
for i in range(n):
	print n

list(range(5,1,-1))

#range is and iterable function so we can pass the range function directly to for and it will give you hte values after extracting

#print does not extracts value but list extracts value individually 
s='abcd'
print (s)   #will print abcd 
print (list(s)) #will print ['a','b','c','d']







































