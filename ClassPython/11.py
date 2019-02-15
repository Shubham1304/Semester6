#Class of 12th Feb 2019

#Functions in python 

def fun():
	'''This fcntion says hello'''
	print ('Hello')

call=fun
fun()
call()
print (fun.__doc__)

''' 
Fun and call are the global frames 
When we use parameter passing in simpple datatypes like integer float string, change in parameter doesn't change the argument




''' 

def fn3(x):
	x+=x
	print (x) #70
a=35
fn3(a)
print (a) #35
print ('-'*20)
sep='+'
print(1,2)  #sep=' ' is the default value of the separator for print function 
#the above output is 1 2 and not 1+2 because we have not passed it as an argument to print function 

print(4,5,sep=sep) 
print (2,3,sep='-')


#reference type : list, set, tuple, dictionary 

def fn4(a):
	#a=[1,2]
	#print(a)
	#a=a+[1,2]  here why the original list was not modified was that because the = creates a new 		#	    list copy in the activation record  
	#= will always create a new list and modify the entire reference	
	#print (a)
	a.append(52)  #modified the entire list reference because 
	print (a)    
l=[3,4]
fn4(l)   #we are passing the list as values and list is a collection of references
#when we pass the list values it behaves like pass by reference because we are passing the  
print(l) 

print(a)

#append adds the elements to the existing list so when we 

def fn5(a):
	print ('fn4',id(a))
	a=a+[1,2]
	print(a,id(a))
	a.append(5)
	print(a,id(a))


l=[3,4]
print ('main:before',l,id(l))
fn5(l)
print ('main:after',l,id(l))


g=[5,6]
print(g,id(g))
g.clear()
print(g,id(g))

g=[]
print(g,id(g))



print ('_'*50)

def fn6(a):
	print ('fn6',id(a))
	a+=[1,2]   #when we use shorthand on a reference data type, it says use the same list and add 			   #it to that only so a+= and a=a+ are different .. a+= momdifies the same a and 			   #update  
	print(a,id(a))
	a.append(5)
	print(a,id(a))


l=[3,4]
print ('main:before',l,id(l))
fn6(l)
print ('main:after',l,id(l))

#when we pass refernee pass to a function and we use any functions on it like append then it will #modify the original data itself. Note - value of refernece data type is a collection of references...
