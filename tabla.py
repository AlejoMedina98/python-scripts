import sys

if len(sys.argv)== 3:
	filas = int(sys.argv[1])
	columas = int(sys.argv[2])

	if filas <1 or filas > 9 or columas <1 or columas > 9:
		print("Error -- Llama al script con dos argumentos.")
		print("tabla.py [No. de filas] [No. de columnas]")
	else: 
		# Aquí empieza la lógica
		for i in range(filas):
			for e in range(columas):
				print(" * ", end="")
			print("\n")
else: 
	print("Error -- Llama al script con dos argumentos.")
	print("tabla.py [No. de filas] [No. de columnas]")