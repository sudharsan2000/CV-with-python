import serial

s= serial.Serial('COM3', baudrate = 9600 , timeout = 1)
while 1:
 data = s.readline().decode('ascii')
 print data
