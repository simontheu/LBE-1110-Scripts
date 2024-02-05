#Leo Bodnar USB Serial Timecode Reader

#Select serial device string based on OS
#devString = '/dev/ttyACM0'				#Rpi/Linux
#devString = '/dev/tty.usbmodem1401'	#MacOS
devString = 'COM3'						#Windows - needs correct port number dependent on your system

import serial
import time
bootloaderTrigger = 0xdeface

try:
	serialDevice = serial.Serial(devString, timeout=10, baudrate=bootloaderTrigger)

except:
	print ("Unable to connect to serial device")
	quit()


print ("Connected to: " + serialDevice.name)
