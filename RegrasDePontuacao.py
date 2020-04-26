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
    lPontuacoes.clear()
    
    for i in range(0,6): #preenche tabela 1 a 6
        qnt = 0
        for valor in lValores:
            if valor == i+1:
                qnt+=1 

        lPontuacoes.append(qnt*(i+1))
        

        
    for valor in lValores:
        qnt = 0
        for el in lValores: 
            if(valor == el):
                qnt+=1
    
    if(qnt>=3):
        soma_dados = 0
        for valor in lValores:
            soma_dados = valor + soma_dados
        lPontuacoes.append(soma_dados)
    else:
        lPontuacoes.append(0)
    
    if(qnt>=4):
        soma_dados = 0
        for valor in lValores:
            soma_dados = valor + soma_dados
        lPontuacoes.append(soma_dados)
    else:
        lPontuacoes.append(0)
        
    
    qnt_dupla = qnt_trinca = 0
    for valor in lValores:
        for el in lValores: 
            if(valor == el):
                qnt+=1
        if(qnt == 2):
            qnt_dupla = 1
        if(qnt == 3):
            qnt_trinca = 1
        qnt = 0
    
    if (qnt_dupla == 1 and qnt_trinca == 1):
        lPontuacoes.append(25)
    else:
        lPontuacoes.append(0)
        
    if(2 in lValores and 3 in lValores and 4 in lValores and 5 in lValores and 6 in lValores):
        lPontuacoes.append(30)
    else:
        lPontuacoes.append(0)
    
    if(1 in lValores and 2 in lValores and 3 in lValores and 4 in lValores and 5 in lValores):
        lPontuacoes.append(40)
    else:
        lPontuacoes.append(0)
        
        
    qnt = 0
    for i in range(0,4):
        if(lValores[i] == lValores[i+1]):
            qnt+=1
    
    if(qnt==4):
        lPontuacoes.append(50)
    else:
        lPontuacoes.append(0)
        
    soma = 0    
    for el in lValores:
        soma = el + soma
    
    lPontuacoes.append(soma)
    
    return lPontuacoes
               
        
lPontuacoes = geraPontuacoes([1,3,1,2,1])      
print(lPontuacoes)      
        
        
        
            
            
            
    
    