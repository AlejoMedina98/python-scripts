import sys

if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 1 or numero > 9999:
		print("""
			Error - El numero es incorrecto
			Ejemplo: descomposicion.py [1 - 9999]
			""")
	else: 
		# Comienza la lógica
		cadena = str(numero)
		longitud = len(str(numero))

		for i in range(longitud):
			print("{:04d}".format(int(cadena[longitud-1-i]) *10**i)) # Operaciones matemáticas
else: 
	print("""
		Error - El Script debe recibir un argumento
		Ejemplo: descomposicion.py [1 - 9999]
		""")