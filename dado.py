# -*- coding: utf-8 -*-
'''
    Nome: Dado
    Descriçao: Módulo responsavel por controlar as ações de um dado especifico específico.
    Funcoes de Acesso: jogarDado
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao da função
        
'''

import random

class Dado:
    
    def __init__(self):
        return
    
    def jogaDado(self):
        return random.randint(1,6)
    