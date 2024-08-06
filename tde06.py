def h_m():
    homem_mulher = str(input('Você é homem ou mulher?'))
    while homem_mulher not in ['homem',  'mulher']:
        homem_mulher = input('Você é homem ou mulher?')

    if homem_mulher.lower() == 'homem':
        alturaH = float(input('Insira a sua altura: '))
        p = (72.7 * alturaH) - 58 
        print (f'seu peso ideal é{p}')

    elif homem_mulher.lower() == 'mulher':
        alturaM = float(input('insira sua altura: '))
        pM = (62.1 * alturaM) - 44.7
        print(f'seu peso ideal é {pM}')
h_m() 

