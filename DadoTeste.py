# -*- coding: utf-8 -*-
'''
    Nome: DadoTeste
    Descriçao: Módulo responsavel testar as funções do Módulo Dado.
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao da função
        
'''
import unittest
import Dado

class DadoTeste (unittest.TestCase):

    def testa_se_valor_retornado_pela_funcao_jogarDado_eh_valido (self):       
        retorno_esperado = True
        
        for i in range(0,100):
            resultado = Dado.jogaDado()
            
            if(resultado<1 or resultado>6):
                retorno_esperado = False
            
        self.assertEqual(retorno_esperado, True)
        

unittest.main()