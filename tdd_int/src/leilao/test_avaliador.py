from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avalia(self):

        users = [
            Usuario('Edu'),
            Usuario('Karol')
        ]

        leilao = Leilao('Celular')

        leilao.lances.append(Lance(users[0], 100.0)) # LANCE de Edu
        leilao.lances.append(Lance(users[1], 150.0)) # LANCE da Karol


        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
