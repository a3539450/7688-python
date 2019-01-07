import sys
import time
import csv
import urllib
import threading
import httplib
import socket
import serial
import logging
logging.basicConfig(filename='/tmp/myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
global connect
global L
payload = ""
table = ""
DA = 0
DB = 0
DC = 0
DD = 0
DE = 0
DV = int(0)
DF = 0
DS = ""
CD = int(0)
host='http://www.google.com/'
deviceId = "DpjBrN1w"
deviceKey = "0FQSO35FKLFkjpLF"
ip = "api.mediatek.com"
port = "80"
timeout=5
connect = 1
Serial2 = 115200
ports = '/dev/ttyS0' 
ser = serial.Serial(ports,Serial2)
def connected():
    print("Connect Test")
    global connect
    while True:
        try:
            urllib.urlopen(host)
            connect = 0
            time.sleep(10)
            print("Success connect")
            return connect
        except:
            connect = 1
            time.sleep(15)
            print("Connect Failed")
            return connect
Thread1 = threading.Thread(target = connected)

def csvfile(table,payload):   
    if connect == 1:
        print("Connect Fuck")
        with open('/MCS/output1.csv', 'a') as csvfile: 
            writer2 = csv.writer(csvfile)
            writer2.writerows(table)
        csvfile.closed
    else :
        print("Connect OK")
        headers = {"Content-type": "text/json", "deviceKey": deviceKey}
        try:
            print("Connect ASSS")
            conn = httplib.HTTPConnection(ip + ":" + port) 
            conn.connect()
        except (httplib.HTTPException, socket.error) as ex: 
            with open('/MCS/output1.csv', 'a') as csvfile: 
                writer1 = csv.writer(csvfile)
                writer1.writerows(table)
            csvfile.close
            logger.error(ex)
    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    conn.close

def ttes():
    global DA
    global DB
    global DC
    global DD
    global DE
    global DS
    global CD
    global DV
    global payload
    global table
    while True:
        p1 = str(int(time.time()))
        serread = str(ser.readline())
        sera = serread.replace("\n","")
        data1 = sera.split(",")
        print(data1)
        for i,rows in enumerate(data1):
            if i == 0:
                DA = rows[2:6]
            if i == 1:
                DB = rows[2:6]
            if i == 2:
                DC = rows[2:6]
            # if i == 3:
                # DD = rows[2:5]
                DD = "0"
            if i == 4:
                DE = rows[2:8]
            if i == 5:
                DV = rows[2:5]
        CD = CD + int(DV)
        DS = ('%.3f' % float(float(CD) / 60 / 60))
        D1String = "D1,," + DA
        D2String = "D2,," + DB
        D3String = "D3,," + DC
        D4String = "D4,," + DD
        D5String = "D5,," + DE
        D6String = "D6,," + DS
        payload = D1String + "\n" + D2String + "\n" + D3String + "\n" + D4String + "\n" + D5String + "\n" + D6String + "\n"
        table = [
        ["D1",p1,DA],
        ["D2",p1,DB],
        ["D3",p1,DC],
        ["D4",p1,DD],
        ["D5",p1,DE],
        ["D6",p1,DS],
        ]
    print(payload)
    time.sleep(1)
Thread3 = threading.Thread(target = ttes)

def read():
    while True:
        time.sleep(30)
        csvfile(table,payload)
Thread4 = threading.Thread(target = read)

def main():
    Thread1.start()
    Thread3.start()
    Thread4.start()
if __name__ == "__main__":
    main()