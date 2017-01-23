# La librería sys importa componentes del sistema, para lo que lo usaremos será para ingresar datos como parametros en el interprete
# sys.argv de la librería sys, devuelve una lista de los argumentos que hemos pasado a la hora de correr el Script

import sys

print("Hola amigo")

if len(sys.argv) > 1 and len(sys.argv)< 3:
	print("Tu argumento ha sido: ", sys.argv[1])
elif len(sys.argv) > 2:
	print("Tus argumentos son: ")
	for i in range(len(sys.argv)):
		if i == 0:
			continue
		print(sys.argv[i])
else: 
	print("No has tenido argumentos...")

