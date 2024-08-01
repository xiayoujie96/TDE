#2⋅π⋅raio(altura+raio) eh como calcula a area do cilindro
#entradas
lataValor=50
lataPinta=3
#processamento
alturaCilindro=float(input("Insira a altura do cilindro:"))
raioCilindro=float(input("Insira o raio do cilindro:"))
calculoAreaM2=2*3.1415*raioCilindro*(alturaCilindro+raioCilindro)
#saida
print("A area total do cilindro é de:",calculoAreaM2)
quantidadeLatas = calculoAreaM2/lataPinta
valorTotal = quantidadeLatas*lataValor
print("serao necessarias:", quantidadeLatas, "latas e isso custará:", valorTotal, "reais")
