import math

a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))

delta = ((b**2) - (4*a*c))

xP = 0
xN = 0
if delta == 0:
		xP = ((-b + math.sqrt(delta)) / (2 * a))
		print("a raiz desta equação é", xP)
else:
	if delta < 0:
		print("esta equação não possui raízes reais")
	else:
		xP = ((-b + math.sqrt(delta)) / (2 * a))
		xN = ((-b - math.sqrt(delta)) / (2 * a))
		
		if xP > xN:
			x = xN
			y = xP
			print("as raízes da equação são",x,"e", y)
		else:
			x = xP
			y = xN

			print("as raízes da equação são",x,"e", y)