import csv
import sys
import serial

def main():
    with open('C:\python\casd.csv',  newline='') as csvfile:
        writer = csv.reader(csvfile)
        # print(writer)
        for i,rows in enumerate(writer):
            if i <= 3:
                row = rows
                data = row[0] + ',' + row[1] + ',' + row[2]
                print(row)
    csvfile.closed
if __name__ == "__main__":
     main()