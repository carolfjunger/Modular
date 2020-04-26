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

lValores = []
lDadosEscolhidos = []

def arremessa(qnt_dados):
    lValores.clear()
    for i in range(0,qnt_dados):
        lValores.append(Dado.jogaDado())
    return lValores

def escolhe_dados(lDados):
    lAuxiliar = lValores
    for dado in lDados:
        if(dado not in lAuxiliar):
            return 0
        else:
            lAuxiliar.remove(dado)
    
    lDadosEscolhidos = lDados
    return 1
    
def possiveis_pontuacoes(lValores):
    return RegrasDePontuacao.geraPontuacoes(lValores)
    