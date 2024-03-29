# -*- coding: utf-8 -*-
'''
    Nome: arremesso
    Descriçao: Módulo responsavel por controlar as regras de pontuacoes em uma rodada de um jogo de yathzee.
    Funcoes de Acesso: geraPontuacoes
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               26/04/2020          criacao da função
        AB             2               28/04/2020          alteração da função para dicionário
        
'''

__all__ = ["geraPontuacoes"]


'''
    Definição:
        Função responsável por gerar pontuacao de 5 dados em um jogo de Yathzee.
    Parâmetros:
        lValores: Lista com valores dos dados que serão calculados a pontuação
    Retorno: 
        Dicionário com possiveis pontuações para cada escolha da cartela
'''

def geraPontuacoes(lValores):
    DicPosicoes = {}

    
    for i in range(0,6): #preenche tabela 1 a 6
        qnt = 0
        for valor in lValores:
            if valor == i+1:
                qnt+=1 
        
        if(i ==0):
            DicPosicoes['jogadaDeUm'] = qnt*(i+1)
        if(i ==1):
            DicPosicoes['jogadaDeDois'] = qnt*(i+1)
        if(i ==2):
            DicPosicoes['jogadaDeTres'] = qnt*(i+1)
        if(i ==3):
            DicPosicoes['jogadaDeQuatro'] = qnt*(i+1)
        if(i ==4):
            DicPosicoes['jogadaDeCinco'] = qnt*(i+1)
        if(i ==5):
            DicPosicoes['jogadaDeSeis'] = qnt*(i+1)
        

        
    for valor in lValores:
        qnt = 0
        for el in lValores: 
            if(valor == el):
                qnt+=1
    
    if(qnt>=3):
        soma_dados = 0
        for valor in lValores:
            soma_dados = valor + soma_dados
        DicPosicoes['trinca'] = soma_dados
    else:
        DicPosicoes['trinca'] = 0
    
    if(qnt>=4):
        soma_dados = 0
        for valor in lValores:
            soma_dados = valor + soma_dados
        DicPosicoes['quadra'] = soma_dados
    else:
        DicPosicoes['quadra'] = 0
        
    
    qnt_dupla = qnt_trinca = 0
    for valor in lValores:
        qnt = 0
        for el in lValores: 
            if(valor == el):
                qnt+=1
                
        if(qnt == 2):
            qnt_dupla = 1
        if(qnt == 3):
            qnt_trinca = 1
        
    
    if (qnt_dupla == 1 and qnt_trinca == 1):
        DicPosicoes['fullHouse'] = 25
    else:
        DicPosicoes['fullHouse'] = 0
        
    if(2 in lValores and 3 in lValores and 4 in lValores and 5 in lValores and 6 in lValores):
        DicPosicoes['sequenciaAlta'] = 30
    else:
        DicPosicoes['sequenciaAlta'] = 0
    
    if(1 in lValores and 2 in lValores and 3 in lValores and 4 in lValores and 5 in lValores):
        DicPosicoes['sequenciaBaixa'] = 40

    else:
        DicPosicoes['sequenciaBaixa'] = 0
        
        
    qnt = 0
    for i in range(0,4):
        if(lValores[i] == lValores[i+1]):
            qnt+=1
    
    if(qnt==4):
        DicPosicoes['general'] = 50
    else:
        DicPosicoes['general'] = 0
        
    soma = 0    
    for el in lValores:
        soma = el + soma
    
    DicPosicoes['jogadaAleatoria'] = soma
    
    return DicPosicoes
      
        
        
        
            
            
            
    
    