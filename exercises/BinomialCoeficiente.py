def fatorial(x):
	j = x

	if x == 0:
		x = 1
	else:
		j = j - 1
		while (j != 0):
			x = x * j

			j = j - 1

	# print(x)	
	return x

# import Fatorial2.py
# n!/ k!(n - k)!

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

x = fatorial(n)
y = fatorial(k)

bino = x / (x - y)

print("O coeficiente binomial é: ", bino)

120
___
120 - 2

