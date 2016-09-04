import subprocess, sys, os
f = open('PIDOutput.txt', 'r+')
lines=f.readlines()
target = open('pythonOutput.txt', 'w')
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
for i in range(5,50):
	if(lines[i] == "\n"):
		break
	if(hasNumbers(str(lines[i])) == True):
		target.write(lines[i])	
target.close()
g = open('pythonOutput.txt', 'r')
lines=g.readlines()
array = []
count = 0
for i in lines:
	tmp = ""
	for char in lines[count]:
		if(char.isdigit()):
			tmp += str(char)
	array.append(tmp)
	count +=1
call = "kill "
length = len(array)
for x in range(length):
	call += str(array[x]) + " "
call += "> /dev/null 2>&1"
os.system(call)
# Close the file
f.close()
