import requests
import json


def sendLog(loco, files):

		try:
			lvurl = (loco['url'] + "?loco=" + str(loco["locomotiva"]))
			r = requests.post(lvurl , files = files)
			return r.text
		except requests.exceptions.Timeout:
			return "requests.exceptions.Timeout:  Maybe set up for a retry, or continue in a retry loop"
		except requests.exceptions.TooManyRedirects:
			return "requests.exceptions.TooManyRedirects: Tell the user their URL was bad and try a different one"
		except requests.exceptions.RequestException as e:
			return "requests.exceptions.RequestException: catastrophic error. bail."
		except OSError as err:
			return "OS error: {0}".format(err)