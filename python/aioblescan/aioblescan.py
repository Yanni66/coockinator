#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket, asyncio, sys
from struct import pack, unpack, calcsize
import subprocess


HCI_COMMAND = 0x01
HCI_ACL_DATA = 0x02
HCI_SCO_DATA = 0x03
HCI_EVENT = 0x04
HCI_VENDOR = 0x05

PRINT_INDENT="    "

CMD_SCAN_REQUEST = 0x200c

MY_UUID = b'\x90\x6e\xd6\xab\x67\x85\x4e\xab\x98\x47\xbf\x98\x89\xc0\x98\xae'

class MACAddr:

    def __init__(self,name,mac="00:00:00:00:00:00"):
        self.name = name
        self.val=mac.lower()

    def encode (self):

        return int(self.val.replace(":",""),16).to_bytes(6,"little")

    def decode(self,data):

        self.val=':'.join("%02x" % x for x in reversed(data[:6]))
        return data[6:]

    def __len__(self):
        return 6

    def show(self,depth=0):
        return

class Bool:

    def __init__(self,name,val=True):
        self.name=name
        self.val=val

    def encode (self):
        val=(self.val and b'\x01') or b'\x00'
        return val

    def decode(self,data):
        self.val= data[:1]==b"\x01"
        return data[1:]

    def __len__(self):
        return 1

    def show(self,depth=0):
        return

class Byte:

    def __init__(self,name,val=0):
        self.name=name
        self.val=val

    def encode (self):
        val=pack("<c",self.val)
        return val

    def decode(self,data):
        self.val= unpack("<c",data[:1])[0]
        return data[1:]

    def __len__(self):
        return 1

    def show(self,depth=0):
        return

class EnumByte:

    def __init__(self,name,val=0,loval={0:"Undef"}):
        self.name=name
        self.val=val
        self.loval=loval

    def encode (self):
        val=pack(">B",self.val)
        return val

    def decode(self,data):
        self.val= unpack(">B",data[:1])[0]
        return data[1:]

    @property
    def strval(self):
        if self.val in self.loval:
            return self.loval[self.val]
        else:
            return str(self.val)

    def __len__(self):
        return 1

    def show(self,depth=0):
        return

class BitFieldByte:

    def __init__(self,name,val=0,loval=["Undef"]*8):
        self.name=name
        self._val=val
        self.loval=loval

    def encode (self):
        val=pack(">B",self._val)
        return val

    def decode(self,data):
        self._val= unpack(">B",data[:1])[0]
        return data[1:]

    def __len__(self):
        return 1

    @property
    def val(self):
        resu={}
        for x in self.loval:
            if x not in ["Undef","Reserv"]:
                resu[x]=(self._val & mybit)>0
        return resu

    def show(self,depth=0):
        return

class IntByte:

    def __init__(self,name,val=0):
        self.name=name
        self.val=val

    def encode (self):
        val=pack(">b",self.val)
        return val

    def decode(self,data):
        self.val= unpack(">b",data[:1])[0]
        return data[1:]

    def __len__(self):
        return 1

    def show(self,depth=0):
        return

class UIntByte:

    def __init__(self,name,val=0):
        self.name=name
        self.val=val

    def encode (self):
        val=pack(">B",self.val)
        return val

    def decode(self,data):
        self.val= unpack(">B",data[:1])[0]
        return data[1:]

    def __len__(self):
        return 1

    def show(self,depth=0):
        return

class ShortInt:

    def __init__(self,name,val=0,endian="big"):
        self.name=name
        self.val=val
        self.endian = endian

    def encode (self):
        if self.endian == "big":
            val=pack(">h",self.val)
        else:
            val=pack("<h",self.val)
        return val

    def decode(self,data):
        if self.endian == "big":
            self.val= unpack(">h",data[:2])[0]
        else:
            self.val= unpack("<h",data[:2])[0]
        return data[2:]

    def __len__(self):
        return 2

    def show(self,depth=0):
        return

class UShortInt:

    def __init__(self,name,val=0,endian="big"):
        self.name=name
        self.val=val
        self.endian = endian

    def encode (self):
        if self.endian == "big":
            val=pack(">H",self.val)
        else:
            val=pack("<H",self.val)
        return val

    def decode(self,data):
        if self.endian == "big":
            self.val= unpack(">H",data[:2])[0]
        else:
            self.val= unpack("<H",data[:2])[0]
        return data[2:]

    def __len__(self):
        return 2

    def show(self,depth=0):
        return

