import downloadHD
import time
import os
import setparametros as par
downloadHD.setInicio(time.time())

def reset():
	os.system('sudo reboot')
  
try:  
	while(downloadHD.openParametros()):
		parAlterados = par.verificarMundacaDeParametros()
		if(parAlterados):
    			break
		for i in range(10):
			if(downloadHD.openParametros()):
				#downloadHD.main()
				time.sleep(downloadHD.getDelay())
			else:
				break
		if(downloadHD.openParametros()):
			reset()
except Exception as err:
	    print(" OS error: {0}".format(err))
finally:		
	reset()
