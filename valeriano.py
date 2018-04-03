import json
import io
import os


try:
    to_unicode = unicode
except NameError:
    to_unicode = str

os.system('cls' if os.name == 'nt' else 'clear')	
try:
	with open('C:\\Users\\valerio\\Documents\\Projetos\\Python\\DownloadHelperDinamico\\parametros.json') as f:    
		loco = json.load(f)
		print ('\nValores atuais: \n')
		print ('\tLocomotiva: ' + str(loco['locomotiva']))
		print ('\tDelay: ' + str(loco['delay']))
except OSError as err:
	print(now()+" OS error: {0}".format(err))	
	
	
# Define data
data = {
		"locomotiva": 852,
		"delay": 1 
		}

# Write JSON file

def alterarParametros():
	try:
		with io.open('C:\\Users\\valerio\\Documents\\Projetos\\Python\\DownloadHelperDinamico\\parametros.json', 'w', encoding='utf8') as outfile:
			str_ = json.dumps(data,
							  indent=4, sort_keys=True,
							  separators=(',', ': '), ensure_ascii=False)
			outfile.write(to_unicode(str_))
			print ('> Salvo com SUCESSO !!!\n')
	except OSError as err:
		print(now()+" OS error: {0}".format(err))		


x = str(raw_input("\nDeseja alterar parametros (sim/nao) ?"))

if(x.upper() == "SIM"):
	data['locomotiva'] = int(raw_input("\nLocomotiva: "))
	data['delay'] = int(raw_input("\nDelay(segundos): "))
	alterarParametros()

