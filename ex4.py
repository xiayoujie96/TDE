notas = input("Insira aqui suas 4 notas separas por um espaço: ")
notas = [int(x) for x in notas.split()]
media = sum(notas) / len (notas)
print(f"Sua média é {media:.2f}")

