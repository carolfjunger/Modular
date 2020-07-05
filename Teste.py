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
        ACJ             13              25/05/2020          refatoração dos testes de jogador e partida
        ACJ             14              26/05/2020          refatoração dos testes de rodada
        AB              15              26/05/2020          refatoracao dos testes de cartela
        ACJ             16              30/05/2020          criacao dos testes para iniciarodada
        ACJ             17              31/05/2020          refatoração dos testes de arremesso
        AB              18              31/05/2020          atualizacao de funcoes
        AB              18              01/06/2020          atualizacao de funcoes
        
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
from ConectarBD import conecatarNoBD
import recuperacao

class JogadorTeste(unittest.TestCase):
    def testa_01_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 01 Funcao Cria Jogador - Funcao retorna -1 caso o nome seja uma string vazia")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.cria("", connection)
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 02 Funcao Cria Jogador - Funcao retorna -2 caso o nome nao seja uma string")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.cria(1223, connection )
        self.assertEqual(retorno_esperado, -2)

    def testa_03_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 03 Funcao Cria Jogador - Funcao retorna -3 caso ja a conexao com o banco nao seja estabelecida")
        connection = -1
        retorno_esperado = Jogador.cria("Joao", connection)
        self.assertEqual(retorno_esperado, -3)

    def testa_04_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 04  Funcao Cria Jogador- Funcao retorna 1 caso o jogador tem sido criado ")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.cria("Pedro", connection)
        self.assertEqual(retorno_esperado, 1)

    def testa_01_funcao_existe_modulo_jogador(self):
        print("Caso de Teste 01  Funcao Existe Jogador- Funcao retorna -1 caso o jogador nao exista ")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.existe(-1, connection)
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_existe_modulo_jogador(self):
        print("Caso de Teste 02  Funcao Existe Jogador- Funcao retorna 1 caso o jogador  exista ")
        connection = conecatarNoBD()
        Jogador.cria("Pedro", connection)
        retorno_esperado = Jogador.existe(1, connection)
        self.assertEqual(retorno_esperado, 1)
    
    def testa_01_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 01 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -1 caso o jogador Id nao exista")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(-3, 25, connection)
        self.assertEqual(retorno_esperado, -1)


    def testa_03_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 03 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -3 caso a total de pontos nao seja um int")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(2, "oi", connection)
        self.assertEqual(retorno_esperado, -3)

    def testa_04_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 04 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna -4 caso a total de pontos seja menor que 0")
        connection = conecatarNoBD()
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(2, -1, connection)
        self.assertEqual(retorno_esperado, -4)
    
    def testa_05_funcao_vinculaPontuacaoFinalAoJogador_modulo_jogador(self):
        print("Caso de Teste 05 Funcao vinculaPontuacaoFinalAoJogador - Funcao retorna 1 caso sucesso")
        connection = conecatarNoBD()
        Jogador.cria("Pedro", connection)
        retorno_esperado = Jogador.vinculaPontuacaoFinalAoJogador(1, 100, connection)
        self.assertEqual(retorno_esperado, 1)        

    

class PartidaTeste(unittest.TestCase):
    
    def teste_02_funcao_finaliza_modulo_partida(self):
        print("Caso de Teste 02 Funcao Finaliza Partida - Funcao retorna 1 caso tenha finalizado a partida")
        connection = conecatarNoBD()
        Partida.cria([2,3], connection)
        retorno_esperado = Partida.finaliza(1,connection)
        self.assertEqual(retorno_esperado, 1)
    
    def teste_01_funcao_cria_modulo_partida(self):
        print("Caso de Teste 01 Funcao Cria Partida- Funcao retorna -1 caso array de jogadores tenha tamanho menor que 2")
        connection = conecatarNoBD()
        retorno_esperado = Partida.cria([], connection)
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_partida(self):
        print("Caso de Teste 02 Funcao Cria Partida - Funcao retorna -1 caso jogadores nao seja um array")
        connection = conecatarNoBD()
        retorno_esperado = Partida.cria(1111, connection)
        self.assertEqual(retorno_esperado, -2)


    def teste_03_funcao_cria_modulo_partida(self):
        print("Caso de Teste 03 Funcao Cria Partida - Funcao retorna -2 caso ja tenha uma partida ativa")
        connection = conecatarNoBD()
        Jogador.cria("João", connection)
        Jogador.cria("Pedro", connection)
        Partida.cria([1,2], connection)
        retorno_esperado = Partida.cria([1,2], connection)
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_cria_modulo_partida(self):
        print("Caso de Teste 04 Funcao Cria Partida - Funcao retorna 1 caso Partida seja criada com os jogadores")
        connection = conecatarNoBD()
        Partida.finaliza(1,connection)
        Jogador.cria("João", connection)
        Jogador.cria("Pedro", connection)   
        retorno_esperado = Partida.cria([1,2], connection)
        Partida.finaliza(1,connection)
        self.assertEqual(retorno_esperado, 1)



    def teste_01_funcao_defineJogadorComMaiorPontuacao_modulo_partida(self):
        print("Caso de Teste 01 Funcao defineJogadorComMaiorPontuacao")
        connection = conecatarNoBD()
        retorno_esperado = Partida.defineJogadorComMaiorPontuacao([1,2],11,connection)

        self.assertEqual(retorno_esperado, 1)



