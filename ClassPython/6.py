#Class of 5th February 2019


#for loops 


#file handling in python 

#Why do we need files ? Persistence ie file stores the data permanently 
#How to open and create a file in python?

# open : r,w,a
# perform certain operations 
# close the file
#Errors that can be encountered if we dont close the file ? We can not use the file in any other program. Also contents wont be saved 

fh = open ('test2.txt','r')
#file can also be treated as an object so it is stored in some location similarly to how other values are stored in the memory so we need a file object to point to it.
print (fh,type(fh))

line = fh.readline() #one line at a time
print ()
#rstrip function will remove a new line at the end of the file 
#lstrip function will remove a new line at the right of the line ie at the beginning of the line
#line.strip will remove all the new line characters 


while line:
	line = line.strip()
	print(line)
	line = fh.readline() 
#once the line is read the fh pointer is moved to next location 
#then we use readline function to read that line that is pointed out by fh pointer


fg=open('test2.txt','r')
line = fg.readlines() #makes it an iterable #returns as a list with each line as an element of the line

print(line,type(line))
for l in line: 
	print (l.strip())


#read function reads the whole content of file as a string
#line= fh.read().split('\n')

'''This code is 

with open('test2.txt','r') as f: 		#same as f = open('filename.txt','r') but the advantage is that it closes the file automatically when the while loop ends so we dont have to worry about
	line = f.readline().strip()		#closing the file.
	while line:
		line=line.strip()
		if line.startswith('From'):
			print line 


#mbox.txt mboxshort.txt
#www.py4e.com/code/









































								
