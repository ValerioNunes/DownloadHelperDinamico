
from time import sleep             # lets us have a delay  
import thread
import time
import os

delay =  1
led =  True
ledPin =  24
statusLed = False

if (os.name == 'posix'):
	import RPi.GPIO as GPIO          
	GPIO.setmode(GPIO.BCM)            
	GPIO.setup(ledPin, GPIO.OUT)
	statusLed = True


def ligarLed():
		GPIO.output(ledPin, 1)
		sleep(5) 


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
				GPIO.output(ledPin, 1)         # set GPIOledPin to 1/GPIO.HIGH/True  
				sleep(delay)                 # wait half a second  
				GPIO.output(ledPin, 0)         # set GPIOledPin to 0/GPIO.LOW/False  
				sleep(delay) 
			GPIO.output(ledPin, 1)         # set GPIOledPin to 1/GPIO.HIGH/True  
			sleep(5)   
			GPIO.output(ledPin, 0) 
			GPIO.cleanup() 		
	except KeyboardInterrupt:          
		GPIO.cleanup()   
		

try:
    thread.start_new_thread( print_time, ("Thread-Led", ))
except:
   print "Error: unable to start thread"

