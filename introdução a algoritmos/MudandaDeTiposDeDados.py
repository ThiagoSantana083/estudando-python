print("Texto (string - str) para inteiro no Python")
numero1 = 5
texto = "2"

textoParaInteiro = int(texto)
soma = numero1 + textoParaInteiro
print(type(soma))
print(soma)

print("Float para inteiro no Python")
numeroFloat = 20.5
floatParaInteiro = int(numeroFloat)
print(type(floatParaInteiro))
print(floatParaInteiro)

print("Float para texto")
numeroFloat2 = 20.67
floatParaTexto = str(numeroFloat2)
print(type(floatParaTexto))
print(floatParaTexto)

print("Texto para float")
textoFloat = "56.7"
textoParaFloat = float(textoFloat)
print(type(textoParaFloat))
print(textoParaFloat)