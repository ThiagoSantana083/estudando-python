idade = 18
usaSunga = False

if idade >= 18 and usaSunga:
    print("Maior de idade com sunga para a piscina")
elif idade < 18 and usaSunga:
    print("Menor de idade e não usa sunga")
elif idade >= 18 and not usaSunga:
    print("Maior de idade sem sunga - impossível entrar na piscina")
else:
    print("Erro ao saber dados")