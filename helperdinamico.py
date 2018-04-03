origem  = 'C:\\Users\\valerio\\Documents\\Projetos\\Python\\origem\\'
destino = 'C:\\Users\\valerio\\Documents\\Projetos\\Python\\'

import json
from subprocess import call
import shutil
import os 
import time 
import logging

logging.basicConfig(filename='VSHelpDinamico.log',level=logging.DEBUG)


def shutdown():
    call('halt', shell=False)

def now():
	return  time.asctime( time.localtime(time.time()) )
	
def moverArquivos():
	if os.path.exists(origem) == True:	
		    try:	
				shutil.move(origem,destino + time.strftime(str(loco['locomotiva'])+'/%Y/%m/%d'))
				logging.info(now()+" Logs do HelpDinamico movidos com SUCESSO !!!")
				shutdown()
		    except OSError as err:
				logging.warning(now()+" OS error: {0}".format(err))
				print(now()+" OS error: {0}".format(err))

def main():
	logging.info(now()+" Iniciando...")
	moverArquivos()
	logging.info(now()+" Finalizado")
	time.sleep(loco['delay'])	

try:
	with open('C:\\Users\\valerio\\Documents\\Projetos\\Python\\DownloadHelperDinamico\\parametros.json') as f:    
		loco = json.load(f)
		logging.info(now()+" "+str(loco))
		print (loco)
except OSError as err:
	logging.warning(now()+" OS error: {0}".format(err))
	print(now()+" OS error: {0}".format(err))
	
	
	
main()	
	
print 'hello word'