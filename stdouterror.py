import sys
logfile = open('d:/3.log','w+')
oldStdout = sys.stdout
print 'Hello World in File Log!'
print 'Being processed...'
print 'End of program'
sys.stdout = logfile
sys.stdout = oldStdout
logfile.close()