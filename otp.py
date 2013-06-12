#Python one-time pad encryption module
from zlib import crc32
from struct import unpack,pack



file_num = 0
offset = 0



class Otp_manager:

    def loadpads(self,cid):
        f = open("./otp/" + cid + "/in.0","rb")
        o = open("./otp/" + cid + "/in.0","rb")
        self.in_contents = f.read()
        self.out_contents = o.read()
        f.close()
        o.close()
    
    def __init__(self,contact_id):
        functional = False
        self.in_file_list = {}
        self.in_file_active = 0
        self.in_contents = b""
        self.in_offset = 0
        self.out_file_list = {}
        self.out_file_active = 0
        self.out_contents = b""
        self.out_offset = 0
        self.loadpads("0")

    

    def encrypt(self,ba_str,usechecksum = True):
        cs = 0
        el = bytearray()
        for a in range(0,len(ba_str)):
            el.append(ba_str[a] ^ self.out_contents[a+self.out_offset])

        self.out_offset = self.out_offset + len(ba_str)

        
        xorlong = unpack(">L",self.out_contents[self.out_offset:self.out_offset+4])
        cs = (crc32(ba_str) ^ xorlong[0])        
        self.out_offset = self.out_offset + 4

        return (pack(">BQL",0,self.out_offset,cs),el)

    def decrypt(self,ba_str,crc = 0):
        d_str = bytearray()
        for a in ba_str:
            d_str.append(a ^ self.in_contents[self.in_offset])
            self.in_offset = self.in_offset + 1
        return d_str

   # def encrypt(self,ba_str,usechecksum = True):
    #    pass







a = bytearray("Test1234",'UTF-8')
b = bytearray("1234Test",'UTF-8')



s = Otp_manager(255)
a = (s.encrypt(bytearray("Gobshite","UTF-8")))
print(s.decrypt(a[1]))

#
