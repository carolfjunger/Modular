# -*- coding: utf-8 -*-
'''
    Nome: Teste
    Descriçao: Modulo responsavel por rodar os testes.
    Autores: 
        ACJ - Ana Carolina Junger
        AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               22/04/2020          criacao dos primeiros testes
        ACJ             2               23/04/2020          criacao dos testes para o módulo Rodada
        AB              3               25/04/2020          criacao dos testes para o modulo dado
        AB              4               25/04/2020          criacao dos primeiros testes para arremesso
        ACJ             5               26/04/2020          criacao dos testes para o modulo Cartela
        AB              6               26/04/2020          criacao testes para regrasDePontuacao com lista
        AB              7               26/04/2020          criacao testes para regrasDePontuacao com lista
        ACJ             8               27/04/2020          separacao dos testes em classes por modulos
        AB              9               27/04/2020          criacao testes para arremessa com casos de erro
        AB              10              28/04/2020          atualizacao de testes para regrasDePontuacao com dicionario
        ACJ             11              02/05/2020          criacao dos testes para funcao existe jogador
        ACJ             12              03/04/2020          criacao dos testes restantes
        
       
        
       


'''

import unittest
import Jogador
import Partida
import Rodada
import Cartela
import Dado
import Arremesso
import Dado
import RegrasDePontuacao

class JogadorTeste(unittest.TestCase):
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

    def testa_01_funcao_limpa_jogadores_modulo_jogador(self):
        print("Caso de Teste 01  Funcao Limpa Jogadores")
        retorno_esperado=True
        for i in range(100):
            Jogador.limpa_jogadores()
            if (Jogador.jogadores != []):
                retorno_esperado = False
                break
        self.assertEqual(retorno_esperado, True)

    def testa_01_funcao_pegaJogadorId_modulo_jogador(self):
        print("Caso de Teste 01  Funcao pegaJogadorId")
        retorno_esperado=True
        for i in range(100):
            Jogador.limpa_jogadores()
            Jogador.cria("Joao")
            jogadorId = Jogador.pegaJogadorId("Joao")
            if (jogadorId != 0 ):
                retorno_esperado = False
                break
        self.assertEqual(retorno_esperado, True)

    def testa_01_funcao_existe_modulo_jogador(self):
        print("Caso de Teste 01  Funcao Existe Jogador- Funcao retorna -1 caso o jogador nao exista ")
        Jogador.limpa_jogadores()
        retorno_esperado = Jogador.existe(25)
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_existe_modulo_jogador(self):
        print("Caso de Teste 02  Funcao Existe Jogador- Funcao retorna 1 caso o jogador  exista ")
        Jogador.limpa_jogadores()
        Jogador.cria("Pedro")
        jogadorId = Jogador.pegaJogadorId("Pedro")
        retorno_esperado = Jogador.existe(jogadorId)
        self.assertEqual(retorno_esperado, 1)
    
    def testa_01_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 01 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -1 caso o jogador Id nao exista")
        Jogador.limpa_jogadores()
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(0, 25)
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 02 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -2 caso o jogador Id nao seja um id")
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador("oi", 25)
        self.assertEqual(retorno_esperado, -2)

    def testa_03_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 03 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -3 caso a total de pontos nao seja um int")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(jogadorId, "oi")
        self.assertEqual(retorno_esperado, -3)

    def testa_04_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 04 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -4 caso a total de pontos seja menor que 0")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(jogadorId, -1)
        self.assertEqual(retorno_esperado, -4)
    

