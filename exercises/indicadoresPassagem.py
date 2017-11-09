x = input("Digite o numero: ")
opa = 0
igual = False
j = len(x)

while j > 0 and igual == False:
	print(j)
	aux = opa

	opa = int(x) % 10
	
	if aux == opa:
		igual = True
		print("aux: ", aux, "opa: ", opa)
	j = j - 1

if igual:
	print("Há valores iguais em sequencia! =)")
else:
	print("Não há valores iguais em sequencia! =(")	