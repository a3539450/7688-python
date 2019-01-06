import sys
import time
import csv
import urllib
import threading
#import http ## Windows Python 3.2
import httplib ## Unix Python 2.7
import socket
import serial
import logging
#import datetime

logging.basicConfig(filename='/tmp/myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
global connect
global L
global tt
global DF
global DG
DG = 0
DF = 0
tt = 0
host='http://www.google.com/'
deviceId = "DpjBrN1w"
deviceKey = "0FQSO35FKLFkjpLF"
ip = "api.mediatek.com"
port = "80"
timeout=5
connect = 1
Serial2 = 115200
ports = '/dev/ttyS0' ## Unix 7688
# ports = 'COM5' ## Windows System
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
        with open('/MCS/output1.csv', 'a') as csvfile: ##Python 2.7 Unix
        # with open('C:\python\data.csv ', 'a', newline='' ) as csvfile: ##Python 3.x Windows
            writer2 = csv.writer(csvfile)
            writer2.writerows(table)
        csvfile.closed
    else :
        print("Connect OK")
        # with open('/MCS/output1.csv') as readcsvfile:
        # # with open('C:\Python\casd.csv', newline='') as readcsvfile:
        #     read1 = csv.reader(readcsvfile)
        #     for i , row in enumerate(read1)
        #         if i <= 3:
        #         row = rows
        #         data = row[0] + ',' + row[1] + ',' + row[2]
        #         print(data)
        #     readcsvfile.close
        headers = {"Content-type": "text/json", "deviceKey": deviceKey}
        try:
            print("Connect ASSS")
            # conn = http.client.HTTPConnection(ip + ":" + port, timeout=30) ## Windows Python 3.x
            conn = httplib.HTTPConnection(ip + ":" + port) ## Unix Python 2.7
            conn.connect()
        #except (http.client.HTTPException, socket.error) as ex: ## Windows Python 3.x
        except (httplib.HTTPException, socket.error) as ex: ## Unix Python 2.7
            with open('/MCS/output1.csv', 'a') as csvfile: ## Python 2.7 Unix
            # with open('C:\python\data.csv', 'a', newline='')as csvfile1: ## Python 3.x Windows
                writer1 = csv.writer(csvfile)
                writer1.writerows(table)
            csvfile.close
            logger.error(ex)
    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    conn.close

# def Water():
#     # global L
#     global tt
#     global DG
#     global DF
#     mls = DG/60
#     DF = DF + mls
#     tt = tt + 1
#     Thread3 = threading.Thread( target = Water )

def Serial():
    global DE
    global DF
    global DG
    while True:
        # serread = str(ser.readline())
        # sera = serread.replace("\n","")
        # data1 = sera.split(",")
        # for i , rows in enumerate(data1):
        #     if i == 4:
        #         DE = rows[2:5]
        #     if i == 5:
        #         DG = rows[2:5]
        print(DG)
        # DH = DG / 60
        # DJ = DF + DH
        # DF = str(DJ)
    
Thread2 = threading.Thread(target = Serial)
        
def ttes():
    global DF
    global DG
    DS = str(DF)
    DE = str(0) 
    DD = str(0)
    while True:
        p1 = str(int(time.time()))
        serread = str(ser.readline())
        sera = serread.replace("\n","")
        data1 = sera.split(",")
        for i,rows in enumerate(data1):
            if i == 0:
                DA = rows[2:6]
            if i == 1:
                DB = rows[2:6]
            if i == 2:
                DC = rows[2:6]
            # if i == 3:
            #     DD = rows[2:5]
            if i == 4:
                DG = rows[2:5]
            if i == 5:
                DE = rows[2:5]
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
        ["D6",p1,DF],
        ]
        time.sleep(20)
        csvfile(table,payload)
Thread3 = threading.Thread(target = ttes)

def main():
    Thread1.start()
    Thread2.start()
    Thread3.start()

if __name__ == "__main__":
    main()