class LongInt:

    def __init__(self,name,val=0,endian="big"):
        self.name=name
        self.val=val
        self.endian = endian

    def encode (self):
        if self.endian == "big":
            val=pack(">l",self.val)
        else:
            val=pack("<l",self.val)
        return val

    def decode(self,data):
        if self.endian == "big":
            self.val= unpack(">l",data[:4])[0]
        else:
            self.val= unpack("<l",data[:4])[0]
        return data[4:]

    def __len__(self):
        return 4

    def show(self,depth=0):
        return

class ULongInt:

    def __init__(self,name,val=0,endian="big"):
        self.name=name
        self.val=val
        self.endian = endian

    def encode (self):
        if self.endian == "big":
            val=pack(">L",self.val)
        else:
            val=pack("<L",self.val)
        return val

    def decode(self,data):
        if self.endian == "big":
            self.val= unpack(">L",data[:4])[0]
        else:
            self.val= unpack("<L",data[:4])[0]
        return data[4:]

    def __len__(self):
        return 4

    def show(self,depth=0):
        return

class OgfOcf:

    def __init__(self,name,ogf=b"\x00",ocf=b"\x00"):
        self.name=name
        self.ogf= ogf
        self.ocf= ocf

    def encode (self):
        val=pack("<H",(ord(self.ogf) << 10) | ord(self.ocf))
        return val

    def decode(self,data):
        val = unpack("<H",data[:len(self)])[0]
        self.ogf =val>>10
        self.ocf = int(val - (self.ogf<<10)).to_bytes(1,"big")
        self.ogf = int(self.ogf).to_bytes(1,"big")
        return data[len(self):]

    def __len__(self):
        return calcsize("<H")

    def show(self,depth=0):
        return

class Itself:

    def __init__(self,name):
        self.name=name
        self.val=b""

    def encode(self):
        val=pack(">%ds"%len(self.val),self.val)
        return val

    def decode(self,data):
        self.val=unpack(">%ds"%len(data),data)[0]
        return b""

    def __len__(self):
        return len(self.val)

    def show(self,depth=0):
        return

class String:

    def __init__(self,name):
        self.name=name
        self.val=""

    def encode(self):
        if isinstance(self.val,str):
            self.val = self.val.encode()
        val=pack(">%ds"%len(self.val),self.val)
        return val

    def decode(self,data):
        self.val=data
        return b""

    def __len__(self):
        return len(self.val)

    def show(self,depth=0):
        return


class NBytes:

    def __init__(self,name,length=2):
        self.name=name
        self.length=length
        self.val=b""

    def encode(self):
        val=pack(">%ds"%len(self.length),self.val)
        return val

    def decode(self,data):
        self.val=unpack(">%ds"%self.length,data[:self.length])[0][::-1]
        return data[self.length:]

    def __len__(self):
        return self.length

    def show(self,depth=0):
        return

    def __eq__(self,b):
        return self.val==b

class NBytes_List:

    def __init__(self,name,bytes=2):
        self.name=name
        self.length=bytes
        self.lonbytes = []

    def decode(self,data):
        while data:
            mynbyte=NBytes("",self.length)
            data=mynbyte.decode(data)
            self.lonbytes.append(mynbyte)
        return data

    def show(self,depth=0):
        for x in self.lonbytes:
            x.show(depth)

    def __len__(self):
        return len(self.lonbytes)+self.length

    def __contains__(self,b):
        for x in self.lonbytes:
            if b == x:
                return True

        return False

class Float88:

    def __init__(self,name):
        self.name=name
        self.val=0.0

    def encode (self):
        val=pack(">h",int(self.val*256))
        return val

    def decode(self,data):
        self.val= unpack(">h",data)[0]/256.0
        return data[2:]
    def __len__(self):
        return 2

    def show(self,depth=0):
        return




class EmptyPayload:
    def __init__(self):
        pass

    def encode(self):
        return b""

    def decode(self,data):
        return data

    def __len__(self):
        return 0

    def show(self,depth=0):
        return


