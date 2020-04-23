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


def cria(jogador, numero):
    if (type(jogador) != dict ):
        return -1
    elif (jogador == {}):
        return -2
    if ( type(numero) == int):
        if(numero<1):
            return -4
        elif (numero>13):
            return -5
    else:    
        return -3
    for rodada in rodadas:
        if(rodada["ativa"] ==  True):
            return -6
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


'''
    Definição:
        Função responsável por finalizar uma Rodada ativa de uma partida de Yahtzee.
    Parâmetros:
        
    Retorno: 
        1: caso rodade tenha sido finalizada com sucesso
        -1: caso nao tem rodada ativa

'''

def finaliza ():
    for rodada in rodadas:
        if (rodada["ativa"] == True):
            rodada["ativa"] = False
            return 1
    return -1