# -*- coding: utf-8 -*-
'''
    Nome: Partida
    Descriçao: Modulo responsavel por gerenciar um partida num jogo de Yathzee
    Funcoes de Acesso: cria, finaliza
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               22/04/2020          criacao das primeiras funcoes

'''

__all__ = ["cria", "finaliza", "limpa_partidas"]

partidas = []

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

def cria (jogadores):
    if (type(jogadores) != list):
        return -2
    elif (len(jogadores) < 2):
        return -1
    for partida in partidas:
        if( partida["ativa"] ==  True):
            return -3
    index = len(partidas) - 1
    if (index > 0):
        lastId = partidas[len(partidas) - 1]["id"]
    else:
        lastId = -1
    partida = {"id": lastId + 1, "jogadores": [], "campeao": [], "ativa": True}
    for jogador in jogadores:
        partida["jogadores"].append(jogador)
    if (len(partida["jogadores"]) < 2):
        return -1
    partidas.append(partida)
    return 1

'''
    Definição:
        Função responsável por limpar a lista de partidas.
    Parâmetros:
    Retorno: 
    
'''

def limpa_partidas():
    while( partidas != []):
        partidas.pop()



'''
    Definição:
        Função responsável por definir o ganhador da partida.
    Parâmetros:
    Retorno: 
        lista com o jogador ou os jogadores (caso empate) que obtiveram a maior pontuacao
        
'''

def defineJogadorComMaiorPontuacao (jogadores):
    maxPontuacao = jogadores[0]["totalDePontos"]
    jogadorCampeao = [jogadores[0]]
    for i in range(1, len(jogadores)):
        if (maxPontuacao < jogadores[i]["totalDePontos"]):
            maxPontuacao = jogadores[i]["totalDePontos"]
            jogadorCampeao = [jogadores[i]]
        elif (maxPontuacao == jogadores[i]["totalDePontos"] ):
            jogadorCampeao.append(jogadores[i])

    return jogadorCampeao

'''
    Definição:
        Função responsável por finalizar uma partida ativa e definir o ganhador
        da partida.
    Parâmetros:
    Retorno: 
        1: caso partida finalizada com sucesso e campeao definido
        -1: caso nao tenha partidas ativas
        
'''


def finaliza ():
    for partida in partidas:
        if (partida["ativa"] == True):
            jogadorCampeao = defineJogadorComMaiorPontuacao(partida["jogadores"])
            partida["ativa"] = False
            partida["campeao"] = jogadorCampeao
            return 1
    return -1

