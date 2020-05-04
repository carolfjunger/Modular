# -*- coding: utf-8 -*-
import unittest
import Jogador
import Partida
import Rodada
import Cartela
import Dado
import Arremesso
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


class DadoTeste (unittest.TestCase):
    def teste_01_funcao_jogaDado_modulo_Dado (self): 
        #print("Caso de Teste 01 Funcao jogaDado - Funcao )
        retorno_esperado = True
        
        for i in range(0,100):
            resultado = Dado.jogaDado()
            
            if(resultado<1 or resultado>6):
                retorno_esperado = False
            
        self.assertEqual(retorno_esperado, True)
        
class ArremessoTeste (unittest.TestCase):
    

    def testa_se_dados_escolhidos_sao_possiveis(self):
        Arremesso.lArremessos.clear()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados        

        self.assertEqual(Arremesso.escolhe_dados([3,1,5]) ,1)
    
    def testa_se_tem_dados_para_arremessar(self):
        Arremesso.lArremessos.clear()
        retorno_esperado = Arremesso.arremessa([1,2,3,4,5])
        
        self.assertEqual(retorno_esperado, -2)
        
    def testa_se_tem_arremesso(self):
        Arremesso.lArremessos.clear()
        Arremesso.arremessa([])
        Arremesso.arremessa([1])
        Arremesso.arremessa([1,2,3])
        
        retorno_esperado = Arremesso.arremessa([1,2,3,4])
        
        self.assertEqual(retorno_esperado, -1)
        
    def testa_se_lValores_retorna_valor_esperado(self):
        Arremesso.lArremessos.clear()
        retorno_esperado = Arremesso.arremessa([])
        for el in retorno_esperado:
            self.assertEqual(type(el), int)
            
        self.assertEqual(len(retorno_esperado), 5)
        
        
    def testa_se_dados_escolhidos_nao_sao_possiveis(self):
        Arremesso.lArremessos.clear()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados
        
        self.assertEqual(Arremesso.escolhe_dados([3,1,6]),0)
        self.assertEqual(Arremesso.escolhe_dados([3,3,3]),0)


unittest.main()