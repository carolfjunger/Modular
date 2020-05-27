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
        
'''

__all__ = ["cria", "limpa_rodadas", "finaliza"]

rodadas = []

import mysql.connector
from mysql.connector import Error
from Principal import conecatarNoBD

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
        print('row')
        print(row)
        if(row != []):
            return row[0]
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


