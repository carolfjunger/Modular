# -*- coding: utf-8 -*-
'''
    Nome: Cartela
    Descriçao: Modulo responsavel por gerenciar uma Cartela num jogo de Yathzee
    Funcoes de Acesso: cria, somaPontuacao, validaPosicao
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               26/04/2020          criacao das primeiras funcoes
        AB              2               26/05/2020          alteracao de funcoes para compatibilidade com xml
        AB              3               31/05/2020          atualizacao de funcoes
        
'''

import Jogador
import recuperacao

__all__ = ["cria", "preenche", "somaPontuacao", "verificaSePontuacaoEstaDisponivel"]

'''
    Definição:
        Função responsável por criar uma cartela para cada jogador em uma partida de Yahtzee.
    Parâmetros:
        
    Retorno: 
        1: caso a cartela tenha sido criado com sucesso
        -1: nao exista jogador
'''

def cria(partida_id, connection):
    lJogadores = Jogador.pegaTodos(partida_id, connection)
    
    lId = []
    for el in lJogadores:
        lId.append(el[0])
        
    if len(lId) == 0 :
        return -1
    
    recuperacao.inicializa(lId)
    
    return 1        

'''
    Definição:
        Função responsável por preencher uma cartela em uma partida de Yahtzee.
    Parâmetros:
        jogadorId: Id do jogador
        posicaoCartela: nome da posicao a ser preenchida na cartela
        ponto: valor dos pontos a serem preenchidos
    Retorno: 
        1: caso a cartela tenha sido preenchida com sucesso
        -1: caso arquivo xml não tenha sido preenchido corretamente
'''

def preenche(jogadorId,posicaoCartela, pontos):

    dicJogo = recuperacao.load()
    try:
        dicJogo[jogadorId][posicaoCartela] = str(pontos)
        recuperacao.save(dicJogo)
        
        teste = recuperacao.load()
        
        if(teste[jogadorId][posicaoCartela] == ' '):
            return -1
    except:
        return -2
    
    return 1



'''
    Definição:
        Função responsável por preencher uma cartela em uma partida de Yahtzee.
    Parâmetros:
        jogadorId: Id do jogador
        posicaoCartela: nome da posicao a ser preenchida na cartela
        ponto: valor dos pontos a serem preenchidos
    Retorno: 
        1: caso a cartela tenha sido preenchida com sucesso
        -1: caso arquivo xml não tenha sido preenchido corretamente
'''

def verificaSePontuacaoEstaDisponivel(jogadorId,posicaoCartela):
    dicJogo = recuperacao.load()
    try:
        if(dicJogo[jogadorId][posicaoCartela] == ' '):
            return True
        else:
            return False
        
    except:
        return -2
    



'''
    Definição:
        Função responsável por retornar a pontuacao final de um jogador em uma partida de Yahtzee.
    Parâmetros:
        jogadorId: Id do jogador
    Retorno: 
        1: caso a soma tenha sido realizada com sucesso
        -1: caso o jogador nao tenha cartela
'''

def somaPontuacao (jogadorId, connection):

    dicJogo = recuperacao.load()
    
    try:
        dicJogo[jogadorId]
    except:
        return -1

    totalDePontos = 0
    for el in dicJogo[jogadorId]:
        if(dicJogo[jogadorId][el] != ' ' ):
            totalDePontos = totalDePontos + int(dicJogo[jogadorId][el])
    
    Jogador.vinculaPontuacaoFinalAoJogador(jogadorId, totalDePontos, connection)
    
    return 1
