# -*- coding: utf-8 -*-
'''
    Nome: arremesso
    Descriçao: Módulo responsavel por controlar as ações de um arremesso em uma rodada de um jogo de yathzee.
    Funcoes de Acesso: arremessa, escolhe_dados
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao das funções
        AB             2               27/04/2020          criacao casos erro funcoes
        AB             3               28/04/2020          alterações para variaveis globais
        AB             4               04/05/2020          adição de calculo de pontuação na funcao arremessa

        
'''

import Dado
import RegrasDePontuacao

__all__ = ["arremessa"]



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


def arremessa(dados):
    lAux = dados
    for dado in lAux:
        if(dado["selecionado"] == 0):
            dado['valor'] = Dado.jogaDado()
    # lAux = lDadosEscolhidos
    
    # qnt_dados = 5 - len(lDadosEscolhidos)

    # if qnt_dados <= 0:
    #     return -2
    
    # for i in range(0,qnt_dados):
    #     lAux.append(Dado.jogaDado())   
    
    # lValores = lAux
    print('chamou')
    return lAux