class PartidaTeste(unittest.TestCase):
    def teste_01_funcao_cria_modulo_partida(self):
        print("Caso de Teste 01 Funcao Cria Partida- Funcao retorna -1 caso array de jogadores tenha tamanho menor que 2")
        retorno_esperado = Partida.cria([])
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_partida(self):
        print("Caso de Teste 02 Funcao Cria Partida - Funcao retorna -1 caso jogadores nao seja um array")
        retorno_esperado = Partida.cria(1111)
        self.assertEqual(retorno_esperado, -2)

    def teste_01_funcao_limpa_partidas_modulo_partida(self):
        print("Caso de Teste 01 Funcao limpa_partidas")
        retorno_esperado=True
        for i in range(100):
            Jogador.limpa_jogadores()
            Jogador.cria("Joao")
            Jogador.cria("Pedro")
            Partida.cria(Jogador.jogadores)
            Partida.limpa_partidas()
            if (Partida.partidas != []):
                retorno_esperado = False
                break
        self.assertEqual(retorno_esperado, True)

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

    def teste_01_funcao_defineJogadorComMaiorPontuacao_modulo_partida(self):
        print("Caso de Teste 01 Funcao defineJogadorComMaiorPontuacao")
        retorno_esperado = Partida.defineJogadorComMaiorPontuacao([ { "id": 0, "nome": "Joao", "totalDePontos": 100}, { "id": 1, "nome": "Pedro", "totalDePontos": 200}])

        self.assertEqual(retorno_esperado, [{ "id": 1, "nome": "Pedro", "totalDePontos": 200}])

    def teste_02_funcao_defineJogadorComMaiorPontuacao_modulo_partida(self):
        print("Caso de Teste 02 Funcao defineJogadorComMaiorPontuacao")
        retorno_esperado = Partida.defineJogadorComMaiorPontuacao([ { "id": 0, "nome": "Joao", "totalDePontos": 200}, { "id": 1, "nome": "Pedro", "totalDePontos": 200}])

        self.assertEqual(retorno_esperado, [{ "id": 0, "nome": "Joao", "totalDePontos": 200}, { "id": 1, "nome": "Pedro", "totalDePontos": 200}])

    def teste_03_funcao_defineJogadorComMaiorPontuacao_modulo_partida(self):
        print("Caso de Teste 03 Funcao defineJogadorComMaiorPontuacao")
        retorno_esperado = Partida.defineJogadorComMaiorPontuacao([ { "id": 0, "nome": "Joao", "totalDePontos": 300}, { "id": 1, "nome": "Pedro", "totalDePontos": 200}])

        self.assertEqual(retorno_esperado, [{ "id": 0, "nome": "Joao", "totalDePontos": 300}])


class RodadaTeste(unittest.TestCase):
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

    def teste_01_funcao_limpa_rodadas_modulo_rodada(self):
        print("Caso de Teste 01 Funcao limpa_rodadas")
        retorno_esperado=True
        for i in range(100):
            Jogador.limpa_jogadores()
            Rodada.limpa_rodadas()
            Jogador.cria("Joao")
            jogador = Jogador.jogadores[0]
            Rodada.cria(jogador, 1)
            Rodada.limpa_rodadas()
            if (Rodada.rodadas != []):
                retorno_esperado = False
                break
        self.assertEqual(retorno_esperado, True)
    
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


