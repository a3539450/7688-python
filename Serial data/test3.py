import time
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

deviceId = "S11kn0Wi7"
deviceKey = "369cb0bb9fcebeb880c037ce55f0fc00a9456937c2e44c615ab9784ab1081e43"
ip = "test233.bounceme.net"
port = "80"

def post_to_mcslite(payload):
    headers = {"Content-type": "text/csv", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection(ip + ":" + port)
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(30) 

    conn.request("POST", "/api/devices/" + deviceId + "/datapoints.csv", payload, headers)
    response = conn.getresponse()
    #print( response.status, response.reason, payload, time.strftime("%c"))
    #print( response.reason, payload, response.read())
    print( payload, headers )
    #data = response.read()
    conn.close()

while True:
    value = bridgeclient()
    h0 = value.get("h") ##arduino
    t0 = value.get("t") ##arduino
    m0 = value.get("m") ##arduino
    p0 = value.get("p") ##arduino
    t0String = "temp,,"  + t0
    h0String = "humi,,"  + h0
    m0String = "meter,," + m0
    p0String = "hpa,,"   + p0
    payload =  p0String + "\n" + m0String + "\n" + h0String + "\n" + t0String + "\n"
    post_to_mcslite(payload)
    time.sleep(30)