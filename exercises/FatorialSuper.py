def fatorial(n):
	fat = 1
	while (n > 1):
		fat = fat * n
		n = n - 1
	return fat


def numero_binomial(j, k):
	return fatorial(j)/(fatorial(k) * fatorial(j - k))
