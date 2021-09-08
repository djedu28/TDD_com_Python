from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    #test_quando_..._deve_...

    def setUp(self):
        self.users = {
            "Edu":Usuario('Edu'),
        }
        self.lances = [
            ("Edu",100.0), # 1º LANCE de Edu
        ]

        self.leilao = Leilao('Celular')


    def AvaliarLances(self,leilao,lances):
        """Macro para avaliar Lances"""
        from operator import itemgetter

        [self.leilao.lances.append(Lance(user,lance)) for (user,lance) in lances]

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = min(lances, key = itemgetter(1))[1]
        maior_valor_esperado = max(lances, key = itemgetter(1))[1]
        # menor_valor_esperado = min(lances, key = lambda k: lances[k][1])
        # maior_valor_esperado = max(lances, key = lambda k: lances[k][1])

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):
        # LANCE EM ORDEM DECRESCENTE

        # Adiciona usuario Karol
        self.users['Karol'] = Usuario('Karol')
        # Adiciona 1º Lance de Karol
        self.lances.append(('Karol',150.0))

        # Avalia Lances
        self.AvaliarLances(self.leilao,self.lances)


    def test_quando_adicionados_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):
        # LANCE EM ORDEM CRESCENTE

        # Adiciona usuario Karol
        self.users['Karol'] = Usuario('Karol')
        # Adiciona 1º Lance de Karol
        self.lances.append(('Karol',150.0))

        self.lances.reverse() # invertendo a ordem

        # Avalia Lances
        self.AvaliarLances(self.leilao,self.lances)


    def test_quando_tiver_um_lance_deve_retornar_o_mesmo_valor_no_maior_e_menor_lance(self):
        # LANCE UNICO

        self.AvaliarLances(self.leilao,self.lances)


    def test_quando_o_leilao_tiver_tres_lances_deve_retornar_o_maior_e_o_menor_valor(self):
        # 3 LANCES, 2 USUARIOS

        # Adiciona usuario Karol
        self.users['Karol'] = Usuario('Karol')
        # Adiciona 1º Lance de Karol
        self.lances.append(('Karol',150.0))
        # Adiciona 2º Lance de Karol
        self.lances.append(('Karol',128.0))

        # Avalia Lances
        self.AvaliarLances(self.leilao,self.lances)


    # def test_quando_..._deve_...(self):
