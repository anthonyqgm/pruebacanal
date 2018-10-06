class CasaStark:  #Super-clase/clase base
	"""Personajes de Games Of Thrones
		Casa Stark"""
	print("Hijos de Eddard Stark y Lady Catelyn")
	def __init__(self, apellido_stark):	
		self.apellido_stark = apellido_stark

class CasaTargaryen: # Super-clase/clase base
	"""Personaje de Games Of Thrones
	Casa Targaryen"""
	print("Hijos de Aerys - El rey loco")
	def __init__(self, apellido_targaryen):
		self.apellido_targaryen = apellido_targaryen
		

class HerederoStark(CasaStark):  # Sub-clase \ Clase derivada
	"""Sub-clase que hereda de la clase CasaStark"""
	def nombre(self, nombre, apellido_stark):
		print("Mi nombre es ", nombre, " Heredero de la casa ", apellido_stark)


class HerederoTargaryen(CasaTargaryen): #Sub-clase \Clase derivada

	"""sub-clase que hereda de la clase CasaTargaryen"""
	def nombre_t(self, nombre_t, apellido_targaryen):
		print("Mi nombre es ", nombre_t, "Heredero de la casa ", apellido_targaryen)

# Instancimos objetos de la clase deribada HerederoStark
robb = HerederoStark("Stark")
sansa = HerederoStark("Stark")
arya = HerederoStark("Stark")
bran = HerederoStark("Stark")
rickon = HerederoStark("Stark")
# Accedemos a metodos y atributos (objeto.metodo)
print(robb.nombre("robb ", robb.apellido_stark))
print(sansa.nombre("sansa ", sansa.apellido_stark))
print(arya.nombre("arya ", arya.apellido_stark))
print(bran.nombre("bran ", bran.apellido_stark))
print(rickon.nombre("rickon ", rickon.apellido_stark))

#Instanciamos objetos de la clase derivada HerederoTargaryen
daenerys = HerederoTargaryen("Targaryen")
viserys = HerederoTargaryen("Targaryen")

print(daenerys.nombre_t("Daenerys ", daenerys.apellido_targaryen))
print(viserys.nombre_t("Viserys ", viserys.apellido_targaryen))
