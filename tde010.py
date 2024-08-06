'''
O IMC, índice de massa corporal, é calculado através da seguinte fórmula: IMC = massa /
altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
usuário e mostre o valor do IMC e qual sua condição segundo o critério apresentado na
tabela da OMS (Organização Mundial de Saúde)
18.5abaixo
18.5-25normal
25-30acima
30+obeso
'''
massa = float(input())
altura = float(input())
imc = massa / altura**2
if imc < 18.5:  print('Você está abaixo do peso')
elif imc <= 25:  print('Você está no peso normal')
elif imc <= 30:  print('Você está acima do peso')
else: 
    print('Você está obeso')
    print(f'Seu IMC é {imc}')