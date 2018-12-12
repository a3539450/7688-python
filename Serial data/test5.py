import sys
import time
import csv
import urllib
import threading
import http
import socket
import serial
#import datetime

global connect 
host='http://www.google.com/'
deviceId = "DpjBrN1w"
deviceKey = "0FQSO35FKLFkjpLF"
ip = "api.mediatek.com"
port = "80"
timeout=5
connect = 1
Serial2 = 115200
# port = '/dev/ttyS0' ## Unix 7688
port = 'COM5' ## Windows System
srl = serial.Serial(port,Serial2)
def connected():
    global connect
    while True:
        try:
            urllib.request.urlopen(host)
            connect = 0
            time.sleep(10)
            return connect
        except:
            connect = 1
            time.sleep(15)
            return connect
Thread1 = threading.Thread(target = connected)

def csvfile(table,payload):   
    if connect == 1:
        # with open('/MCS/output1.csv', 'a') as csvfile: ##Python 2.7 Unix
        with open('C:\python\data.csv ', 'a', newline='' ) as csvfile: ##Python 3.x Windows
            writer2 = csv.writer(csvfile)
            writer2.writerows(table)
        csvfile.closed
    else :
        # with open('/MCS/output1.csv') as readcsvfile:
        # with open('C:\Python\casd.csv', newline='') as readcsvfile:
        #     read1 = csv.reader(readcsvfile)
        #     for i,row in enumerate(read1)
        #         if i <= 3:
        #         row = rows
        #         data = row[0] + ',' + row[1] + ',' + row[2]
        #         print(data)
        #     readcsvfile.close
        headers = {"Content-type": "text/json", "deviceKey": deviceKey}
        conn = http.client.HTTPConnection(ip + ":" + port, timeout=30)
        try:
            conn.connect()
            conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)
            response = conn.getresponse()
            print( response.status, response.reason, payload, time.strftime("%c"))
            conn.close  
        except (http.client.HTTPException, socket.error) as ex:
            # with open('/MCS/output1.csv', 'a') as csvfile: ##Python 2.7 Unix
            with open('C:\python\data.csv', 'a', newline='')as csvfile1: ##Python 3.x Windows
                writer1 = csv.writer(csvfile1)
                writer1.writerows(table)
            csvfile.close
            # with open('/log/error.log', 'a') as log: ## Python 2.7 Unix
            with open('C:\python\error.log', 'a', newline='') as log: ## Python 3.x Windows
                error = log.writer(log)
                error.writerow("Error: %s" % ex)
def ttes():
    while True:
        p1 = str(int(time.time()))
        int DA = 0
        int DB = 0
        int DC = 0
        int DD = 0
        int DE = 0
        int DF = 0
        data = str(ser.readline())
        dataa = data.replace("\n","")
        data1 = dataa.split(",")
        for i,rows in enumerate(data1):
            if i == 0:
                DA = rows[0:5]
            else:
                DA = '0'
            if i == 1:
                DB = rows[0:5]
            else:
                DB = '0'
            if i == 2:
                DC = rows[0:5]
            else:
                DC = '0'
            if i == 3:
                DD = rows[0:5]
            else:
                DD = '0'
            if i == 4:
                DE = rows[0:5]
            else:
                DE = '0'
            if i == 5:
                DF = rows[0:5]
            else:
                DF = '0'
        D1String = "D1,," + DA
        D2String = "D2,," + DB
        D3String = "D3,," + DC
        D4String = "D4,," + DD
        D5String = "D5,," + DE
        D6String = "D6,," + DF
        payload = D1String + "\n" + D2String + "\n" + D3String + "\n" + D4String + "\n" + D5String + "\n" + D6String + "\n"
        table = [
        ["D1",p1,DA],
        ["D2",p1,DB],
        ["D3",p1,DC],
        ["D4",p1,DD],
        ["D5",p1,DE],
        ["D6",p1,DF],
        ]
        # p1 = str(int(time.time()))
        # t0String = "temp,," + t0
        # h0String = "humi,," + h0
        # m0String = "me,,"    + m0
        # p0String = "hpa,,"  + p0
        # payload =  t0String + "\n" + h0String + "\n" + m0String + "\n" + p0String + "\n" + p1 + "\n"
        # table = [
        #  ["temp",p1,t0],
        #  ["humi",p1,h0],
        #  ["me",p1,m0],
        #  ["hpa",p1,p0]]
        csvfile(table,payload)
Thread2 = threading.Thread(target = ttes)

def main():
    Thread2.start()
    Thread1.start()

if __name__ == "__main__":
    main()