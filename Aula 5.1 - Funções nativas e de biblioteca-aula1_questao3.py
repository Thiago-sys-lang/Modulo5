import random

def adivinhar_numero():
    numero_aleatorio = random.randint(1, 10)
    
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
        if palpite < numero_aleatorio:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_aleatorio:
            print("Muito alto, tente novamente!")
        else:
            print("Correto! O número é", numero_aleatorio)
            break

adivinhar_numero()
