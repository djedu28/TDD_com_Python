from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):
        # LANCE EM ORDEM DECRESCENTE

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

    def test_quando_adicionados_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):
        # LANCE EM ORDEM CRESCENTE
        users = [
            Usuario('Edu'),
            Usuario('Karol')
        ]

        leilao = Leilao('Celular')

        leilao.lances.append(Lance(users[1], 150.0)) # LANCE da Karol
        leilao.lances.append(Lance(users[0], 100.0)) # LANCE de Edu


        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
