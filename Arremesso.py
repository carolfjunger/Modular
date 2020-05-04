# -*- coding: utf-8 -*-
'''
    Nome: arremesso
    Descriçao: Módulo responsavel por controlar as ações de um arremesso em uma rodada de um jogo de yathzee.
    Funcoes de Acesso: jogarDado
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao da função
        
'''

import Dado
import RegrasDePontuacao

__all__ = ["arremessa", "escolhe_dados"]

lValores = []
lDadosEscolhidos = []
lArremessos = []
lPontuacao = []



'''
    Definição:
        Função responsável por arremessar os dados em um jogo de Yathzee.
    Parâmetros:
        nome: Lista com dados já selecionados pelo jogador, no caso de nenhum dado ainda ter sido escolhido,
        uma lista vazia.
    Retorno: 
        lValores: caso o arremesso esteja ok
        -1: caso o jogador já tenha arremessado o número máximo de vezes
        -2: caso o jogador já tenha escolhido todos os 5 dados
'''


def arremessa(lDadosEscolhidos):
    lAux = lDadosEscolhidos
    
    qnt_dados = 5 - len(lDadosEscolhidos)
    qnt_arremesso = len(lArremessos)
  
    if qnt_arremesso == 3:
        return -1
    
    if qnt_dados <= 0:
        return -2
    
    for i in range(0,qnt_dados):
        lAux.append(Dado.jogaDado())   
    
    lValores = lAux
    lPontuacao.append(RegrasDePontuacao.geraPontuacoes(lValores))
    
    lArremessos.append(lValores)
    
    return lValores

'''
    Definição:
        Função responsável por guardar os dados que o jogador irá manter em uma rodada em um jogo de Yathzee.
    Parâmetros:
        lDados: Lista com dados selecionados pelo jogador
    Retorno: 
        0: caso o jogador tenha selecionado um valor que não tinha caido
        1: Funcionou guardar os dados selecionados na lista lDadosEscolhidos
'''
    
def escolhe_dados(lDados):
    lAuxiliar = lValores
    for dado in lDados:
        if(dado not in lAuxiliar):
            return 0
        else:
            lAuxiliar.remove(dado)
    
    lDadosEscolhidos.append(lDados)
    return 1
