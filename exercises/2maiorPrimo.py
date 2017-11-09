def primo(x):
	i = j = f = 1
	while (i < x):
		
		while(j < i):
			print("J: ", j)
			if (i != 1 and  i % j == 0):
				f = i
			j = j + 1
		
		i = i + 1
		
	return f
x = 6

print(primo(x))