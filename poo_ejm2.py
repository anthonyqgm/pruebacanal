class MiPerro:
	"""Segundo ejemplo para el manejo y 
	comprension de clases, objetos
	y metodos. con metodos __init__"""
	def __init__(self):  #Metodo que se ejecuta al instanciar
		print("Todos somos objetos")

	def ladrar(self, ladrido):
		print(ladrido)

	def juego(self, juegar):
		print(juegar)	

	def proteger(self, cuidar):
		print(cuidar)	

#Instanciamos dos objetos de la clase miPerro
getrudis = MiPerro()
parker = MiPerro()

#Accedemos a los metodos
getrudis.ladrar("Guau gua me llamo getrudis")
parker.ladrar("Guau Guau yo me llamo parker Guay Hola!")