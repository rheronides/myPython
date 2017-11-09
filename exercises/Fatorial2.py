def fatorial(x):
	j = x

	if x == 0:
		x = 1
	else:
		j = j - 1
		while (j != 0):
			x = x * j

			j = j - 1

	print(x)	
	return x

x = int(input("Digite o valor de n1:	"))
fatorial(x)
