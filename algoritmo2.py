'''
Crea un programa en Python que pida al usuario adivinar un número secreto (por ejemplo, 7).
El programa seguirá pidiendo al usuario que adivine hasta que acierte.
al cliente poner mensajes de el numero ingresado es mayor al adivinado 
sino el numero ingresado es menor al adivinado
limitarlo a una cierta cantidad de intentos

'''

numero_secreto = 10
# numero_secreto = random.randint(1, 10)
#numeroPorAdivinar = int(input("adivina el numero secreto ingresando (entre el 1 y el 10)"))
intentos = 0
max_intentos = 5

while True :
    numeroPorAdivinar = int(input("adivina el numero secreto ingresando (entre el 1 y el 10)"))
    if numeroPorAdivinar == numero_secreto :
        print("adivino")
        break
    else:
        if numeroPorAdivinar > numero_secreto :
            print("El número ingresado es mayor al número secreto ")
        else:
            print("El número ingresado es menor al número secreto. ")
    
        #print("no has acertado")
