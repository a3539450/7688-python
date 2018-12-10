import csv
import sys
import serial

def main():
    with open('C:\python\casd.csv',  newline='') as csvfile:
        writer = csv.reader(csvfile)
        for i,rows in enumerate(writer):
            if i <= 3:
                row = rows
                data = row[0] + ',' + row[1] + ',' + row[2]
                print(data)
    csvfile.closed
if __name__ == "__main__":
     main()