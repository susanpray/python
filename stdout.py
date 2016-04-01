import sys

oldStdout = None
logfile = None
try:
    logfile = open('d:/1.log','w+')
    oldStdout = sys.stdout
    sys.stdout = logfile
    print 'Hello World in File Log!'
finally:
    if logfile:
        logfile.close()
    if oldStdout:
        sys.stdout = oldStdout

print 'Hello World in Screen!'