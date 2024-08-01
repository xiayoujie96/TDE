#2⋅π⋅raio(altura+raio) eh como calcula a area do cilindro
#entradas
lataValor=50
lataPinta=3
alturaCilindro=float(input("Insira a altura do cilindro:"))
raioCilindro=float(input("Insira o raio do cilindro:"))
#processamento
calculoAreaM2=2*3.1415*raioCilindro*(alturaCilindro+raioCilindro)
quantidadeLatas = calculoAreaM2/lataPinta
valorTotal = quantidadeLatas*lataValor
#saida
print("A area total do cilindro é de:",calculoAreaM2)
print("serao necessarias:", quantidadeLatas, "latas e isso custará:", valorTotal, "reais")
