#Script encargado de bajar imagenes de LoremPixel

from urllib.request import urlopen
import os

url = "http://lorempixel.com"
cathegories = ["abstract", "animals", "business","cats","city","food","nightlife","fashion","people","nature","sports","technics","transport"]

#Comprobar que los valores son correctos por medio de un While

while(True):
	os.system("cls")
	print("\n")
	ancho = input("¿Ancho de la imagen?")
	alto = input("¿Alto de la imagen?")
	if ancho.isdigit() and alto.isdigit():
		break
	else:
		print("Los valores deberán de ser digitos")
		input("Continuar...")


#Comprobar categoria existente
while(True):
	print("\n¿Categoría?\n")
	for c in cathegories:
		print(c)
	print("\n")
	categoria = input()
	if categoria in cathegories:
		break
	else:
		os.system("cls")
		print("\nCategoría incorrecta, selecciona y escribe una de la lista")

#texto en la imagen
while(True):
	text = input("¿Quieres un texto en la imagen [S/N]?")
	if text == 's' or text == 'S':
		texto = input("Escribe el texto: ")
		break
	elif text == 'n' or text == 'N':
		print("¡No pasa nada :)!")
		break
	else:
		os.sistem("cls")
		print("\nOpcion no valida, intenta de nuevo.")

try:
	url = "http://lorempixel.com/{}/{}/{}/{}".format(ancho, alto,categoria,texto)
except:
	url = "http://lorempixel.com/{}/{}/{}".format(ancho, alto, categoria)


r = urlopen(url)
lectura = r.read()

imagen = open("imagen.jpeg", "wb")
imagen.write(lectura)
imagen.close()

print("\nLa imagen ha sido guardada con éxito.")
input("Pulsa una tecla para salir...")


