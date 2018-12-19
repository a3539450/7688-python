import sys
import serial
import urllib
import time

# host='http://www.google.com/'

# while True:
#         try:
#             urllib.urlopen(host)
#             connect = 0
#             time.sleep(10)
#             print("Success connect")
#         except:
#             connect = 1
#             time.sleep(15)
#             print("Connect Failed")


Serial2 = 115200
# srl = serial.Serial('COM5',115200)
ser = serial.Serial('/dev/ttyS0',115200)

while True:

    data = str(ser.readline())
    dataa = data.replace("\n","")
    data1 = dataa.split(",")
    for i,rows in enumerate(data1):
        if i == 0:
            data2 = rows[2:6]
        if i == 1:
            data3 = rows[2:6]
        if i == 2:
            data4 = rows[2:6]
        if i == 3:
            data5 = rows[2:6]
        if i == 4:
            data6 = rows[2:6]
        if i == 5:
            data7 = rows[2:6]
    print(data2)
    print(data3)
    print(data4)
    print(data5)
    print(data6)
    print(data7)
    print(data)

    # print(ser.readline())
    # if ser.read()=='a':
    #     IncommingNum = ser.read()
    #     sensor = int(ser.read(int(IncommingNum)))
    #     a = 8
    #     a += int(IncommingNum)
    #     print(sensor,a)
    # if ser.read()=='b':
    #     IncommingNum = ser.read()
    #     sensor1 = int(ser.read(int(IncommingNum)))
    #     a1 = 8
    #     a1 += int(IncommingNum)
    #     print(sensor1,a1)
       