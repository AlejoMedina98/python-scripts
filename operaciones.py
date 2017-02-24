#Este es un modulo que realiza cuatro operaciones: suma, resta, producto y division.

def suma(a,b):
	try:
		return(a+b)
	except TypeError:
		return "Error. Tipo de dato no valido"

def resta(a,b):
	try:
		return(a-b)
	except TypeError:
		return "Error. Tipo de dato no valido"

def producto(a,b):
	try:
		return(a*b)
	except TypeError:
		return "Error. Tipo de dato no valido"
def division(a,b):
	try:
		return(a/b)
	except TypeError:
		return "Error. Tipo de dato no valido"
	except ZeroDivisionError:
		return "No se puede dividir por cero."