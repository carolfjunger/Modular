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
        
'''

__all__ = ["cria", "limpa_jogadores", "pegaJogadorId", "vinculaPontuacaoFinalAoJogador"]

jogadores = []


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


def cria (nome):
    if (nome == "" ):
        return -1
    if (type(nome) != str):
        return -2
    for jog in jogadores:
        if (jog["nome"] == nome):
            return -3
    index = len(jogadores) - 1
    if (index > 0):
        lastId = jogadores[len(jogadores) - 1]["id"]
    else:
        lastId = -1
    jogador = { "id": lastId + 1, "nome": nome, "totalDePontos": 0}
    jogadores.append(jogador)
    return 1

'''
    Definição:
        Função responsável por limpar a lista de jogadores de uma partida de Yahtzee.
    Parâmetros:
    Retorno: 
        
'''

def limpa_jogadores ():
    while(jogadores != []):
        jogadores.pop()



'''
    Definição:
        Função responsável por pegar o id de um jogador a partir do nome.
    Parâmetros: nome
    Retorno: String id do jogador
        
'''

def pegaJogadorId (nome):
    for jogador in jogadores:
        if (jogador["nome"] == nome):
            return jogador["id"]


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

def vinculaPontuacaoFinalAoJogador (jogadorId, totalDePontos):
    if (type(jogadorId) != int):
        return -2
    if (type(totalDePontos) != int):
        return -3
    if (totalDePontos<0):
        return -4 
    for jogador in jogadores:
        if (jogador["id"] == jogadorId):
            jogador["totalDePontos"] = totalDePontos
            return 1
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

def existe (jogadorId):
    for jogador in jogadores:
        if ( jogador["id"] == jogadorId):
            return 1
    return -1
