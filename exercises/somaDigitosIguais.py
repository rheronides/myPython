x = int(input("Digite um n: "))
contr = False
a = 0
while x != 0:
	a = a + x % 10
	x = x // 10
print(a)