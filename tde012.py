kg = float(input('insira seu peso em kg: '))
libra = 2.20 * kg
if 161 <= libra <=168: print ('Super-médio')
elif 169 <= libra <=175: print ('Meio-pesado')
elif 176 <= libra <= 200: print ('Cruzador')
elif libra > 200: print('Peso-pesado')
else: print('Categoria inferior a Super-médio')