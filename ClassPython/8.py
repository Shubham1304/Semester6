#Class of 7th Feb

#File reading and writing operations
import sys
'''f = open ('test.txt','r')

lines = f.readlines()
print(lines)
s=['a\n',	'b\n','c\n']
fw = open('test2.txt','w')
fw.writelines(s)


print (fw.tell())  #tells the position of the file pointer 
fw.seek(6)
print (fw.tell())

s = ['aaa','bbb','222']


#Exception handling 

#If nothing is mentioned in the exception class then base class as exception class 

try:
	f = open ('x.txt','r')
except Exception as e:
	print ('No file',e)

---------------------------------check this code------------------------------------------------------
#e will return the __doc__ of the exception class
try:
	f = open ('x.txt','r')
except FileNotFoundError:
	print ('Exception')
	#sys.exit()
	exit(0)
except Exception as e:
	print ('No file')
	#sys.exit()
	exit(0)
finally :
	f.close()

	
'''



#Print first 20 fibonacci numbers

s = {}
s[0]=0
s[1]=1
for i in range (2,20):
	s[i]=int (s[i-1])+int(s[i-2]);	
for i in range (20):
	print (int(s[i]))


















