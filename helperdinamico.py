import downloadHD
import time
import os

downloadHD.setInicio(time.time())

def reset():
	os.system('sudo reboot')
  
try:  
	while(downloadHD.openParametros()):
		for i in range(10):
			if(downloadHD.openParametros()):
				downloadHD.main()
				time.sleep(downloadHD.getDelay())
			else:
				break
		if(downloadHD.openParametros()):
			reset()
except Exception as err:
	    print(" OS error: {0}".format(err))
finally:		
	reset()
