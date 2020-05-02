# -*- coding: utf-8 -*-
'''
    Nome: Cartela
    Descriçao: Modulo responsavel por gerenciar uma Cartela num jogo de Yathzee
    Funcoes de Acesso: cria, somaPontuacao, validaPosicao
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               26/04/2020          criacao das primeiras funcoes
        
'''

import Jogador
__all__ = ["cria", "somaPontuacao"]


cartelas = []



'''
    Definição:
        Função responsável por criar uma cartela em uma partida de Yahtzee.
    Parâmetros:
        nome: String com o nome do jogador
    Retorno: 
        1: caso a cartela tenha sido criado com sucesso
        -1: caso o jogadorId nao seja um numero
        -2: caso nao exista um jogador com esse id
        -3: caso ja exista uma cartela para esse jogador
'''
def cria(jogadorId):
    if (type(jogadorId) != int):
        return -1
    idExiste = Jogador.existe(jogadorId)
    if (idExiste != 1):
        return -2
    jogadorJaTemCartela = False
    for cartela in cartelas:
        if( cartela["jogadorId"] == jogadorId):
            jogadorJaTemCartela = True
            break
    if (jogadorJaTemCartela):
        return -3
    index = len(cartelas) - 1
    if (index > 0):
        lastId = cartelas[len(cartelas) - 1]["id"]
    else:
        lastId = -1
    cartela = { "id": lastId + 1 ,"jogadorId": jogadorId, "pontuacoes": {"jogadaDeUm": -1, "jogadaDeDois": -1, "jogadaDeTres": -1, "jogadaDeQuatro": -1, "jogadaDeCinco": -1, "jogadaDeSeis": -1, "trinca": -1, "quadra": -1, "fullHouse": -1, "sequenciaAlta": -1, "sequenciaBaixa": -1, "general": -1, "jogadaAleatoria": -1} }
    cartelas.append(cartela)
    return 1


'''
    Definição:
        Função responsável limpar a lista de cartelas.
    Parâmetros:
    
    Retorno: 
    
'''
def limpa_cartelas():
    while(cartelas != []): 
        cartelas.pop()

'''
    Definição:
        Função responsável por verificar se uma cartela existe.
    Parâmetros:
        jogadorId: Id do jogador
    Retorno: 
        i: index da cartela caso ela exista
        -1: caso a cartela nao exista

'''
def verificaSeACartelaExiste (jogadorId):
    for i in range(0, len(cartelas)):
        if(cartelas[i]["jogadorId"] == jogadorId):
            return i
    return -1


'''
    Definição:
        Função responsável por preencher uma cartela em uma partida de Yahtzee.
    Parâmetros:
        jogadorId: Id do jogador
        posicaoCartela: nome da posicao a ser preenchida na cartela
        ponto: valor dos pontos a serem preenchidos
    Retorno: 
        1: caso a cartela tenha sido preenchida com sucesso
        -1: caso o jogadorId nao seja um numero
        -2: caso o jogador nao tenha cartela
        -3: caso a posicao da cartela nao seja uma string
        -4: caso o nome da pontuacao nao exista
        -5: caso os pontos nao sejam um numero inteiro
        -6: caso os pontos sejam menores que zero
'''

def preenche(jogadorId,posicaoCartela, pontos):
    if (type(jogadorId) != int):
        return -1
    index = verificaSeACartelaExiste(jogadorId)
    if (index == -1):
        return -2
    if (type(posicaoCartela) != str):
        return -3
    cartela = cartelas[index]
    pontuacoes = cartela["pontuacoes"]
    pontuacaoExiste = False
    for nomeDaPontuacao in pontuacoes:
        if (nomeDaPontuacao == posicaoCartela):
            pontuacaoExiste = True
            break
    if (pontuacaoExiste == False):
        return -4
    if (type(pontos) != int):
        return -5
    if (pontos < 0):
        return -6
    pontuacoes[posicaoCartela] = pontos 
    return 1


'''
    Definição:
        Função responsável por retornar a pontuacao final de um jogador em uma partida de Yahtzee.
    Parâmetros:
        jogadorId: Id do jogador
    Retorno: 
        1: caso a soma tenha sido realizada com sucesso
        -1: caso o jogadorId nao seja um numero
        -2: caso o jogador nao tenha cartela
        -3: caso ocorra erro na funcao vinculaPontuacaoFinalAoJogador
'''
def somaPontuacao (jogadorId):
    if (type(jogadorId) != int):
        return -1
    index = verificaSeACartelaExiste(jogadorId)
    if (index == -1):
        return -2
    pontuacoes = cartelas[index]["pontuacoes"]
    totalDePontos = 0
    for pontuacao in pontuacoes.values():
        totalDePontos += pontuacao
    retorno = Jogador.vinculaPontuacaoFinalAoJogador(jogadorId, totalDePontos)
    if(retorno == 1):
        return 1
    return -3