class Packet:

    def __init__(self, header="\x00", fmt=">B"):
        self.header = header
        self.fmt = fmt
        self.payload=[]
        self.raw_data=None

    def encode (self) :
        return pack(self.fmt, self.header)

    def decode (self, data):
        try:
            if unpack(self.fmt,data[:calcsize(self.fmt)])[0] == self.header:
                self.raw_data=data
                return data[calcsize(self.fmt):]
        except:
            pass
        return None

    def retrieve(self,aclass):
        resu=[]
        for x in self.payload:
            try:
                if isinstance(aclass,str):
                    if x.name == aclass:
                        resu.append(x)
                else:
                    if isinstance(x,aclass):
                        resu.append(x)

                resu+=x.retrieve(aclass)
            except:
                pass
        return resu

class HCI_Command(Packet):

    def __init__(self,ogf,ocf):
        super().__init__(HCI_COMMAND)
        self.cmd = OgfOcf("command",ogf,ocf)
        self.payload = []

    def encode(self):
        pld=b""
        for x in self.payload:
            pld+=x.encode()
        plen=len(pld)
        pld=b"".join([super().encode(),self.cmd.encode(),pack(">B",plen),pld])
        return pld

    def show(self,depth=0):
        self.cmd.show(depth)
        for x in self.payload:
            x.show(depth)

class HCI_Cmd_LE_Scan_Enable(HCI_Command):

    def __init__(self,enable=True,filter_dups=True):
        super(self.__class__, self).__init__(b"\x08",b"\x0c")
        self.payload.append(Bool("enable",enable))
        self.payload.append(Bool("filter",filter_dups))

class HCI_Cmd_LE_Set_Scan_Params(HCI_Command):

    def __init__(self,scan_type=0x0,interval=10, window=750, oaddr_type=0,filter=0):

        super(self.__class__, self).__init__(b"\x08",b"\x0b")
        self.payload.append(EnumByte("scan type",scan_type,
                                     {0: "Passive",
                                      1: "Active"}))
        self.payload.append(UShortInt("Interval",int(round(min(10240,max(2.5,interval))/0.625)),endian="little"))
        self.payload.append(UShortInt("Window",int(round(min(10240,max(2.5,min(interval,window)))/0.625)),endian="little"))
        self.payload.append(EnumByte("own addresss type",oaddr_type,
                                     {0: "Public",
                                      1: "Random",
                                      2: "Private IRK or Public",
                                      3: "Private IRK or Random"}))
        self.payload.append(EnumByte("filter policy",filter,
                                     {0: "None",
                                      1: "Sender In White List",
                                      2: "Almost None",
                                      3: "SIWL and some"}))


class HCI_Cmd_LE_Advertise(HCI_Command):

    def __init__(self,enable=True):
        super(self.__class__, self).__init__(b"\x08",b"\x0a")
        self.payload.append(Bool("enable",enable))

class HCI_Cmd_LE_Set_Advertised_Msg(HCI_Command):

    def __init__(self,msg=EmptyPayload()):
        super(self.__class__, self).__init__(b"\x08",b"\x08")
        self.payload.append(msg)

class HCI_Cmd_LE_Set_Advertised_Params(HCI_Command):

    def __init__(self,interval_min=500, interval_max=750,
                       adv_type=0x3, oaddr_type=0, paddr_type=0,
                       peer_addr="00:00:00:00:00:00", cmap=0x7, filter=0):

        super(self.__class__, self).__init__(b"\x08",b"\x06")
        self.payload.append(UShortInt("Adv minimum",int(round(min(10240,max(20,interval_min))/0.625)),endian="little"))
        self.payload.append(UShortInt("Adv maximum",int(round(min(10240,max(20,max(interval_min,interval_max)))/0.625)),endian="little"))
        self.payload.append(EnumByte("adv type",adv_type,
                                        {0: "ADV_IND",
                                         1: "ADV_DIRECT_IND high",
                                         2: "ADV_SCAN_IND",
                                         3: "ADV_NONCONN_IND",
                                         4: "ADV_DIRECT_IND low"}))
        self.payload.append(EnumByte("own addresss type",paddr_type,
                                     {0: "Public",
                                      1: "Random",
                                      2: "Private IRK or Public",
                                      3: "Private IRK or Random"}))
        self.payload.append(EnumByte("peer addresss type",oaddr_type,
                                     {0: "Public",
                                      1: "Random"}))
        self.payload.append(MACAddr("peer",mac=peer_addr))
        self.payload.append(BitFieldByte("Channels",cmap,["Channel 37","Channel 38","Channel 39","RFU","RFU","RFU","RFU", "RFU"]))

        self.payload.append(EnumByte("filter policy",filter,
                                     {0: "None",
                                      1: "Scan",
                                      2: "Connection",
                                      3: "Scan and Connection"}))

