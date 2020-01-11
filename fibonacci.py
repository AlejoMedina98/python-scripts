num = int(input("¿Qué posición del fibonacci quieres?: "))

factorial = num
x = 0
y = 1
z = 1

for i in range(1, num+1):
    factorial = factorial * (num-i) if i != num else factorial
    
    if(i == 1 or i == 2):
        z = x if i == i else y
    else:
       z = x + y
       x = y
       y = z

print(f"La factorial de {num} es {factorial}")
print(f"El número en la pocición {num} de la serie fibonacci es {z}")