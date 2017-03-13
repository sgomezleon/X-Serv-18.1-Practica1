#! /usr/bin/python3

import webapp

class cut_url(webapp.webApp):
	
	dicc_url = {}
	m = 0

	def parse(self, request):

		recurso = request.split(' ', 2)[1]
		peticion = request.split()[0]
		print("Recurso: " + recurso)
		print("Peticion: " + peticion)
		real_url = None

		if peticion == 'POST':
			ultimaLinea = request.split()[-1]
			_, real_url = ultimaLinea.split('=')
			print(recurso)
			print(real_url)
			if 'http://' in real_url or 'https://' in real_url:
				real_url = real_url
			elif 'www.' in real_url:
				real_url = 'http://' + real_url
			else:
				real_url = 'http://www.' + real_url
			print(real_url)
		
		return(peticion, recurso,real_url)

	def process(self, resourceName):

		print(self.dicc_url)
		resourceName, requestName, url = resourceName
				
		if  resourceName == 'GET':

			if requestName == '/':
				httpCode = "200 OK"
				htmlBody = "<html><body><h4>Dame una url: <br></h4>"\
							 + "<form method = 'POST' action = ''>Contenido: <input type='text' name = 'Content'><br>\
							 <input type='submit' value='Enviar'></form></body></html>"

			else:
				httpCode = "404 Not Found"
				htmlBody = "<html><body><h1>You aren't in te correct page. Please, click " \
							+ "<a href=http://localhost:1234/ >here</a></h1>"

		elif resourceName == 'POST':
			if url in self.dicc_url.keys():
				httpCode = "200 OK"
				htmlBody = "<p> Url encontrada</p>" + "<p> Url original:  <a href = '" + url + "'>" + url + "</a></p>"\
							+ "<p> Url acortada: <a href = '" + self.dicc_url[url] + "'>" + self.dicc_url[url] + "</a></p>"\
							+ "<p> Lista de url's guardadas<p>" + self.dicc_url + "<p>"\
							+ "<p><a href=http://localhost:1234/ >Click here to main page</a></p>"
			elif url:
				
				print(self.dicc_url)

				self.dicc_url[url] = str(self.m)
				httpCode = "200 OK"
				htmlBody = "<p> Url:</p>" + "<p> Url original: <a href = '" + url + "'>" + url + "</a></p>"\
							+ "<p> Url acortada: <a href = '" + self.dicc_url[url] + "'>" + self.dicc_url[url] + "</a></p>"\
							+ "<p> Lista de url's guardadas<p>" + str(self.dicc_url) + "<p>"\
							+ "<p><a href=http://localhost:1234/ >Click here to main page</a></p>"
				self.m = self.m + 1
			else:
				httpCode = "404 not found"
				htmlBody = "<html><body>Not Found</body></html>"

		return (httpCode, htmlBody)


if __name__ == "__main__":
	testWebApp = cut_url("localhost", 1234)
