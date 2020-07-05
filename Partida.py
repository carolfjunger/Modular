# -*- coding: utf-8 -*-
'''
    Nome: Partida
    Descriçao: Modulo responsavel por gerenciar um partida num jogo de Yathzee
    Funcoes de Acesso: cria, finaliza
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               22/04/2020          criacao das primeiras funcoes
        ACJ             2               25/05/2020          refatoração do codigo

'''

__all__ = ["cria", "finaliza", "pegaJogadorCampeao"]

from ConectarBD import conecatarNoBD
from mysql.connector import Error
import Jogador

'''
    Funcao: cria
    Definição:
        Função responsável por criar uma partida.
    Parâmetros:
        jogadores: Lista do tipo Jogador contendo os jogadores participantes
        da partida que será inicializada.
    Retorno: 
        1: caso partida criada com sucesso
        -1: caso tenha menos que dois jogadores
        -2: caso o tipo de jogadores nao seja uma lista
        -3: caso ja exista uma outra partida ativa
        
'''

def cria (jogadores, connection):
    if (type(jogadores) != list):
        return -2
    elif (len(jogadores) < 2):
        return -1
    partida = pegaPartidaAtual(connection)
    if(partida is not None):
        return -3
    query1 = 'INSERT INTO partidas(ativa) VALUES(true)'
    try:
        cursor = connection.cursor()
        if (cursor):
            cursor.execute(query1)
            connection.commit()
            partida_id = pegaPartidaAtual(connection)
            query2 = 'INSERT INTO jogador_na_partida(jogador_Id, partida_Id) VALUES(%s,%s);'
            data = []
            for jogador in jogadores:
                data.append((jogador, partida_id))
            cursor.executemany(query2, data)
            connection.commit()
            return 1
    except Error as e:
        print('Erro na cria jogador', e)
        return -3
    return 1

'''
    Definição:
        Função responsável por pegar a partida atual.
    Parâmetros:
    Retorno: 
    
'''

def pegaPartidaAtual (connection):
    try:
        cursor = connection.cursor()
        query= 'select id from partidas where ativa=true'
        if (cursor):
            cursor.execute(query)
            row = cursor.fetchone()
            if(row is not None):
                return row[0]
            return row
    except Error as e:
        print('Erro na pegaPartidaAtual', e)
        return -1



'''
    Definição:
        Função responsável por definir o ganhador da partida.
    Parâmetros:
    Retorno: 
        lista com o jogador ou os jogadores (caso empate) que obtiveram a maior pontuacao
        
'''

def defineJogadorComMaiorPontuacao (jogadoresIds, partida_id, connection):
    jogadores = []
    # pega o total de pontos de cada jogador nessa partida
    for jogador_id in jogadoresIds:
        jogador = Jogador.pegaInformacoesDoJogador(jogador_id,connection)
        if (jogador != -1):
            jogadores.append({ "id": jogador[0], "totalDePontos": jogador[2] })
    # verifica quem obteu mais pontos
    maxPontuacao = jogadores[0]["totalDePontos"]
    jogadoresCampeoes = [jogadores[0]["id"]]
    for i in range(1, len(jogadores)):
        if(jogadores[i]["totalDePontos"]  is not None):
            if (maxPontuacao < jogadores[i]["totalDePontos"]):
                maxPontuacao = jogadores[i]["totalDePontos"]
                jogadoresCampeoes = [jogadores[i]["id"]]
            elif (maxPontuacao == jogadores[i]["totalDePontos"] ):
                jogadoresCampeoes.append(jogadores[i["id"]])
    # seta a flag campeao para os jogadores que obtiveram maior pontuação
    for joagdorCampeao in jogadoresCampeoes:
        try:
            cursor = connection.cursor()
            if(cursor):
                query = 'UPDATE jogador_na_partida SET campeao=1 WHERE jogador_id=%s and partida_id=%s'
                cursor.execute(query, (joagdorCampeao,partida_id))
                connection.commit()
        except Error as e:
            print('Erro na defineJogadorComMaiorPontuacao', e)
            return -1

    return 1

'''
    Definição:
        Função responsável por finalizar uma partida ativa e definir o ganhador
        da partida.
    Parâmetros:
    Retorno: 
        1: caso partida finalizada com sucesso e campeao definido
        -1: caso nao tenha partidas ativas
        
'''


def finaliza (partida_id, connection):
    # partida_id = pegaPartidaAtual(connection)
    query = 'select jogador_id from jogador_na_partida where partida_id = %s'
    query2 = 'UPDATE partidas SET ativa=0 WHERE id=%s'
    try:
        cursor = connection.cursor()
        if (cursor):
            cursor.execute(query, (partida_id,))
            queryResult = cursor.fetchall()
            jogadores = []
            for row in queryResult:
                jogadores.append(row[0])
            campeao = defineJogadorComMaiorPontuacao(jogadores, partida_id, connection)
            if (campeao == 1): # foi definido um campeao e a partida pode ser finalizada
                cursor.execute(query2, (partida_id,))
                connection.commit()
                return 1
            else:
                return -2
            
    except Error as e:
        print('Erro na pegaPartidaAtual', e)
        return -1


def pegaJogadorCampeao(partidaId, connection):
    query = 'select jogador_id, campeao from jogador_na_partida where partida_id=%s'
    cursor = connection.cursor()
    if(cursor):
        cursor.execute(query, (partidaId,))
        records = cursor.fetchall()
        jogadorId = -1
        for row in records:
            if(row[1] == 1):
                jogadorId = row[0]
        if (jogadorId != -1):
            query2 = 'select nome, totalDepontos from jogadores where id=%s'
            cursor.execute(query2, (jogadorId,))
            row = cursor.fetchone()
            return row
        else:
            return -1
    else:
        return -2

pegaJogadorCampeao(1, conecatarNoBD())