class CartelaTeste(unittest.TestCase):
    def teste_01_funcao_cria_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Cria Cartela- Funcao retorna -1 caso nao receba um Id de jogador como parametro")
        retorno_esperado = Cartela.cria("")
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_cartela(self):
        print("Caso de Teste 02 Funcao Cria Cartela- Funcao retorna -2 caso nao o Id nao seja vinculado a nenhum jogador existente")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        retorno_esperado = Cartela.cria(50)
        self.assertEqual(retorno_esperado, -2)

    def teste_03_funcao_cria_modulo_cartela(self):
        print("Caso de Teste 03 Funcao Cria Cartela- Funcao retorna -3 caso o jogador exista e ja possua uma cartela")
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        Cartela.cria(0)
        retorno_esperado = Cartela.cria(0)
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_cria_modulo_cartela(self):
        print("Caso de Teste 04 Funcao Cria Cartela- Funcao retorna 1 caso o jogador exista e ja nao possua uma cartela")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        retorno_esperado = Cartela.cria(0)
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_limpa_cartelas_modulo_cartela(self):
        print("Caso de Teste 01 Funcao limpa_cartelas")
        retorno_esperado=True
        for i in range(100):
            Jogador.limpa_jogadores()
            Cartela.limpa_cartelas()
            Jogador.cria("Joao")
            retorno_esperado = Cartela.cria(0)
            Cartela.limpa_cartelas()
            if (Cartela.cartelas != []):
                retorno_esperado = False
                break
        self.assertEqual(retorno_esperado, True)

    def teste_01_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Preenche Cartela- Funcao retorna -1 caso nao receba um Id de jogador como parametro")
        retorno_esperado = Cartela.preenche("", "somaDeUm", 1)
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 02 Funcao Preenche Cartela- Funcao retorna -2 caso o Id de jogador nao esteja vinculado a nenhuma cartela")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        retorno_esperado = Cartela.preenche(50,"somaDeUm", 1)
        self.assertEqual(retorno_esperado, -2)

    def teste_03_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 03 Funcao Preenche Cartela- Funcao retorna -3 caso a posicao na cartela nao seja uma string")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.preenche(jogadorId, 0, 1)
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 04 Funcao Preenche Cartela- Funcao retorna -4 caso a posicao na cartela nao exista")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.preenche(jogadorId, "somaDeSete", 1)
        self.assertEqual(retorno_esperado, -4)

    def teste_05_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 05 Funcao Preenche Cartela- Funcao retorna -5 caso os pontos nao sejam um inteiro")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.preenche(jogadorId, "jogadaDeUm", "oi")
        self.assertEqual(retorno_esperado, -5)

    def teste_06_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 06 Funcao Preenche Cartela- Funcao retorna -6 caso os pontos sejam um inteiro menor que zero")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.preenche(jogadorId, "jogadaDeUm", -1)
        self.assertEqual(retorno_esperado, -6)

    def teste_07_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 07 Funcao Preenche Cartela- Funcao retorna 1 caso a pontuacao tenha sido preenchidaa com sucesso")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.preenche(jogadorId, "jogadaDeUm", 1)
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Soma Pontuacao Cartela- Funcao retorna -1 caso nao receba um Id de jogador como parametro")
        retorno_esperado = Cartela.somaPontuacao("")
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 02 Funcao Soma Pontuacao Cartela- Funcao retorna -2 caso o Id de jogador nao esteja vinculado a nenhuma cartela")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.somaPontuacao(50)
        self.assertEqual(retorno_esperado, -2)

    def teste_03_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 03 Funcao Soma Pontuacao Cartela- Funcao retorna -3 caso de algum erro na funcao vinculaPontuacao")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        retorno_esperado = Cartela.somaPontuacao(jogadorId)
        self.assertEqual(retorno_esperado, -3)
    
    def teste_04_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 04 Funcao Soma Pontuacao Cartela- Funcao retorna 1 caso pontuacao tenha sido somada com sucesso")
        Jogador.limpa_jogadores()
        Cartela.limpa_cartelas()
        Jogador.cria("Joao")
        jogadorId = Jogador.pegaJogadorId("Joao")
        Cartela.cria(jogadorId)
        Cartela.preenche(jogadorId, "jogadaDeUm", 1)
        Cartela.preenche(jogadorId, "jogadaDeDois", 2)
        Cartela.preenche(jogadorId, "jogadaDeTres", 3)
        Cartela.preenche(jogadorId, "jogadaDeQuatro", 4)
        Cartela.preenche(jogadorId, "jogadaDeCinco", 5)
        Cartela.preenche(jogadorId, "jogadaDeSeis", 6)
        Cartela.preenche(jogadorId, "trinca", 3)
        Cartela.preenche(jogadorId, "quadra", 4)
        Cartela.preenche(jogadorId, "fullHouse", 25)
        Cartela.preenche(jogadorId, "sequenciaAlta", 30)
        Cartela.preenche(jogadorId, "sequenciaBaixa", 40)
        Cartela.preenche(jogadorId, "general", 50)
        Cartela.preenche(jogadorId, "jogadaAleatoria", 30)
        retorno_esperado = Cartela.somaPontuacao(jogadorId)
        self.assertEqual(retorno_esperado, 1)


class ArremessoTeste (unittest.TestCase):
    
    def teste01(self):
        print("Caso de Teste 01 Funcao arremessa - Funcao retorna -2 caso já tenham sido escolhido todos os cinco dados que o jogador quer manter")
        Arremesso.limpa_arremesso()
        retorno_esperado = Arremesso.arremessa([1,2,3,4,5])
        
        self.assertEqual(retorno_esperado, -2)
        
    def teste02(self):
        print("Caso de Teste 02 Funcao arremessa - Funcao retorna -1 caso já tenha chegado ao número limite de arremessos")
        Arremesso.limpa_arremesso()
        Arremesso.arremessa([])
        Arremesso.arremessa([1])
        Arremesso.arremessa([1,2,3])
        
        retorno_esperado = Arremesso.arremessa([1,2,3,4])
        
        self.assertEqual(retorno_esperado, -1)
        
    def teste03(self):
        print("Caso de Teste 03 Funcao arremessa - Funcao retorna uma lista com 5 inteiros, testa se a lista tem 5 itens")
        Arremesso.limpa_arremesso()
        retorno_esperado = Arremesso.arremessa([])

        self.assertEqual(len(retorno_esperado), 5)

    def teste04(self):
        print("Caso de Teste 04 Funcao arremessa - Funcao retorna uma lista com 5 inteiros, testa se todos itens da lista sao inteiros")
        Arremesso.limpa_arremesso()
        retorno_esperado = Arremesso.arremessa([])
        
        self.assertEqual(all(isinstance(n, int) for n in retorno_esperado), True)
        
        
    def teste05(self):
        print("Caso de Teste 05 Funcao escolhe_dados - Funcao retorna 0 caso o valor escolhido não tenha caido em algum dos dados do arremesso")
        Arremesso.limpa_arremesso()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados
        
        self.assertEqual(Arremesso.escolhe_dados([3,3,3]),0)
        
    def teste06(self):
        print("Caso de Teste 06 Funcao escolhe_dados - Funcao retorna 1 caso tenha guardado os valores dos dados selecionados pelo usuário")
        Arremesso.limpa_arremesso()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados        

        self.assertEqual(Arremesso.escolhe_dados([3,1,5]) ,1)
   

