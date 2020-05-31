# -*- coding: utf-8 -*-
'''
    Nome: Rodada
    Descriçao: Modulo responsavel por gerenciar uma Rodada num jogo de Yathzee
    Funcoes de Acesso: cria, finaliza
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               23/04/2020          criacao das primeiras funcoes
        ACJ             2               26/05/2020          refatoração do codigo
        ACJ             3               31/05/2020          criacao do iniciaRodada
        
'''

__all__ = ["cria", "existe"]

rodadas = []

import mysql.connector
from mysql.connector import Error
from Principal import conecatarNoBD, selecionaDados
from Arremesso import arremessa
from RegrasDePontuacao import geraPontuacoes

'''
    Definição:
        Função responsável por verificar se o jogador já está numa rodada ativa
    Parâmetros: 
        jogadorId: id do jogador
        partidaId: id da partida
    Retorno: 
        1: caso o jogador esteja
        -1: caso o jogador nao esteja
        
'''

def existe (jogadorId, partidaId, numero, connection):
    query = 'select * from rodadas where numero=%s and jogador_id=%s and partida_id=%s'
    cursor = connection.cursor()
    if (cursor):
        cursor.execute(query, (numero,jogadorId,partidaId))
        row = cursor.fetchall()
        if(row != []):
            return 1
    return -1

  


'''
    Definição:
        Função responsável por criar uma Rodada de uma partida de Yahtzee.
    Parâmetros:
        jogador: Instância do tipo Jogador que representa o jogador que jogará a rodada
        numero: número da rodada a ser criada
    Retorno: 
        1: caso rodada tenha sido criada com sucesso
        -1: caso jogador nao seja um dicionario
        -2: caso jogador nao seja do tipo Jogador
        -3: caso numero nao seja um inteiro
        -4: caso o numero seja menor que 1
        -5: caso o numero seja maior que 13
        -6: caso ja tenha alguma rodada ativa

'''


def cria(jogadorId, partidaId,numero, connection):
    if ( type(numero) == int):
        if(numero<1):
            return -4
        elif (numero>13):
            return -5
    else:    
        return -3
    existeRodada = existe(jogadorId,partidaId, numero, connection)
    if(existeRodada != -1):
        return -6
    query = 'INSERT INTO rodadas(jogador_id, numero, partida_Id) VALUES(%s,%s, %s);'
    cursor = connection.cursor()
    if (cursor):
        cursor.execute(query, (jogadorId, numero, partidaId))
        connection.commit()     
        return 1
    return -1



def iniciaRodada(rodadaId, connection):
    query1 = "select * from rodadas where id=%s"
    if(connection.is_connected()):
        cursor = connection.cursor()
        cursor.execute(query1, (rodadaId,))
        rodada = cursor.fetchall()
        if(rodada != []):
            query2 = "select * from possiveis_pontuaçoes_na_rodada where rodada_id=%s"
            cursor.execute(query2, (rodadaId,))
            pontuacaoNaRodada = cursor.fetchall()
            if (pontuacaoNaRodada != []):
                return -3 # caso o jogador já tenha pontuado nessa rodada
            dados = []
            for i in range(1,4):
                dadosResultantes = arremessa(dados)
                pontuacoesAtuais = geraPontuacoes(dadosResultantes)
                dados = selecionaDados(dadosResultantes)
                if (len(dados) == 5 or i == 3 ):
                    for key in pontuacoesAtuais.keys():
                        if(pontuacoesAtuais[key] != 0): # salva no banco somente as posições em que o jogador pontua alguma coisa, ou seja, pontua algo diferente de zero
                            try:
                                query3 = 'INSERT INTO possiveis_pontuaçoes_na_rodada(rodada_id, pontuacaoName, pontuacaoValor) VALUES(%s,%s, %s);'
                                pontuacaoPontos = pontuacoesAtuais[key]
                                pontuacaoNome = key
                                cursor.execute(query3, (rodadaId,pontuacaoNome, pontuacaoPontos))
                                connection.commit()
                                if (cursor.rowcount != 1):
                                    return -4 #erro na inserção de uma possivel pontuacao
                            except Error as e:
                                print("Erro ao inserir tupla {}".format(e))
                                return -4 #erro na inserção de uma possivel pontuacao
        else:
            return -1
    else:
        return -2 #erro ao conectar no bd
    return 1
