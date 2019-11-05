import json
import io
import os
import time
import socket


locoHelper = [9020,823,829,832,824,818,9012,857,813,9014,814]
parametros = 'parametros.json'


data = {
		"locomotiva": 111,
		"delay": 60,
		"url": "http://172.20.15.22/permissaoviagem/LogHelperDinamico/SalvarLog",
		"origem": "/media/usb/test",
		"status": "start"
		}

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

os.system('cls' if os.name == 'nt' else 'clear')	

def existeArq(file):
  try:
    f = open(file)
    f.close()
    return True
  except:
    return False
	
def now():
	return  time.asctime(time.localtime(time.time()))

def addLinha(uuid):
	if(uuid != None):
		return 'UUID={0} /media/usb vfat auto,nofail,noatime,users,rw,uid=pi,gid=pi 0 0'.format(uuid)
	else:
		return 'Pendrive nao Encontrado!!!! Verificar Pendrive'
		
def IDPenDrive():
		temp = os.popen("ls -l /dev/disk/by-uuid/").read().split('\n')
		for linha in temp:
			if(linha.find('sda1') > 0):
				 return linha.split(' ')[8]
					
                    	


def openParametros():
	if(existeArq(parametros)):
	
		global data
		try:
			with open(parametros) as f:    
				loco = json.load(f)
				data = loco
				print ('\nValores Anteriores: \n')
				print ('\tLocomotiva: ' + str(loco['locomotiva']))
				print ('\tDelay: ' + str(loco['delay']))
				print ('\tURL: ' + str(loco['url']))
				print ('\tOrigem: ' + str(loco['origem']))
				print ('\tStatus: ' + str(loco['status']))
			return True
		except OSError as err:
			logging.warning(now()+" OS error: {0}".format(err))
			print(now()+" OS error: {0}".format(err))
			return False
		
		
def alterarLocoDelay():
	L = int(raw_input("\nLocomotiva: "))
	while(not(L in locoHelper)):
		L = int(raw_input("\nLocomotiva Invalida, Digite novamnete : "))
	data['locomotiva'] = L
	data['delay'] = int(raw_input("\nDelay(segundos): "))
	alterarParametros()

def start():
	data['status'] = "start"
	alterarParametros()

def stop():
	data['status'] = "stop"
	alterarParametros()		

def alterarPendrive():
	data['origem'] = str(raw_input("\n1 Digite a Origem: "))
	alterarParametros()	

def alterarStatus():
	tipoStatus = ["1","2"] 
	print ('|> Opicoes de Status:')
	print ('\t1 - Start')
	print ('\t2 - Stop')
	L = str(raw_input("\n1 Digite a opcao de Status: "))
	while(not(L in tipoStatus)):
		L = str(raw_input("\nStatus Invalida, Digite a opcao de Status: "))
	if(L == "1"):
		start()
	if(L == "2"):
		stop()
	
def alterarURL():
	data['url'] = str(raw_input("\n1 Digite a URL: "))
	alterarParametros()	

def opcoesAlteracao():
	print ('\n|> Opcoes de Alteracao:')
	print ('\t1 - Alterar Locomotiva e Delay')
	print ('\t2 - Alterar Status')	
	print ('\t3 - Alterar URL')	
	print ('\t4 - Alterar Dir Origem')	
	x = str(raw_input("\nDigite a opcao desejada ?"))
	
	if(x == "1"):
		alterarLocoDelay()
	if(x == "2"):
		alterarStatus()
	if(x == "3"):
		alterarURL()
	if(x == "4"):
		alterarPendrive()
		
def alterarParametros():
	try:
		with io.open(parametros, 'w', encoding='utf8') as outfile:
			str_ = json.dumps(data,
							  indent=4, sort_keys=True,
							  separators=(',', ': '), ensure_ascii=False)
			outfile.write(to_unicode(str_))
			print ('\n|> Salvo com SUCESSO !!!\n')
	except OSError as err:
		print(" OS error: {0}".format(err))		