class DadoTeste (unittest.TestCase):

    def teste01 (self):       
        print("Caso de Teste 01 Funcao jogaDado - Funcao retorna True caso todos os 100 numeros sejam de 1 a 6 ou False caso tenha algum número fora desse intervalo")
        retorno_esperado = True
        
        for i in range(0,100):
            resultado = Dado.jogaDado()
            
            if(resultado<1 or resultado>6):
                retorno_esperado = False
            
        self.assertEqual(retorno_esperado, True)
        


class RegrasDePontuacaoTeste(unittest.TestCase):
    
    def transformaEmDicionario (self, lPontuacao):
        DicPosicoes = {'jogadaDeUm': 0, 'jogadaDeDois' : 0, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 0}
        
        i = 0
        for posicao in DicPosicoes:
            DicPosicoes[posicao] = lPontuacao[i]
            i+=1
            
        return DicPosicoes
    
    def teste01(self):
        print("Caso de Teste 01 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        retorno_esperado = RegrasDePontuacao.geraPontuacoes([1,3,1,2,1])
        self.assertEqual(retorno_esperado, {'jogadaDeUm': 3, 'jogadaDeDois' : 2, 'jogadaDeTres': 3, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 8, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 8})
        
    def teste02(self):
        print("Caso de Teste 02 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([2,3,1,2,1]), {'jogadaDeUm': 2, 'jogadaDeDois' : 4, 'jogadaDeTres': 3, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 9})
        
    def teste03(self):
        print("Caso de Teste 03 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([2,3,1,2,1]), {'jogadaDeUm': 2, 'jogadaDeDois' : 4, 'jogadaDeTres': 3, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 9} )
        
    def teste04(self):
        print("Caso de Teste 04 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,1,2,4]), {'jogadaDeUm': 2, 'jogadaDeDois' : 2, 'jogadaDeTres': 3, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 11})
    
    def teste05(self):
        print("Caso de Teste 05 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([4,5,1,2,6]), {'jogadaDeUm': 1, 'jogadaDeDois' : 2, 'jogadaDeTres': 0, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 5, 'jogadaDeSeis': 6, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 18})
        
    def teste06(self):
        print("Caso de Teste 06 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([4,5,6,2,6]), {'jogadaDeUm': 0, 'jogadaDeDois' : 2, 'jogadaDeTres': 0, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 5, 'jogadaDeSeis': 12, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 23})
        
    def teste07(self):
        print("Caso de Teste 07 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,5,6,2,6]), {'jogadaDeUm': 0, 'jogadaDeDois' : 2, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 5, 'jogadaDeSeis': 18, 'trinca': 25, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 25})
        
    def teste08(self):
        print("Caso de Teste 08 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,6,6,2,6]), {'jogadaDeUm': 0, 'jogadaDeDois' : 2, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 24, 'trinca': 26, 'quadra': 26, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 26})
        
    def teste09(self):
        print("Caso de Teste 09 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,6,2,2,6]), {'jogadaDeUm': 0, 'jogadaDeDois' : 4, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 18, 'trinca': 22, 'quadra': 0, 'fullHouse': 25, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 22})
    
    def teste10(self):
        print("Caso de Teste 10 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([3,2,4,6,5]), {'jogadaDeUm': 0, 'jogadaDeDois' : 2, 'jogadaDeTres': 3, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 5, 'jogadaDeSeis': 6, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 30, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 20})
        
    def teste11(self):
        print("Caso de Teste 11 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,2,5,4]), {'jogadaDeUm': 1, 'jogadaDeDois' : 2, 'jogadaDeTres': 3, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 5, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 40, 'general': 0, 'jogadaAleatoria': 15})
        
    def teste12(self):
        print("Caso de Teste 12 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,1,1,1,1]), {'jogadaDeUm': 5, 'jogadaDeDois' : 0, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 5, 'quadra': 5, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 50, 'jogadaAleatoria': 5})
        
    def teste13(self):
        print("Caso de Teste 13 Funcao geraPontuacoes - Funcao retorna um dicionário com os valores calculados corretos para a lista passada")
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,2,3,4,5]), {'jogadaDeUm': 1, 'jogadaDeDois' : 2, 'jogadaDeTres': 3, 'jogadaDeQuatro': 4, 'jogadaDeCinco': 5, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 40, 'general': 0, 'jogadaAleatoria': 15}
)
