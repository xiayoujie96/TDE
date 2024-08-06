massa = float(input('Insira aqui seu peso em KG: '))
altura = float(input('Insira aqui sua altura em metros: '))
imc = massa / altura ** 2
if 18.5 <= imc <= 25:
    print ('Seu imc está normal')
elif imc<18.5:
    massa_minima = 18.5 * altura ** 2
    print(f'Seu imc está abaixo do normal, você precisa ter {massa_minima:.2f} kg')
elif imc>24.9:
    massa_maxima = 24.9 * altura ** 2
    print(f'Seu imc está acima do normal, você precisa ter {massa_maxima:.2f} kg')


    '''
    massa = float(input('Insira aqui seu peso em KG: '))       #usei esse pra resolver tambem, mas o resultado tava dando muito output
altura = float(input('Insira aqui sua altura em metros:'))
imc = massa / altura ** 2
while  18.5<= imc <= 25:
    print('Seu IMC está dentro do peso normal')
    break
    
while imc <= 18.5: 
    massa += 1
    imc = massa / altura**2
    print (f'sua massa minima para estar dentro do imc normal é {massa}')
    
while imc >= 25:
    massa -= 1
    imc = massa / altura**2
    print (f'sua massa maxima para estar dentro do imc normal é {massa}')
    '''