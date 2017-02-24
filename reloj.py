#Ejecuta este pequeño script en la terminal y tendrás un hermoso reloj... :3 
import datetime
import time
import os

while(True):
	dt = datetime.datetime.now()
	os.system('cls')
	print(dt.strftime("%I:%M:%S"))
	time.sleep(1)