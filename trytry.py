# -*- coding: UTF-8 -*-
import os
import sys
import logging
from sys import stdout
oldStdout = None
logfile = None
pp = "C:\\Users\\swang\\Desktop\\pythonfile"

logging.basicConfig(filename='mylog.log', level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d : %(message)s')

def logging_func(info,debug,error,critical):
    logger = logging.getLogger('hello')

    logger.info(info)
    logger.debug(debug)
    logger.error(error)
    logger.critical(critical)

def makefile(pathpath):
    if os.path.isfile(pathpath):
        print ("the file is existed")
    else:
        a=open(pathpath,"w")
        a.write("sdfgsadgadg")
        a.close()
        print "%s is created,very good" % pathpath
        sss = "%s is created,very good" % pathpath
        logging_func(sss,"no bug","no error","no critical")

def programe():
    while pp:
        ff = raw_input("please enter a file to be created,'.' or 'q' for quit:")
        if ff == "susan.txt":
            print "this file can't be created"
            cccc = "this file can't be created"
            logging_func(cccc,"no bug","no error","no critical")
            break
        elif ff == "q":
            print "quit!"
            break
        else:
            print os.getcwd()
            os.chdir(pp)
            print pp
            full=os.path.join(pp,ff)
            print full
            def tryfunc():
                try:
                    makefile(full)
                except IOError,e:
                    print "there is input error and need a file name is provided"
                finally:
                    return
            tryfunc()
programe()







