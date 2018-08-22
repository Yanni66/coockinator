#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import asyncio
import argparse
import re
import aioblescan as aiobs


def check_mac(val):
    try:
        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", val.lower()):
            return val.lower()
    except:
        pass
    raise argparse.ArgumentTypeError("%s is not a MAC address" % val)

parser = argparse.ArgumentParser(description="Track BLE advertised packets")
parser.add_argument("-m", "--mac", type=check_mac, action='append',
                    help="Look for these MAC addresses.")
parser.add_argument("-R","--raw", action='store_true', default=False,
                    help="Also show the raw data.")
parser.add_argument("-a","--advertise", type= int, default=0,
                    help="Broadcast like an EddyStone Beacon. Set the interval between packet in millisec")
parser.add_argument("-D","--device", type=int, default=0,
                    help="Select the hciX device to use (default 0, i.e. hci0).")
try:
    opts = parser.parse_args()
except Exception as e:
    parser.error("Error: " + str(e))
    sys.exit()

def my_process(data):
    global opts

    ev=aiobs.HCI_Event()
    xx=ev.decode(data)
    if opts.mac:
        goon = False
        mac= ev.retrieve("peer")
        for x in mac:
            if x.val in opts.mac:
                goon=True
                break
        if not goon:
            return

    if opts.raw:
        print("Raw data: {}".format(ev.raw_data))
    else:
        ev.show(0)

try:
    mydev=int(sys.argv[1])
except:
    mydev=0


event_loop = asyncio.get_event_loop()
mysocket = aiobs.create_bt_socket(mydev)
fac=event_loop._create_connection_transport(mysocket,aiobs.BLEScanRequester,None,None)
conn,btctrl = event_loop.run_until_complete(fac)
btctrl.process=my_process
if opts.advertise:
    command = aiobs.HCI_Cmd_LE_Advertise(enable=False)
    btctrl.send_command(command)
    command = aiobs.HCI_Cmd_LE_Set_Advertised_Params(interval_min=opts.advertise,interval_max=opts.advertise)
    btctrl.send_command(command)
    command = aiobs.HCI_Cmd_LE_Set_Advertised_Msg(msg=EddyStone())
    btctrl.send_command(command)
    command = aiobs.HCI_Cmd_LE_Advertise(enable=True)
    btctrl.send_command(command)

btctrl.send_scan_request()
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    print('keyboard interrupt')
finally:
    print('closing event loop')
    btctrl.stop_scan_request()
    command = aiobs.HCI_Cmd_LE_Advertise(enable=False)
    btctrl.send_command(command)
    conn.close()
    event_loop.close()
