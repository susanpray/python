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
running=1
#遍历文件夹，指明被遍历的文件夹
def formattime(t): #日期字段格式化
    return time.strftime('%c',time.gmtime(t+8*3600))
def cleardate():
    sendlen=0
    sendpkt=0
    recpkt=0
    revlen=0
    times=0

def pcap_analysis(filepath,running):
    cleardate()
    sessionnum=0
    pc = pcap.pcap(filepath,0,0,False)
    sendlen=0
    sendpkt=0
    recpkt=0
    revlen=0
    times=0
    sessionnum=1
    sendflag=0
    revflag=0

    if not pc:
        print "pc is null"
        sys.exit(1)

    while running==1:
        try:
            for ptime,pdata in pc:
                #print ptime,len(pdata)
                p=Ethernet(pdata)
                if p.data.__class__.__name__=='IP':
                    if p.data.data.flags==2:
                       ip1='%d.%d.%d.%d'%tuple(map(ord,list(p.data.src)))#取出第一个包的srcip

                    dstip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.dst)))
                    srcip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.src)))
                    if srcip==ip1:
                      sendlen=sendlen+p.data.len
                      sendpkt=sendpkt+1
                      print 'SendPkt:',sendpkt
                      print 'SendLen:',sendlen

                      if p.data.data.flags==17:#flag=17 是Fin 加 ack包，证明服务器端已经发送了fin请求，而客户端已经接受了，是属于倒数第二个包
                         sendflag=sendflag+1             #将flag置为1，表示再收到一个ack包，就彻底结束
                      if p.data.data.flags==16 and revflag==1:#接受方的flag=1表示应答最后一个fin ack的包，是最后一个包
                         revflag=revflag+1

                    ###############################################################################################
                    if dstip==ip1:
                      recpkt=recpkt+1
                      revlen=revlen+p.data.len#累加
                      print 'RecPkt:',recpkt
                      print 'Reclen:',revlen

                      if p.data.data.flags==16 and sendflag==1:#接受方的flag=1表示应答最后一个fin ack的包，是最后一个包
                       sendflag=sendflag+1

                      if p.data.data.flags==17:#flag=17 是Fin 加 ack包，证明服务器端已经发送了fin请求，而客户端已经接受了，是属于倒数第二个包
                         revflag=revflag+1

                if pc=='':
                    print '88'
                if sendflag==2 and revflag==2:
                    print '========================================================='#这个时候发送已经结束，可以打印信息
                    print 'The file path is',filepath
                    print 'time = ',formattime(ptime)
                    print p.data.__class__.__name__
                    print p.data.data.__class__.__name__
                    print '%sPORT:%d------->%s,PORT:%d' %(srcip,p.data.data.sport,dstip,p.data.data.dport)
                    print 'Total SendPkt:',sendpkt
                    print 'Total SendLen:',sendlen
                    print '%sPORT:%d<-------%s,PORT:%d' %(dstip,p.data.data.dport,srcip,p.data.data.sport)
                    print 'Total RecPkt:',recpkt
                    print 'Total Reclen:',revlen
                    recpkt=0,
                    revlen=0
                    sendpkt=0
                    sendlen=0
                    running=0
                    break
                break
        except Exception as e:
            pass
        except KeyboardInterrupt, e:
            os.system("ps -ef | grep -v grep|grep tcpdump|awk '{print $2}'| xargs kill -9")


if __name__ == "__main__":
    running=1
    pcap_analysis(sys.argv[1],running)




