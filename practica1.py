#! /usr/bin/python3

import webapp
import csv

class cut_url(webapp.webApp):
	
	dicc_url = {}
	dicc_short_url = {}
	m = 0
		
	def parse(self, request):

		recurso = request.split(' ',2)[1]
		num = recurso.split('/')[1]
		peticion = request.split()[0]
		
		print("Recurso: " + recurso)
		print("Peticion: " + peticion)
		print(num)
		real_url = None

		if peticion == 'POST':

			ultimaLinea = request.split()[-1]
			_, real_url = ultimaLinea.split('=')

			if 'http://' in real_url or 'https://' in real_url:
				real_url = real_url
			elif 'www.' in real_url:
				real_url = 'http://' + real_url
			else:
				real_url = 'http://' + real_url
			print(real_url)
		
		return(peticion, recurso, num, real_url)

	def process(self, resourceName):

		resourceName, requestName, num, url = resourceName
				
		if  resourceName == 'GET':

			if requestName == '/':
				httpCode = "200 OK"
				htmlBody = "<html><body><h4>Dame una url: <br></h4>"\
							 + "<form method = 'POST' action = ''>Contenido: <input type='text' name = 'Content'><br>\
							 <input type='submit' value='Enviar'></form></body></html>"
			else:
				if str(num) in self.dicc_short_url.keys():
					try:
						redirect = self.dicc_short_url[str(num)]
						print(redirect)
						httpCode = "301 Moved Permanently"
						htmlBody = "<html><body><meta http-equiv='refresh'content='0 url=" + redirect + "'>"+"</body></html>"
					except KeyError:
						httpCode = "404 Not found"
						htmlBody = "<html><body><h1>Not found. " + "<a href=http://localhost:1234/ >Click here</a></h1>"
				else:
					httpCode = "404 Not Found"
					htmlBody = "<html><body><h1>You aren't in the correct page. Please, click " \
							+ "<a href=http://localhost:1234/ >here</a></h1>"

		elif resourceName == 'POST':
			if url in self.dicc_url.keys():
				httpCode = "200 OK"
				htmlBody = "<p> Url encontrada</p>" + "<p> Url original:  <a href = '" + url + "'>" + url + "</a></p>"\
							+ "<p> Url acortada: <a href = '" + url + "'>" + self.dicc_url[url] + "</a></p>"\
							+ "<p> Lista de url's guardadas<p>" + str(self.dicc_url) + "<p>"\
							+ "<p><a href=http://localhost:1234/ >Click here to main page</a></p>"
			elif url:
				
				self.dicc_url[url] = str(self.m)
				self.dicc_short_url[str(self.m)] = url
				httpCode = "200 OK"
				htmlBody = "<p> Url:</p>" + "<p> Url original: <a href = '" + url + "'>" + url + "</a></p>"\
							+ "<p> Url acortada: <a href = '" + url + "'>" + self.dicc_url[url] + "</a></p>"\
							+ "<p> Lista de url's guardadas<p>" + str(self.dicc_url) + "<p>"\
							+ "<p><a href=http://localhost:1234/ >Click here to main page</a></p>"
				self.m = self.m + 1

			else:
				httpCode = "404 not found"
				htmlBody = "<html><body>Not Found</body></html>"

		return (httpCode, htmlBody)


if __name__ == "__main__":
	testWebApp = cut_url("localhost", 1234)
