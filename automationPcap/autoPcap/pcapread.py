
import scapy
from scapy.all import *

from scapy.utils import PcapReader, PcapWriter
import gzip,zlib,cPickle

class PicklablePacket:
    '''
    A container for scapy packets that can be pickled
    (in contrast to scapy pakcets themselves)
    '''
    def __init__(self, pkt):
        self.contents = str(pkt)
        self.time = pkt.time
    def __call__(self):
        '''
        Get the original scapy packet
        '''
        pkt = scapy.layers.l2.Ether(self.contents)
        pkt.time = self.time
        return pkt
    def dumps(self):
        '''use cpickle to dump'''
        return gzip.zlib.compress(cPickle.dumps(self)).encode('base64')
    @staticmethod
    def loads(string):
        '''
        load object from string
        ''' 
        p = cPickle.loads(gzip.zlib.decompress(string.decode('base64')))
        return p()


        

def read(file_name, start, count):
    '''
    read packets from pcap according to the start packet number and total count 
    '''
    reader = PcapReader(file_name)
    if start > 0:
        reader.read_all(start)
    if count > 0:
        return reader.read_all(count)
    else:
        return reader.read_all(-1)

def write(file_name, packets):
    writer = PcapWriter(file_name, append = True)
    for p in packets:
        writer.write(p)
    writer.flush()
    writer.close()

if __name__ == '__main__':
    packets = read('pdf.pcap', 0, 10)
    # packle the packets to transfer
    p = PicklablePacket(packets[0])
    s =  p.dumps()
    p = PicklablePacket.loads(s)
    print p
    print p.summary()
    
    serialized_packets = [PicklablePacket(p).dumps() for p in packets]
    deserialized_packets = [PicklablePacket.loads(s) for s in serialized_packets]
    write('new.pcap', packets)
