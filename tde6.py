import math
#2⋅π⋅raio(altura+raio) eh como calcula a area do cilindro
#entradas
lataValor=50
lataPinta=3
alturaCilindro=float(input("Insira a altura do cilindro:"))
raioCilindro=float(input("Insira o raio do cilindro:"))
#processamento
calculoAreaM2=2*math.pi*raioCilindro*(alturaCilindro+raioCilindro)
quantidadeLatas = calculoAreaM2/lataPinta
valorTotal = quantidadeLatas*lataValor
num = calculoAreaM2
rounded_num = round(num, 3)
#saida
print("A area total do cilindro é de:",rounded_num)
print(f"serao necessarias: {quantidadeLatas:.2f}", f"latas e isso custará: {valorTotal:.2f} reais")
