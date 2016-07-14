#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pcap
import dpkt
from dpkt.ip import IP
from dpkt.tcp import TCP
from dpkt.udp import UDP
from dpkt.http import *
from dpkt.ethernet import Ethernet
import sys
import os
import os.path
import re


# 遍历文件夹，指明被遍历的文件夹
def formattime(t):  # 日期字段格式化
    return time.strftime('%c', time.gmtime(t + 8 * 3600))


def cleardate():
    sendlen = 0
    sendpkt = 0
    recpkt = 0
    revlen = 0
    times = 0


def pcap_analysis(filepath):
    cleardate()
    sessionnum = 0
    pc = pcap.pcap(filepath, 0, 0, False)
    sendlen = 0
    sendpkt = 0
    recpkt = 0
    revlen = 0
    times = 0
    sessionnum = 1
    sendflag = 0
    revflag = 0
    i=0
    d1 = {}
    d2 ={}
    d3={}
    d4={}
    i=0


    if not pc:
        print "pc is null"
        sys.exit(1)

    try:
        for ptime, pdata in pc:
            # print ptime,len(pdata)
            p = Ethernet(pdata)
            if p.data.__class__.__name__ == 'IP':
                i=i+1
                print 'i:',i
                if p.data.data.flags == 2:
                    ip1 = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src))) # 取出第一个包的srcip
                    print ip1
                    print '@@@@@@@@@@@@@@@@@'
                    sp = p.data.data.sport#sp会变化
                    dp=  p.data.data.sport
                    print d1
                    d1[sp]=0
                    d2[sp]=0
                    d3[sp]=0
                    d4[sp]=0
            dp = p.data.data.dport
            dstip = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
            srcip = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
            sprot=p.data.data.sport
            dport=p.data.data.dport
            print srcip
            if srcip==ip1:


                      d1[sprot]=d1[sprot]+1
                      d2[sprot]=d2[sprot]+p.data.len
                      print 'd1:',d1
            if dstip==ip1 :

                      d3[dport]=d3[dport]+1
                      d4[dport]=d4[dport]+p.data.len
                      print 'd3:',d3



    except Exception as e:
        # print 'exection: {0}'.format(e)
        pass

    #print '====================This result of packet====================================='  # 这个时候发送已经结束，可以打印信息

    #print 'The send pkt of port:',d1
    #print 'The send len of port:',d2
    #print 'The send pkt of port:',d3
    #print 'The send len of port:',d4

    print '====================This result of Es====================================='
    for k in d1.keys():
     print k
     print '$$$$$$$$$$$$$$$$$'
     print 'The send pkt of port:',k,d1[k]
     print 'The send data of port:',k,d2[k]
     print 'The recv data of port:',k,d3[k]
     print 'The recv data of port:',k,d4[k]
     GetEs_result(k,dp)



def  GetEs_output(sport,dprot):
    output = os.popen('bash flow_search.sh'+' '+bytes(sport) +' '+bytes(dprot))
    text=output.read()
    output.close()
    return text

# write "data" to file-filename
def WriteEs_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()

def GetEs_result(sport,dprot):
    WriteEs_file('com',GetEs_output(sport,dprot))
    #pat2 = "sendpacket[\. ]+: (^[1-9]\d*$)"
    sendpacket='"sendpacket":([0-9]*)'
    receiveoctet='receiveoctet":([0-9]*)'
    receivepacket='receivepacket":([0-9]*)'
    sendoctet='sendoctet":([0-9]*)'
    Es_Senpkt= re.findall(sendpacket, GetEs_output(sport,dprot))[0]
    Es_Senlen=re.findall(sendoctet, GetEs_output(sport,dprot))[0]
    Es_RecPkt=re.findall(receivepacket, GetEs_output(sport,dprot))[0]
    Es_RecLen=re.findall(receiveoctet, GetEs_output(sport,dprot))[0] #正则比对找出结果

    print'The Es SenPkt:',Es_Senpkt
    print'The Es SenLen:',Es_Senlen
    print'The Es RecPkt:',Es_RecPkt
    print'The Es RecLen:',Es_RecLen




if __name__ == "__main__":
    pcap_analysis(sys.argv[1])