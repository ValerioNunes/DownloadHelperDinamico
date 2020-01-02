
from time import sleep             # lets us have a delay  
import thread
import time
import os

statusLed = False
if (os.name == 'posix'):
	import RPi.GPIO as GPIO          
	GPIO.setmode(GPIO.BCM)            
	GPIO.setup(24, GPIO.OUT)
	statusLed = True

delay =  1
led =  True

def falhaPendrive():
	global delay
	delay =  0.1

def enviando():
	global delay
	delay =  1
	
def sucesso():
	global led
	led = False
	
def print_time( threadName):
	print(threadName)
	try:
		if(statusLed):
			while led:
				GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
				sleep(delay)                 # wait half a second  
				GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
				sleep(delay) 
			GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
			sleep(5)   
			GPIO.output(24, 0) 
			GPIO.cleanup() 		
	except KeyboardInterrupt:          
		GPIO.cleanup()   
		

try:
    thread.start_new_thread( print_time, ("Thread-Led", ))
except:
   print "Error: unable to start thread"

