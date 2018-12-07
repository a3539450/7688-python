# import time
# import csv
import sys
import serial

Serial2 = 115200
srl = serial.Serial('/dev/ttyS0',115200)

while True:
    print(srl.read())
    # if srl.read()=='a':
    #             IncommingNum = srl.read()
    #             sensor = int(srl.read(int(IncommingNum)))

    #             # a = 8
    #             a = int(IncommingNum)
    #             print (sensor,a)
# def main():
#     h0 = "11" ##arduino
#     t0 = "12" ##arduino
#     m0 = "13" ##arduino
#     p0 = "14" ##arduino
#     p1 = str(int(time.time()))
#     t0String = "temp,," + t0
#     h0String = "humi,," + h0
#     m0String = "me,,"    + m0
#     p0String = "hpa,,"  + p0
#     payload =  t0String + "\n" + h0String + "\n" + m0String + "\n" + p0String + "\n" + p1 + "\n"
#     table = [
#         ['temp',p1,t0],
#         ['humi',p1,h0],
#         ['me',p1,m0],
#         ['hpa',p1,p0]]
#     #print(table)
#     with open('C:\python\casd.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(table)
#     csvfile.closed
# if __name__ == "__main__":
#      main()