x = int(input("Digite um número inteiro: "))

i = 1
j = 1

while i < x:
	if x % i == 0:
		j = j + 1
	i = i + 1

if j > 1:
	print("primo")	
else:
	print("não primo")	