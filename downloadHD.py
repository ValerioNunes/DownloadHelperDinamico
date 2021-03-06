

import json
import subprocess
import shutil
import time 
#import logging
import restHD
import zipHD
import io
import ledHD	
import deletarlogs
import setparametros as par
import os

#logging.basicConfig(filename='VSHelpDinamico.log',level=logging.DEBUG)

print(par.getJsonParametros())

parametros = par.getNameFileParametros()
def existeArq(file):
  try:
    f = open(file)
    f.close()
    return True
  except:
    return False

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return temp

def iwconfig():
        temp = os.popen("iwconfig").readline()
        return temp
		
def Desligar():
	print 'Desligar'
	ledHD.sucesso()
	print loco['origem']
	deletarlogs.start(loco['origem'])
	#os.system("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind")
	if (os.name == 'posix'):
		subprocess.call("/sbin/shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def now():
	return  time.asctime(time.localtime(time.time()))

def isPenDrive():
		pasta = loco['origem'];
		caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
		arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
		if(len(arquivos) > 0):
			return True
		return False
				 
def moverArquivos():

	if (isPenDrive()):
			if(zipHD.ZippArquivo(loco)):	
				try:	
					ledHD.enviando()
					file = {'file':  open(zipHD.getArquivoZip(), 'rb')}
					resposta =  restHD.sendLog(loco, file)
					print "Duracao : "+getDuracao()+" Segundos -> Result : ", resposta
					#logging.info(now()+"Duracao : "+getDuracao()+" Segundos -> Result "+resposta)
					if(resposta == '"Sucessagem!"'):
						os.remove(zipHD.getArquivoZip())
						Desligar()
				except OSError as err:
					#logging.warning(now()+" OS error: {0}".format(err))
					print(now()+" OS error: {0}".format(err))
				if(existeArq(zipHD.getArquivoZip())):
					os.remove(zipHD.getArquivoZip())
	
					
	else:
		#logging.warning(now()+" Pendrive nao encontrado !!! ")
		print (now()+" Nenhum Arquivo Encontrado !!! ")	
		ledHD.falhaPendrive()
		
def openParametros():
	global loco
	try:
		with open(parametros) as f:    
			loco = json.load(f)
			
			if(loco['status'] == "start"):
				return True
			else:
				return False
	except OSError as err:
		#logging.warning(now()+" OS error: {0}".format(err))
		print(now()+" OS error: {0}".format(err))
		return False

def getDuracao():
	return str(int(time.time() - inicio))

def setInicio(tempo):
			global inicio
			inicio = tempo
			
def getDelay():
	return loco['delay']
	
def main():
	
	#logging.info("\n"+now()+" Iniciando... "+ measure_temp())
	print ("\n"+now()+" Iniciando... "+ measure_temp())
	moverArquivos()
	#logging.info("\n"+now()+" Finalizado "+ measure_temp())
	print ("\n"+now()+" Finalizado "+ measure_temp())
	
	
	
