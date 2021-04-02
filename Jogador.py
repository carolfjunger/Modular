# -*- coding: utf-8 -*-
'''
    Nome: Jogador
    Descriçao: Modulo responsavel por gerenciar um jogador num jogo de Yathzee
    Funcoes de Acesso: cria
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               22/04/2020          criacao das primeiras funcoes
        ACJ             2               26/04/2020          criacao da funcao pegaJogadorId
        ACJ             3               02/05/2020          criacao da funcao existe
        ACJ             4               03/05/2020          insercao da documentacao faltante
        ACJ             5               25/05/2020          refatoração do codigo
        ACJ             6               31/05/2020          correcao de erros
        
'''
import mysql.connector
from mysql.connector import Error

__all__ = ["cria",  "vinculaPontuacaoFinalAoJogador"]


'''
    Definição:
        Função responsável por criar um Jogador de uma partida de Yahtzee.
    Parâmetros:
        nome: String com o nome do jogador
    Retorno: 
        1: caso jogador tenha sido criado com sucesso
        -1: caso o nome seja uma string vazia
        -2: caso o nome nao seja uma string
        -3: caso ja existem um jogador com esse nome
'''


def cria (nome, connection):
    if (nome == "" ):
        return -1
    if (type(nome) != str):
        return -2
    if(connection == -1):
        return -3
    query = 'INSERT INTO jogadores(nome) VALUES(%s)'
    try:
        cursor = connection.cursor()
        if (cursor):
            cursor.execute(query, (nome,))
            connection.commit()
            return 1
    except Error as e:
        print('Erro na cria jogador', e)
        return -3
    

'''
    Definição:
        Função responsável por vincular a soma da pontuacao da cartela ao jogador.
    Parâmetros: 
        jogadorId: id do Jogador
        totalDePontos: int com a soma total de pontos da cartela
    Retorno:
        1: caso sucesso
        -1: caso o jogador nao exista
        -2: caso o jogadorId nao seja um inteiro
        -3: caso o totalDePontos nao seja um inteiro
        -4: caso o totalDePontos seja menor que 0
        
'''

def vinculaPontuacaoFinalAoJogador (jogadorId, totalDePontos, connection):
    
    if (type(jogadorId) != int):
        return -2
    if (type(totalDePontos) != int):
        return -3
    if (totalDePontos<0):
        return -4
    if(existe(jogadorId, connection) != 1):
        return -1

    query="UPDATE jogadores SET totalDePontos = %s WHERE id = %s"
    cursor = connection.cursor()
    if (cursor):
        cursor.execute(query, (totalDePontos,jogadorId))
        connection.commit()
        return 1

def pegaInformacoesDoJogador(jogadorId, connection):
    query = 'select * from jogadores where id=%s'
    try:
        cursor = connection.cursor()
        if (cursor):
            cursor.execute(query, (jogadorId,))
            result = cursor.fetchall()
            if (result is not None):
                return result[0]
            return -1           
    except Error as e:
        print('Erro na pegaInformacoesDoJogador', e)
        return -1

'''
    Definição:
        Função responsável por verificar se um jogador existe
    Parâmetros: 
        jogadorId: id do jogador
    Retorno: 
        1: caso o jogador exista
        -1: caso o jogador nao exista
        
'''

def existe (jogadorId, connection):
    query = 'select * from jogadores where id=%s'
    cursor = connection.cursor()
    if (cursor):
        cursor.execute(query, (jogadorId,))
        row = cursor.fetchone()
    if(row is not None):
        return 1
    return -1

'''
 Definição:
        Função responsável por pegar todos os jogadores participantes de uma partida de Yatzhee
    Parâmetros: 
        connection: conecta ao banco de dados
    Retorno:
        -1: caso lista vazia
'''

def pegaTodos(partida_id, connection):
    query = 'select jogador_id from jogador_na_partida where partida_id=%s'
    cursor = connection.cursor()
    if (cursor):
        cursor.execute(query,(partida_id,))
        result = cursor.fetchall()
        print('result', result)
        if (result is not None):
            return result
        return -1


    
    
    
    