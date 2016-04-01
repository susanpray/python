from filelinelen import filelen
import os
file1 = 'mylog.log'
logopen = open(file1,"r")
file2 = 'mylog.lognew'
newopen = open(file2,"w")
lines = logopen.readlines()
date = '2016-03-18'
print file1 , "'s lines is :" , filelen(file1)

for line in lines:
    if "ERROR" in line:
        newopen.write(line)
#print newopen.readlines()

newopen.close()
logopen.close()

os.remove(file1)
os.rename(file2,file1)
print file1 , "'s lines is :" , filelen(file1)