class RodadaTeste(unittest.TestCase):
    def teste_01_funcao_existe_modulo_rodada(self):
        print("Caso de Teste 01 Funcao Existe Rodada- Funcao retorna -1 caso a rodada nao exista")
        connection = conecatarNoBD()
        retorno_esperado = Rodada.existe(1,13,-2,connection)
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_existe_modulo_rodada(self):
        print("Caso de Teste 02 Funcao Existe Rodada- Funcao retorna 1 caso a rodada  exista")
        connection = conecatarNoBD()
        Rodada.cria(1,1,1,connection)
        retorno_esperado = Rodada.existe(1,1,1,connection)
        self.assertEqual(retorno_esperado, 1)
    
    def teste_03_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 03 Funcao Cria Rodada- Funcao retorna -3 caso o numero da rodada nao seja um numero")
        connection = conecatarNoBD()
        retorno_esperado = Rodada.cria(1,13,"oi",connection)
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 04 Funcao Cria Rodada- Funcao retorna -4 caso o numero da rodada seja menor que 1")
        connection = conecatarNoBD()
        retorno_esperado = Rodada.cria(2,13,-1,connection)
        self.assertEqual(retorno_esperado, -4)

    def teste_05_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 05 Funcao Cria Rodada- Funcao retorna -5 caso o numero da rodada seja maior que 13")
        connection = conecatarNoBD()
        retorno_esperado = Rodada.cria(2,13,15,connection)
        self.assertEqual(retorno_esperado, -5)

    def teste_06_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 06 Funcao Cria Rodada- Funcao retorna -6 caso ja exista uma rodada ativa")
        connection = conecatarNoBD()
        Rodada.cria(1,1,1,connection)
        retorno_esperado = Rodada.cria(1,1,1,connection)
        self.assertEqual(retorno_esperado, -6)

    def teste_07_funcao_cria_modulo_rodada(self):
        print("Caso de Teste 07 Funcao Cria Rodada- Funcao retorna 1 caso a rodada tenha sido criada com sucesso")
        connection = conecatarNoBD()
        rodada = 0
        for i in range(1,14):
            if(Rodada.existe(1,1,i,connection) == -1):
                rodada = i
                break
        retorno_esperado = Rodada.cria(1,1,rodada,connection)
        if(connection.is_connected):
            cursor = connection.cursor()
            if(rodada > 1):
                query = 'select id from rodadas where jogador_id=%s and partida_id=%s and numero=%s;'
                cursor.execute(query, (1,1,rodada))
                result = cursor.fetchone()[0]
                query1 = 'delete from rodadas where id=%s;'
                cursor.execute(query1, (result,))
                connection.commit()
            
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_iniciaRodada_modulo_rodada(self):
        print("Caso de Teste 01 Funcao IniciaRodada Rodada- Funcao retorna -1 caso a rodada nao exista")
        connection = conecatarNoBD()
        query = "select * from rodadas where id=%s"
        i = 0
        result = 0
        cursor = connection.cursor()
        if (cursor):
            while (result != []):
                i += 1
                cursor.execute(query,(i,))
                result = cursor.fetchall()
            retorno_esperado = Rodada.iniciaRodada(i,connection)
        else:
            print("Problemas de conexao")
        self.assertEqual(retorno_esperado, -1)

    def teste_03_funcao_iniciaRodada_modulo_rodada(self):
        print("Caso de Teste 03 Funcao IniciaRodada Rodada- Funcao retorna -3 caso o jogador ja tenha pontuado na rodada")
        connection = conecatarNoBD()
        query = "select rodada_id from possiveis_pontuaçoes_na_rodada where id=%s"
        i = 0
        result = None
        cursor = connection.cursor()
        Rodada.iniciaRodada(1,connection)
        if (cursor):
            while (result is None):
                i += 1
                cursor.execute(query,(i,))
                result = cursor.fetchone()
            retorno_esperado = Rodada.iniciaRodada(result[0],connection)
        else:
            print("Problemas de conexao")
        self.assertEqual(retorno_esperado, -3)

    def teste_04_funcao_iniciaRodada_modulo_rodada(self):
        print("Caso de Teste 04 Funcao IniciaRodada Rodada- Funcao retorna 1 caso sucesso")
        connection = conecatarNoBD()
        query = "select rodada_id from possiveis_pontuaçoes_na_rodada where id=%s"
        i = 0
        result = 0
        cursor = connection.cursor()
        if (cursor):
            while (result is not None):
                i += 1
                cursor.execute(query,(i,))
                result = cursor.fetchone()
            query2 = "select * from rodadas where id=%s"
            cursor.execute(query2,(i,))
            result = cursor.fetchone()
            if (result is None):
                rodada = 0
                for i in range(1,14):
                    if(Rodada.existe(1,1,i,connection) == -1):
                        rodada = i
                        break
                Rodada.cria(1,1,rodada,connection)
                query3 = 'select * from rodadas where numero=%s and jogador_id=%s and partida_id=%s'
                cursor.execute(query3, (rodada,1,1))
                rodada_id = cursor.fetchone()[0]
                retorno_esperado = Rodada.iniciaRodada(rodada_id,connection)
                query5 = "select id from possiveis_pontuaçoes_na_rodada where rodada_id=%s"
                cursor.execute(query5, (rodada_id,))
                pontuacoes  = cursor.fetchall()
                for pontuacao in pontuacoes:
                    query6 = 'delete from possiveis_pontuaçoes_na_rodada where id=%s;'
                    cursor.execute(query6, (pontuacao[0],))
                    connection.commit()
                query4 = 'delete from rodadas where id=%s;'
                cursor.execute(query4, (rodada_id,))
                connection.commit()
            else:
                retorno_esperado = Rodada.iniciaRodada(i,connection)

        else:
            print("Problemas de conexao")
        self.assertEqual(retorno_esperado, 1)




