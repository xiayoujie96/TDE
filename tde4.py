print("insira o valor de seu produto e calcularei ele a vista com 5% de desconto, em 2x e em 3x com 5% de juros")
produtoValor = int(input())
print("Preco a vista:", produtoValor*0.95)
print("Parcela em 2x sem juros:", produtoValor/2)
print("valor da parcela em 3x com juros de 5%", (produtoValor*1.05)/3)