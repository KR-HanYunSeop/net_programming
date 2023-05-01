import socket
import struct
import binascii

class Udphdr:
    def __init__(self, SrcPort, DPort, ULength, Cheksum):
            self.SrcPort = SrcPort
            self.DPort = DPort
            self.ULength = ULength
            self.Checksum = Cheksum
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.SrcPort)
        packed += struct.pack('!H', self.DPort)
        packed += struct.pack('!H', self.ULength)
        packed += struct.pack('!H', self.Checksum)
        return packed
#—————————————————————————        
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:16]) 
    return unpacked

def getScrPort():
    return unpack_Udphdr[0]
def getDstPort():
    return unpack_Udphdr[1]
def getLength(unapcked_udphdr):
    return unpack_Udphdr[2]
def getChecksum():
    return unpack_Udphdr[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udp = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udp))
unpacked_udp = unpack_Udphdr(packed_udp)
print(unpacked_udp)