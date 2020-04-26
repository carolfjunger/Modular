# -*- coding: utf-8 -*-
'''
    Nome: arremesso
    Descriçao: Módulo responsavel por controlar as ações de um arremesso em uma rodada de um jogo de yathzee.
    Funcoes de Acesso: jogarDado
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               26/04/2020          criacao da função
        
'''
lPontuacoes = []

def geraPontuacoes(lValores):
    DicPosicoes = {}
    lPontuacoes.clear()
    
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
               
        
print(geraPontuacoes([1,3,1,2,1]))    
      
        
        
        
            
            
            
    
    