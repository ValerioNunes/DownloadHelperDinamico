import os
import zipfile

Origem     = "/media/usb"
ArquivoZip = 'archive.7z'

def ZippArquivo(loco):
	
	try:
		Origem = loco['origem']
		fantasy_zip = zipfile.ZipFile(ArquivoZip, 'w')
		for folder, subfolders, files in os.walk(Origem):
			for file in files:
				if file.endswith('.TXT') or file.endswith('.txt'):
					fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), Origem), compress_type = zipfile.ZIP_DEFLATED)

		fantasy_zip.close()
		return True
	except Exception as err:
	    print(" OS error: {0}".format(err))
	return False


def getArquivoZip():
	return ArquivoZip
	
