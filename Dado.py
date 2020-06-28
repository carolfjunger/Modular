# -*- coding: utf-8 -*-
'''
    Nome: Dado
    Descriçao: Módulo responsavel por controlar as ações de um dado especifico específico.
    Funcoes de Acesso: jogaDado
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao da função
        
'''

import random
import exemplo

print('chamou')
__all__ = ["jogaDado"]

'''
    Definição:
        Função responsável por jogar um dado em um jogo de Yathzee.
    Parâmetros:
    
    Retorno: 
        Valor inteiro de 1 a 6
'''

def jogaDado():
    return random.randint(1,6)



if __name__ == "__main__":
    exemplo.executa_teste(jogaDado())