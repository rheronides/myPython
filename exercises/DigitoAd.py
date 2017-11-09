x = int(input("Digite um número inteiro: "))
ad = False
#1223

while x != 0:
	a = x % 10
	x = x // 10
	b = x % 10

	if a == b:
		ad = True
if ad:
	print("sim")		
else:
	print("não")