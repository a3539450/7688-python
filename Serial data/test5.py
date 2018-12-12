import sys
import time
import csv
import urllib
import threading
import http
import socket
import serial
#import datetime

#sys.path.insert(0, '/usr/lib/python2.7/bridge/')  # Type Bridge
#from bridgeclient import BridgeClient as bridgeclient

global connect 
host='http://www.google.com/'
deviceId = "DZv4BltK"
deviceKey = "rXBX27o4aGY7SnPa"
ip = "api.mediatek.com"
port = "80"
timeout=5
connect = 1
Serial2 = 115200
srl = serial.Serial('/dev/ttyS0',Serial2)
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
        #with open('/MCS/output1.csv', 'a') as csvfile: ##Python 2.7 Unix
        with open('C:\python\data.csv ', 'a', newline='' ) as csvfile: ##Python 3.x Windows
            writer2 = csv.writer(csvfile)
            writer2.writerows(table)
        csvfile.closed
    else :
        with open('C:\Python\casd.csv', newline='') as readcsvfile:
            read1 = csv.reader(readcsvfile)
            for i,row in enumerate(read1)
                if i <= 3:
                row = rows
                data = row[0] + ',' + row[1] + ',' + row[2]
                print(data)
        headers = {"Content-type": "text/json", "deviceKey": deviceKey}
        conn = http.client.HTTPConnection(ip + ":" + port, timeout=30)
        try:
            conn.connect()
            conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)
            response = conn.getresponse()
            print( response.status, response.reason, payload, time.strftime("%c"))
            conn.close  
            #http.client.HTTPConnection.close()
        except (http.client.HTTPException, socket.error) as ex:
            #with open('/MCS/output1.csv', 'a') as csvfile: ##Python 2.7 Unix
            with open('C:\python\data.csv', 'a', newline='')as csvfile1: ##Python 3.x Windows
                writer1 = csv.writer(csvfile1)
                writer1.writerows(table)
            csvfile.close
            #with open('/log/error.log', 'a') as log: ## Python 2.7 Unix
            with open('C:\python\error.log', 'a', newline='') as log: ## Python 3.x Windows
                error = log.writer(log)
                error.writerow("Error: %s" % ex)

def data():
    if connect == 1:
        



def ttes():
    while True:
        int D1, D2, D3, D4, D5, D6, D7, D8, D9, E1, E2, E3
        data = str(ser.readline())
        dataa = data.replace("\n","")
        data1 = dataa.split(",")
        for i,rows in enumerate(data1):
            if i == 0:
                D1 = rows[0:5]
            else:
                D1 = '0'
            if i == 1:
                D2 = rows[0:5]
            else:
                D2 = '0'
            if i == 2:
                D3 = rows[0:5]
            else:
                D3 = '0'
            if i == 3:
                D4 = rows[0:5]
            else:
                D4 = '0'
            if i == 4:
                D5 = rows[0:5]
            else:
                D5 = '0'
            if i == 5:
                D6 = rows[0:5]
            else:
                D6 = '0'
        D1String = "D1,," + D1
        D2String = "D2,," + D2
        D3String = "D3,," + D3
        D4String = "D4,," + D4
        D5String = "D5,," + D5
        D6String = "D6,," + D6
        payload = D1String + "\n" + D2String + "\n" + D3String + "\n" + D4String + "\n" + D5String + "\n" + D6String + "\n"
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