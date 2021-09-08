from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

users = [
    Usuario('Edu'),
    Usuario('Karol')
]

leilao = Leilao('Celular')

leilao.lances.append(Lance(users[0], 100.0)) # LANCE de Edu
leilao.lances.append(Lance(users[1], 150.0)) # LANCE da Karol


print("\n")
for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de R$ {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de R$ {avaliador.menor_lance} e o maior lance foi de R$ {avaliador.maior_lance}')
print("\n")
