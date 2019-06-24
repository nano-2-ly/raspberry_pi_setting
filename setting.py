import serial, time 
SERIALPORT = "/dev/ttyAMAO" 
BAUDRATE = 115200 
ser = serial.Serial(SERIALPORT, BAUDRATE) 
#ser bytesize = serial. EIGHTBITS 
#ser.parity = serial.PARITY_NONE 
#set parity check: no parity 
#ser.stopbits = serial.STOPBITS_ONE 
#number of stop bits ser timeout = 0.1 
#if O read block #ser.xonxoff = False 
#disable software flow control 
#ser.rtscts = False 
#disable hardware flow control 
#serdardts = False 
#disable hardware flow control 
#ser.writeTimeout= 0 
#timeout for write print ("Starting Up Serial Monitor") 
try:
    ser.open() 
except Exception as e:
    print ("Exception: Opening serial port:"+str(e)) 
if ser.isOpen(): 
# print(ser.posrtstr) #connected port 
    try:
        ser.flushinput()
        ser.flushOutput() 
        time sleep(0.1) 
        while True:
            ser.write(b'1') 
            print("write 1") 
            response = ser readline().decode()
            print("pi3 recv data:" + str(response)) 
        ser.close()
    except Exception as e :
        print ("Error Communicating..." + str(e)) 
        ser.close()
    finally:
        ser.close()
        pass 
    else:
        print ("Cannot open serial port.")