class CartelaTeste(unittest.TestCase):

    def teste_01_funcao_cria_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Cria Cartela- Funcao retorna 1 caso exista jogadores na partida")
        connection = conecatarNoBD()
        cursor = connection.cursor()
        query = 'select * from jogador_na_partida where partida_id=%s'
        cursor.execute(query,(1,))
        result = cursor.fetchall()
        if(result == []):
            Jogador.cria('Joao', connection)
            Jogador.cria('Pedro', connection)
            Jogador.cria('José', connection)
            Partida.cria([2,3], connection)
        retorno_esperado = Cartela.cria(1,connection)
 
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Preenche Cartela- Funcao retorna -1 caso arquivo xml nao tenha sido preenchido corretamente")
        connection = conecatarNoBD()
        try:
            dictJogo = recuperacao.load()
        except:
            Cartela.cria(1,connection)
        retorno_esperado = Cartela.preenche(2, 'jogadaDeUm', '-1')
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 02 Funcao Preenche Cartela- Funcao retorna 1 caso arquivo xml tenha sido preenchido corretamente")
        connection = conecatarNoBD()
        try:
            dictJogo = recuperacao.load()
        except:
            Cartela.cria(1,connection)
        retorno_esperado = Cartela.preenche(2, 'jogadaDeUm', '1')
        self.assertEqual(retorno_esperado, 1)

    def teste_03_funcao_preenche_modulo_cartela(self):
        print("Caso de Teste 03 Funcao Preenche Cartela- Funcao retorna -2 caso o jogador nao exista")
        connection = conecatarNoBD()
        try:
            dictJogo = recuperacao.load()
        except:
            Cartela.cria(1,connection)
        retorno_esperado = Cartela.preenche(1, 'jogadaDeUm', '1')
        self.assertEqual(retorno_esperado, -2)

   
    def teste_01_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 01 Funcao Soma Pontuacao Cartela- Funcao retorna -1 caso o jogador nao tenha cartela")
        connection = conecatarNoBD()
        try:
            dictJogo = recuperacao.load()
        except:
            Cartela.cria(1,connection)
        retorno_esperado = Cartela.somaPontuacao('-2', connection)
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_somaPontuacao_modulo_cartela(self):
        print("Caso de Teste 02 Funcao Soma Pontuacao Cartela- Funcao retorna 1 caso sucesso")
        connection = conecatarNoBD()
        try:
            dictJogo = recuperacao.load()
        except:
            Cartela.cria(1,connection)
        retorno_esperado = Cartela.somaPontuacao(2, connection)
        self.assertEqual(retorno_esperado, 1)


class ArremessoTeste (unittest.TestCase):
    
    # def teste01(self):
    #     print("Caso de Teste 01 Funcao arremessa - Funcao retorna -2 caso já tenham sido escolhido todos os cinco dados que o jogador quer manter")
         
    #     retorno_esperado = Arremesso.arremessa( [{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}])
        
    #     self.assertEqual(retorno_esperado, -2)
        
    def teste03(self):
        print("Caso de Teste 03 Funcao arremessa - Funcao retorna uma lista com 5 inteiros, testa se a lista tem 5 itens")
         
        retorno_esperado = Arremesso.arremessa([{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}])

        self.assertEqual(len(retorno_esperado), 5)

    def teste04(self):
        print("Caso de Teste 04 Funcao arremessa - Funcao retorna uma lista com 5 inteiros, testa se todos itens da lista sao inteiros")
         
        retorno_esperado = Arremesso.arremessa([{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}])
        
        self.assertEqual(all(isinstance(n["valor"], int) for n in retorno_esperado), True)
        
   

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
