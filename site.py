from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi
import json
import io
import os
import time




parametros = 'parametros.json'
locoHelper = [9020,823,829,832,824,818,9012,857,813,9012,814]

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

def openParametros():
	if(existeArq(parametros)):
	
		global data
		try:
			with open(parametros) as f:    
				loco = json.load(f)
				data = loco
			return True
		except OSError as err:
			return False
def alterarLoco(n):
	L = int(n)
	while(not(L in locoHelper)):
		L = int(raw_input("\nLocomotiva Invalida, Digite novamnete : "))
	data['locomotiva'] = L
	alterarParametros()

def alterarParametros():
	try:
		with io.open(parametros, 'w', encoding='utf8') as outfile:
			str_ = json.dumps(data,
							  indent=4, sort_keys=True,
							  separators=(',', ': '), ensure_ascii=False)
			outfile.write(to_unicode(str_))
			print ('\n|> Salvo com SUCESSO !!!\n')
			return True
	except OSError as err:
		print(" OS error: {0}".format(err))	
		return False
	
	
	
class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
		
    def do_GET(self):
		self._set_headers()
		print self.path
		print parse_qs(self.path[2:])
		self.wfile.write('''<html>
								<body>
									<form action="" method="post">
									  Numero da Locomotiva: <input type="number" name="loco"><br>
									  <input type="submit" value="Salvar">
									</form>
								</body>
							</html>''')
		return 
		
    def do_POST(self):
		self._set_headers()
		form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD': 'POST'})
		loco = form.getvalue("loco")
		alterarLoco(loco)
		self.wfile.write("<html><body><h1>LOCO: " + form.getvalue("loco") + "!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8088...'
    httpd.serve_forever()

def IniciarSite(threadName):
	print(threadName)

openParametros()
run()
