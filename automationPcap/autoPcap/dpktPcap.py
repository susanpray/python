#!/usr/bin/env python
import dpkt
import sys
f = file(sys.argv[1])
pcap = dpkt.pcap.Reader(f)
for ts,buf in pcap:
	eth = dpkt.ethernet.Ethernet(buf)
	print type(eth)
	print dir(eth)
