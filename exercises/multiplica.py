x = int(input("Digite um número inteiro: "))
# 112
a = 1
while x != 0:
 	a = a * (x % 10)
 	x = x // 10
 	
 	
print(a)  	