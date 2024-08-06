#Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe “Valor inválido” para números negativos).

numero = int(input()) 
raiz = numero**0.5
if numero<0: print('Valor inválido')
else: print(raiz)