class HCI_Cmd_Reset(HCI_Command):
    def __init__(self):
        super(self.__class__, self).__init__(b"\x03",b"\x03")



class HCI_Event(Packet):

    def __init__(self,code=0,payload=[]):
        super().__init__(HCI_EVENT)
        self.payload.append(Byte("code"))
        self.payload.append(UIntByte("length"))

    def decode(self,data):
        data=super().decode(data)
        if data is None:
            return None

        for x in self.payload:
            x.decode(data[:len(x)])
            data=data[len(x):]
        code=self.payload[0]
        length=self.payload[1].val
        if code.val==b"\x0e":
            ev = HCI_CC_Event()
            data=ev.decode(data)
            self.payload.append(ev)
        elif code.val==b"\x3e":
            ev = HCI_LE_Meta_Event()
            data=ev.decode(data)
            self.payload.append(ev)
        else:
            ev=Itself("Payload")
            data=ev.decode(data)
            self.payload.append(ev)
        return data

    def show(self,depth=0):
        for x in self.payload:
            x.show(depth)


class HCI_CC_Event(Packet):
    def __init__(self):
        self.name="Command Completed"
        self.payload=[UIntByte("allow pkt"),OgfOcf("cmd"),Itself("resp code")]


    def decode(self,data):
        for x in self.payload:
            data=x.decode(data)
        return data

    def show(self,depth=0):
        for x in self.payload:
            x.show(depth)

class HCI_LE_Meta_Event(Packet):
    def __init__(self):
        self.name="LE Meta"
        self.payload=[Byte("code")]

    def decode(self,data):
        for x in self.payload:
            data=x.decode(data)
        code=self.payload[0]
        if code.val==b"\x02":
            ev=HCI_LEM_Adv_Report()
            data=ev.decode(data)
            self.payload.append(ev)
        else:
            ev=Itself("Payload")
            data=ev.decode(data)
            self.payload.append(ev)
        return data

    def show(self,depth=0):
        for x in self.payload:
            x.show(depth)


class HCI_LEM_Adv_Report(Packet):
    def __init__(self):
        self.name="Adv Report"
        self.payload=[UIntByte("num reports"),
                      EnumByte("ev type",0,{0:"generic adv", 3:"no connection adv", 4:"scan rsp"}),
                      EnumByte("addr type",0,{0:"public", 1:"random"}),
                      MACAddr("peer")]


    def decode(self,data):

        for x in self.payload:
            data=x.decode(data)
        while len(data) > 1:
            length=UIntByte("sublen")
            data=length.decode(data)
            code=EIR_Hdr()
            data=code.decode(data)
            myinfo=Itself("Payload for %s"%code.strval)
            xx=myinfo.decode(data[:length.val-len(code)])
            self.payload.append(myinfo)
            data=data[length.val-len(code):]
        if data:
            myinfo=IntByte("rssi")
            data=myinfo.decode(data)
            self.payload.append(myinfo)
        return data

    def show(self,depth=0):
        if len(str(self.payload[5].val)) < 4:
            #print(str(self.payload[3].val))
            #print(str(self.payload[5].val))
            subprocess.call("mosquitto_pub -t /devices/BLE/controls/%s -r  -m %s" % (str(self.payload[3].val), str(self.payload[5].val)), shell=True)
            subprocess.call("mosquitto_pub -t /devices/BLE/controls/%s/meta/type -r  -m value" % (str(self.payload[3].val)), shell=True)

