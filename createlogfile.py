#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
file1='/susan/mylog.log1'
a=open(file1,'r')
for i,j in range(01,12):
	filename='mylog.log2016-%d-%d' % i,j
	b=open(filename,'w')
	b.write(a.read())
	b.close()
