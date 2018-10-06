class MiClaseEjemplo:
	""" Esto es un ejemplo
	Clases, objetos y metodos"""
	entero = 4321
	def mensaje(self, msj):
		print(msj)

# Instanciamos de la clase y asignamos el objeto a las variables
x = MiClaseEjemplo()
y = MiClaseEjemplo()

print(x.entero)
print(y.mensaje("Hola POO"))
