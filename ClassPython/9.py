#Class of 9th Feb 2019

#Note that in python3 the sys.exit works only if the statement is in the main lock other wise it will #not work. 

#if try executes then go to try and if try doesnot execute then go to except part so else is like a selective finally part

try:
	print("Inside try")
except:
	print ("Inside except")
else:
	print ("Inside else")

#Now if try executes only then else part will be executed and if error in try else will not be executed 

#List opertions 

a=10
b=10
print(id(a),id(b))
l=[1,2,3]
f=[1,2,3]
print (l is f)
'''
#in list there will be three continuous blocks of memory 
l -> 	| | | |
		 
	|1| |2| |3|
Object 1 cannot be stored directly into the list , 1 will always be an integer so reference is given to set of objects in the list 
both the lists have their own ids 
id of the list is the id of the reference collection and not of the interger value it holds 

'''
print (id(l),id(f))
print (id(l[0]),id(f[0]))

z=1
print(id(z))


h=list()
print(type(h))
h=('abc') #this string is an iterable because it can be used in for loop as iterable 
print (h,type(h))

h=list('abc')
print (h,type(h))

h=[]
print(type(h))
#to add values to the end of the list, we use h.append()
h.append(3)
h.append(1)
print (h) #[3,1]
h.insert(4,5) 	#it automatically corrects the index value to the last index of the arrau 
#so though 4 is not an index in h yet it wont throw error 
#[3,1,5]

h.insert (1,7)
#[3,7,1,5]  -  output
h.extend([4,5,6])
#it exends your list and adds individual values to the list whereas append just simply appends

h[1]=3
print (h)

h.pop()
#last element deleted 

h.pop (3)
#return the deleted element which was at position 3
print(h)
h.remove(3)
#will remove the first occurence of the  number in the braces 

print (h)

h.clear()
print (h)
#empty the list 

a=[]
a=[1,2,3]
print (id(a))
a.clear()
print (a)
print (id(a))

#emptying the list is done by using clear function in order to keep the id of the list equal.

h.reverse() #just reverse the list, do not sorts the list 
print (h)
h.sort(reverse=True)
print (h)

b = ['james','mary','alex']
b.sort()
print(b)
#b.sort(key=1)
print(b)
print(b[1::])

#assignment always creates a new reference 
l=[1,[2,3],4]
print (l)


#shallow copy and deep copy 










































