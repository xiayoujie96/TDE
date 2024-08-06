#determinar valor minimo hora
#determinar o valor fracional e usar if else pra ir somando os minutos
#ler a quantidade de minutos e relacionar a valor minimo ou valor fracional.
import math
valor_minimo = 8.00
minutos = int(input('Insira a minutagem do cliente: '))


if minutos <= 60:
    print('O valor a ser pago é o mínimo, 8,00 reais')
else: 
    tempo_corrido = minutos - 60
tempo_cobrado = tempo_corrido // 15 + (1 if tempo_corrido % 15 != 0 else 0)
valor_final = valor_minimo + (tempo_cobrado * 1.5)      
print (valor_final)
    
