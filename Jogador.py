# -*- coding: utf-8 -*-
'''
    Nome: Jogador
    Descriçao: Modulo responsavel por gerenciar um jogador num jogo de Yathzee
    Funcoes de Acesso: cria
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               22/04/2020          criacao das primeiras funcoes
        
'''

__all__ = ["cria", "limpa_jogadores"]

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
    jogador = { "id": lastId + 1, "nome": nome, "totalDePontos": 0, "rodadas": []}
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

