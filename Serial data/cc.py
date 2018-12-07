import threading
import time
import urllib
import httplib

host='http://www.google.com/'
deviceId = "D0hCO0ne"
deviceKey = "PNab0wHfwi2xcwBV"
ip = "api.mediatek.com"
port = "80"

def test():
    print("test1")
Thread1 = threading.Thread(target=test)

def test2():
    print("test2")
Thread2 = threading.Thread(target=test2)

def connected():
   # print("T1 Start\n")
    while True:
        try:
            urllib.request.urlopen(host)
            time.sleep(3)
            print( 'connected')
            time.sleep(20)
            return True      
        except:
            print( 'no internet!' )
            time.sleep(20)
            return False
        
Thread3 = threading.Thread(target=connected)

def main():
    Thread1.start()
#    Thread3.start()
#    Thread3.join()
    Thread2.start()
    Thread2.join()

if __name__ == '__main__':
    main()

