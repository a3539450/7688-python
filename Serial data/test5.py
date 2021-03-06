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
        with open('C:\python\data.csv', 'a', newline='' ) as csvfile: ##Python 3.x Windows
            writer1 = csv.writer(csvfile)
            writer1.writerows(table)
        csvfile.closed
    else :
        headers = {"Content-type": "text/csv", "deviceKey": deviceKey}
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
            with open('C:\python\data.csv', 'a', newline='')as csvfile: ##Python 3.x Windows
                writer = csv.writer(csvfile)
                writer.writerows(table)
            csvfile.close
            #with open('/log/error.log', 'a', newline='') as log: ## Python 2.7 Unix
            with open('C:\python\error.log', 'a', newline='') as log: ## Python 3.x Windows
                writer = log.writer(log)
                writer = writerow("Error: %s" % ex)

#def update():
    #if connect == 1:


def ttes():
    while True:
        print(connect)
        #value = bridgeclient()
        #h0 = value.get("h") ##arduino
        #t0 = value.get("t") ##arduino
        #m0 = value.get("m") ##arduino
        #p0 = value.get("p") ##arduino
        h0 = "11" ##arduino
        t0 = "12" ##arduino
        m0 = "13" ##arduino
        p0 = "14" ##arduino
        p1 = str(int(time.time()))
        t0String = "temp,," + t0
        h0String = "humi,," + h0
        m0String = "me,,"    + m0
        p0String = "hpa,,"  + p0
        payload =  t0String + "\n" + h0String + "\n" + m0String + "\n" + p0String + "\n" + p1 + "\n"
        table = [
         ["temp",p1,t0],
         ["humi",p1,h0],
         ["me",p1,m0],
         ["hpa",p1,p0]]
        csvfile(table,payload)
        time.sleep(5)
Thread2 = threading.Thread(target = ttes)

def main():
    Thread2.start()
    Thread1.start()

if __name__ == "__main__":
    main()