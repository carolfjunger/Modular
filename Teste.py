# -*- coding: utf-8 -*-
import unittest
import Jogador
import Partida
import Rodada

class VerificarPangramaTests(unittest.TestCase):
    def testa_01_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 01 Funcao Cria Jogador - Funcao retorna -1 caso o nome seja uma string vazia")
        retorno_esperado = Jogador.cria("")
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 02 Funcao Cria Jogador - Funcao retorna -2 caso o nome nao seja uma string")
        retorno_esperado = Jogador.cria(1223)
        self.assertEqual(retorno_esperado, -2)

    def testa_03_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 03 Funcao Cria Jogador - Funcao retorna -3 caso ja exista um jogador com esse nome")
        Jogador.cria("Joao")
        retorno_esperado = Jogador.cria("Joao")
        self.assertEqual(retorno_esperado, -3)

    def testa_04_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 04  Funcao Cria Jogador- Funcao retorna 1 caso o jogador tem sido criado ")
        retorno_esperado = Jogador.cria("Pedro")
        self.assertEqual(retorno_esperado, 1)
    
    def teste_01_funcao_cria_modulo_partida(self):
        print("Caso de Teste 01 Funcao Cria Partida- Funcao retorna -1 caso array de jogadores tenha tamanho menor que 2")
        retorno_esperado = Partida.cria([])
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_partida(self):
        print("Caso de Teste 02 Funcao Cria Partida - Funcao retorna -1 caso jogadores nao seja um array")
        retorno_esperado = Partida.cria(1111)
        self.assertEqual(retorno_esperado, -2)

    def teste_03_funcao_cria_modulo_partida(self):
        print("Caso de Teste 03 Funcao Cria Partida - Funcao retorna -2 caso ja tenha uma partida ativa")
        Jogador.limpa_jogadores()
        Partida.limpa_partidas()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        Partida.cria(Jogador.jogadores)
        retorno_esperado = Partida.cria(Jogador.jogadores)
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_cria_modulo_partida(self):
        print("Caso de Teste 04 Funcao Cria Partida - Funcao retorna 1 caso Partida seja criada com os jogadores")
        Jogador.limpa_jogadores()
        Partida.limpa_partidas()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        retorno_esperado = Partida.cria(Jogador.jogadores)
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_finaliza_modulo_partida(self):
        print("Caso de Teste 01 Funcao Finaliza Partida- Funcao retorna -1 caso nao tenha partidas ativas")
        Partida.limpa_partidas()
        retorno_esperado = Partida.finaliza()
        self.assertEqual(retorno_esperado, -1)
    
    def teste_02_funcao_finaliza_modulo_partida(self):
        print("Caso de Teste 02 Funcao Finaliza Partida - Funcao retorna 1 caso tenha finalizado a partida")
        Partida.limpa_partidas()
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        Partida.cria(Jogador.jogadores)
        retorno_esperado = Partida.finaliza()
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 01 Funcao Cria Rodada- Funcao retorna -1 caso nao receba jogador")
        retorno_esperado = Rodada.cria(12234, 1)
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 02 Funcao Cria Rodada- Funcao retorna -2 caso o dicionario nao represente um jogador")
        retorno_esperado = Rodada.cria({}, 1)
        self.assertEqual(retorno_esperado, -2)

    def teste_03_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 03 Funcao Cria Rodada- Funcao retorna -3 caso o numero da rodada nao seja um numero")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        jogador = Jogador.jogadores[0]
        retorno_esperado = Rodada.cria(jogador, "oi")
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 04 Funcao Cria Rodada- Funcao retorna -4 caso o numero da rodada seja menor que 1")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        jogador = Jogador.jogadores[0]
        retorno_esperado = Rodada.cria(jogador, 0)
        self.assertEqual(retorno_esperado, -4)

    def teste_05_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 05 Funcao Cria Rodada- Funcao retorna -5 caso o numero da rodada seja maior que 13")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        jogador = Jogador.jogadores[0]
        retorno_esperado = Rodada.cria(jogador, 25)
        self.assertEqual(retorno_esperado, -5)

    def teste_06_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 06 Funcao Cria Rodada- Funcao retorna -6 caso ja exista uma rodada ativa")
        Jogador.limpa_jogadores()
        Rodada.limpa_rodadas()
        Jogador.cria("Joao")
        jogador = Jogador.jogadores[0]
        Rodada.cria(jogador, 1)
        retorno_esperado = Rodada.cria(jogador, 2)
        self.assertEqual(retorno_esperado, -6)

    def teste_07_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 07 Funcao Cria Rodada- Funcao retorna 1 caso a rodada tenha sido criada com sucesso")
        Jogador.limpa_jogadores()
        Rodada.limpa_rodadas()
        Jogador.cria("Joao")
        jogador = Jogador.jogadores[0]
        retorno_esperado = Rodada.cria(jogador, 1)
        self.assertEqual(retorno_esperado, 1)
    
    def teste_01_funcao_finaliza_modulo_rodada(self):
        print("Caso de Teste 01 Funcao Finaliza Rodada- Funcao retorna -1 caso nao tenha rodadas ativas")
        Rodada.limpa_rodadas()
        retorno_esperado = Rodada.finaliza()
        self.assertEqual(retorno_esperado, -1)
    
    def teste_02_funcao_finaliza_modulo_rodada(self):
        print("Caso de Teste 02 Funcao Finaliza Rodada - Funcao retorna 1 caso tenha finalizado a rodada ativa")
        Rodada.limpa_rodadas()
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        jogador = Jogador.jogadores[0]
        Rodada.cria(jogador, 1)
        retorno_esperado = Rodada.finaliza()
        self.assertEqual(retorno_esperado, 1)

