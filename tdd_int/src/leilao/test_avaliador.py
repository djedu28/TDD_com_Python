from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    #test_quando_..._deve_...

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


    def test_quando_tiver_um_lance_deve_retornar_o_mesmo_valor_no_maior_e_menor_lance(self):
        # LANCE UNICO

        lance = 100.0

        users = [
            Usuario('Edu'),
        ]

        leilao = Leilao('Celular')

        leilao.lances.append(Lance(users[0], lance)) # LANCE de Edu


        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(lance, avaliador.menor_lance)
        self.assertEqual(lance, avaliador.menor_lance)


    def test_quando_o_leilao_tiver_tres_lances_deve_retornar_o_maior_e_o_menor_valor(self):
        # 3 LANCES, 2 USUARIOS

        users = [
            Usuario('Edu'),
            Usuario('Karol'),
        ]
        lances = [
            100.0,
            150.0,
            128.0,
        ]
        leilao = Leilao('Celular')

        leilao.lances.append(Lance(users[0], lances[0])) # LANCE de Edu
        leilao.lances.append(Lance(users[1], lances[1])) # LANCE da Karol
        leilao.lances.append(Lance(users[1], lances[2])) # LANCE da Carlos


        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = min(lances)
        maior_valor_esperado = max(lances)

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    # def test_quando_..._deve_...(self):
