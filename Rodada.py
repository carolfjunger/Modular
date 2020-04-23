# -*- coding: utf-8 -*-
'''
    Nome: Rodada
    Descriçao: Modulo responsavel por gerenciar uma Rodada num jogo de Yathzee
    Funcoes de Acesso: cria, finaliza
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               23/04/2020          criacao das primeiras funcoes
        
'''

__all__ = ["cria", "limpa_rodadas", "finaliza"]

rodadas = []


def cria(jogador, numero):
    if (type(jogador) != dict or jogador == {} or type(numero) != int or numero<1 or numero>13):
        return -1
    index = len(rodadas) - 1
    if (index > 0):
        lastId = rodadas[len(rodadas) - 1]["id"]
    else:
        lastId = -1
    rodada = {"id": lastId + 1, "jogador": jogador["id"], "numero": numero,  "possiveisPontuacoes": [], "ativa": True}
    rodadas.append(rodada)  
    return 1 


def limpa_rodadas():
    while( rodadas != []):
        rodadas.pop()

def finaliza ():
    for rodada in rodadas:
        if (rodada["ativa"] == True):
            rodada["ativa"] = False
            return 1
    return -1