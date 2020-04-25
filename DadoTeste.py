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
from dado import Dado

class DadoTeste (unittest.TestCase):
    
    dado = Dado()   
    
    def testa_se_valor_retornado_pela_funcao_jogarDado_eh_valido (self):       
        i=0
        retorno_esperado = True
        while (i<100):
            resultado = self.dado.jogaDado()
            if(resultado<1 or resultado>6):
                retorno_esperado = False
            i+=1
        self.assertEqual(retorno_esperado, True)
        
    if __name__ == '__main__':
        unittest.main()