import random
while True:
    numero = random.randint(1,100)
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
    if primo:
        print("Numero primo generado:", numero)
        break