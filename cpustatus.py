#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,time
time2sleep = 2.5
while True:
        print int(time.time()),
        print os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2]
        time.sleep(time2sleep)
