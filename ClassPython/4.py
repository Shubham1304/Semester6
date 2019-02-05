#31st January class

#string operations

s='hello'
print (s.index('o')) #exception if not found

#s.find('a') return -1 if not found

#------------------check valid name-------------------------------------------------------------------------------------
s=''
s=input("Enter the string")
if(s.isalpha()):
	print ("Valid name")
else :
	print ("Not a valid name")



#--------------------check a palindrome----------------------------------------------------------------------------------
s=input ("Enter a number")
r=s[::-1]
if r==s:
	print ("It is a palindrome")
else:
	print("It is not a palindrome")


s='abba'
print (s.index('a'))

s = input ("Enter the string")
	
while i<len(s):
	if (s.isdigit()):
		if(
	