class EIR_Hdr(Packet):
    def __init__(self):
        self.type= EnumByte("type", 0, {
            0x01: "flags",
            0x02: "incomplete_list_16_bit_svc_uuids",
            0x03: "complete_list_16_bit_svc_uuids",
            0x04: "incomplete_list_32_bit_svc_uuids",
            0x05: "complete_list_32_bit_svc_uuids",
            0x06: "incomplete_list_128_bit_svc_uuids",
            0x07: "complete_list_128_bit_svc_uuids",
            0x08: "shortened_local_name",
            0x09: "complete_local_name",
            0x0a: "tx_power_level",
            0x0d: "class_of_device",
            0x0e: "simple_pairing_hash",
            0x0f: "simple_pairing_rand",
            0x10: "sec_mgr_tk",
            0x11: "sec_mgr_oob_flags",
            0x12: "slave_conn_intvl_range",
            0x17: "pub_target_addr",
            0x18: "rand_target_addr",
            0x19: "appearance",
            0x1a: "adv_intvl",
            0x1b: "le_addr",
            0x1c: "le_role",
            0x14: "list_16_bit_svc_sollication_uuids",
            0x1f: "list_32_bit_svc_sollication_uuids",
            0x15: "list_128_bit_svc_sollication_uuids",
            0x16: "svc_data_16_bit_uuid",
            0x20: "svc_data_32_bit_uuid",
            0x21: "svc_data_128_bit_uuid",
            0x22: "sec_conn_confirm",
            0x23: "sec_conn_rand",
            0x24: "uri",
            0xff: "mfg_specific_data",
        })

    def decode(self,data):
        return self.type.decode(data)

    def show(self):
        return self.type.show()

    @property
    def val(self):
        return self.type.val

    @property
    def strval(self):
        return self.type.strval

    def __len__(self):
        return len(self.type)

class Adv_Data(Packet):
    def __init__(self,name,length):
        self.name=name
        self.length=length
        self.payload=[]

    def decode(self,data):
        myinfo=NBytes("Service Data uuid",self.length)
        data=myinfo.decode(data)
        self.payload.append(myinfo)
        if data:
            myinfo=Itself("Adv Payload")
            data=myinfo.decode(data)
            self.payload.append(myinfo)
        return data

    def show(self,depth=0):
        for x in self.payload:
            x.show(depth)

    def __len__(self):
        resu=0
        for x in self.payload:
            resu+=len(x)
        return resu


def create_bt_socket(interface=0):
    exceptions = []
    sock = None
    try:
        sock = socket.socket(family=socket.AF_BLUETOOTH,
                             type=socket.SOCK_RAW,
                             proto=socket.BTPROTO_HCI)
        sock.setblocking(False)
        sock.setsockopt(socket.SOL_HCI, socket.HCI_FILTER, pack("IIIh2x", 0xffffffff,0xffffffff,0xffffffff,0))
        try:
            sock.bind((interface,))
        except OSError as exc:
            exc = OSError(
                    exc.errno, 'error while attempting to bind on '
                    'interface {!r}: {}'.format(
                        interface, exc.strerror))
            exceptions.append(exc)
    except OSError as exc:
        if sock is not None:
            sock.close()
        exceptions.append(exc)
    except:
        if sock is not None:
            sock.close()
        raise
    if len(exceptions) == 1:
        raise exceptions[0]
    elif len(exceptions) > 1:
        model = str(exceptions[0])
        if all(str(exc) == model for exc in exceptions):
            raise exceptions[0]
        raise OSError('Multiple exceptions: {}'.format(
            ', '.join(str(exc) for exc in exceptions)))
    return sock



class BLEScanRequester(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.smac = None
        self.sip = None
        self.process = self.default_process

    def connection_made(self, transport):
        self.transport = transport
        command=HCI_Cmd_LE_Set_Scan_Params()
        self.transport.write(command.encode())

    def connection_lost(self, exc):
        super().connection_lost(exc)

    def send_scan_request(self):
        command=HCI_Cmd_LE_Scan_Enable(True,False)
        self.transport.write(command.encode())

    def stop_scan_request(self):
        command=HCI_Cmd_LE_Scan_Enable(False,False)
        self.transport.write(command.encode())

    def send_command(self,command):
        self.transport.write(command.encode())

    def data_received(self, packet):
        self.process(packet)

    def default_process(self,data):
        pass
