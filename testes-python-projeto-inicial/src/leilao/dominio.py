
class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances


class Avaliador:

    def __init__(self):
        from math import inf # Importando infinito da biblioteca math
        self.maior_lance = inf # Maior lance possivel é Infinito
        self.menor_lance = 0   # Menor lance possivel é Zero
