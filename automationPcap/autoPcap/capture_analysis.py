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

#ip1=os.system("ifconfig -a|grep Bcast|awk -F ':' '{print $2}'|awk '{print $1}'")

output = os.popen("ifconfig -a|grep Bcast|awk -F ':' '{print $2}'|awk '{print $1}'")
ip1=output.read()[:-1]

def pcap_dump():
    try:
        os.system('tcpdump -i eth0 port {0} -w ./pcap/{1}.pcap &'.format(sys.argv[1],sys.argv[2]))

    except IndexError,e:
        if len(sys.argv) < 3:
            print "*"*78
            print '''please input port number and pcap file name
                such as
                python capture_analysis.py [port] [pcapfile]
                python capture_analysis.py 110 pop3_new
'''

            print "*"*78
        sys.exit(1)
    else:
        print "capturing package for port {0} and pcap file will be kept in {1}".format(sys.argv[1],sys.argv[2])


def formattime(t): #日期字段格式化
    return time.strftime('%c',time.gmtime(t+8*3600))

def pcap_analysis():
    sendlen=0
    sendpkt=0
    recpkt=0
    revlen=0
    pc=pcap.pcap()    #注，参数可为网卡名，如eth0
    pc.setfilter('tcp port {0}'.format(sys.argv[1]))   #设置监听过滤器
    if not pc:
        print "pc is null"
        sys.exit(1)

    while True:
        try:
            for ptime,pdata in pc:
                print ptime,len(pdata)
                p=Ethernet(pdata)
                if p.data.__class__.__name__=='IP':
                    srcip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.src)))
                    print "source ip is " + srcip
                    dstip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.dst)))
                    print "dst ip is " + dstip
                    if srcip==ip1:
                        sendlen=sendlen+p.data.len
                        sendpkt=sendpkt+1
                        print '========================================================='
                        print 'time = ',formattime(ptime)
                        print p.data.__class__.__name__
                        print p.data.data.__class__.__name__
                        print '%sPORT:%d------->%s,PORT:%d' %(srcip,p.data.data.sport,dstip,p.data.data.dport)
                        print 'SendPkt:',sendpkt
                        print 'SendLen:',sendlen

                    if dstip==ip1:
                         recpkt=recpkt+1
                         revlen=revlen+p.data.len
                         print '========================================================='
                         print 'time = ',formattime(ptime)
                         print p.data.__class__.__name__
                         print p.data.data.__class__.__name__
                         print '%sPORT:%d<-------%s,PORT:%d' %(dstip,p.data.data.dport,srcip,p.data.data.sport)
                         print 'RecPkt:',recpkt
                         print 'Reclen:',revlen

            print "I'm going to leave now......!"
            break
        except Exception as e:
            #print 'exection: {0}'.format(e)
            pass
        except KeyboardInterrupt, e:
            os.system("ps -ef | grep -v grep|grep tcpdump|awk '{print $2}'| xargs kill -9")

if __name__ == "__main__":
    pcap_dump()
    pcap_analysis()



