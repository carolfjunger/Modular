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

def cria (jogadores):
    if (type(jogadores) != list or len(jogadores) < 2):
        return -1
    for partida in partidas:
        if( partida["ativa"] ==  True):
            return -1
    index = len(partidas) - 1
    if (index > 0):
        lastId = partidas[len(partidas) - 1]["id"]
    else:
        lastId = -1
    partida = {"id": lastId + 1, "jogadores": [], "campeao": "", "ativa": True}
    for jogador in jogadores:
        partida["jogadores"].append(jogador)
    if (len(partida["jogadores"]) < 2):
        return -1
    partidas.append(partida)
    return 1

def limpa_partidas():
    while( partidas != []):
        partidas.pop()

def finaliza ():
    for partida in partidas:
        if (partida["ativa"] == True):
            partida["ativa"] = False
            return 1
    return -1

