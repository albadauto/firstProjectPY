#PROGRAMA DE ADIVINHAÇÃO
#AUTOR: JOSÉ ADAUTO
import random as rand

numeros = []
cont = 1

while cont <= 100:
    numeros.append(cont)
    cont += 1

tentativa = int(input("Digite um numero "))
resposta = int(rand.choice(numeros))

while tentativa != resposta:
    if tentativa < resposta:
         tentativa = int(input("Poxa, tente um valor mais alto "))
    elif tentativa > resposta:
         tentativa = int(input("Poxa, tente um valor menor "))
    

if(tentativa == resposta):
    print("Parabens, voce acertou!: ", resposta)

