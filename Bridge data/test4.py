import sys
import time
import csv
#import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient




while True:
    value = bridgeclient()
    h0 = value.get("h") ##arduino
    t0 = value.get("t") ##arduino
    m0 = value.get("m") ##arduino
    p0 = value.get("p") ##arduino
    p1 = str(int(time.time()))
    t0String = "temp,," + t0
    h0String = "humi,," + h0
    m0String = "m,,"    + m0
    p0String = "hpa,,"  + p0
    payload =  t0String + "\n" + h0String + "\n" + m0String + "\n" + p0String + "\n" + p1 + "\n"
    with open('/MCS/output.csv', 'a') as csvfile:
     writer = csv.writer(csvfile)
     table = [
     ["temp",p1,t0],
     ["humi",p1,h0],
     ["m",p1,m0],
     ["hpa",p1,p0]]
     writer.writerow(table)
    csvfile.closed
    print(payload)
    #print(p1)
    time.sleep(120)