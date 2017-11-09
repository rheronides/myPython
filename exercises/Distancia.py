import math

a = int(input("Digite o primeiro numero"))
b = int(input("Digite o segundo numero"))
c = int(input("Digite o terceiro numero"))
d = int(input("Digite o quarto numero"))

dAB = math.sqrt((a - c)**2 + (b - d)**2)

if dAB >= 10:
	print("longe")
else:
	print("perto")
