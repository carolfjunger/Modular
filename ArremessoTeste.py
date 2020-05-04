# -*- coding: utf-8 -*-
'''
    Nome: ArremessoTeste
    Descriçao: Módulo responsavel testar as funções do Módulo Arremesso.
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               25/04/2020          criacao da função
        
'''

import unittest
import Arremesso


class ArremessoTeste (unittest.TestCase):
    

    def testa_se_dados_escolhidos_sao_possiveis(self):
        Arremesso.lArremessos.clear()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados        

        self.assertEqual(Arremesso.escolhe_dados([3,1,5]) ,1)
    
    def testa_se_tem_dados_para_arremessar(self):
        Arremesso.lArremessos.clear()
        retorno_esperado = Arremesso.arremessa([1,2,3,4,5])
        
        self.assertEqual(retorno_esperado, -2)
        
    def testa_se_tem_arremesso(self):
        Arremesso.lArremessos.clear()
        Arremesso.arremessa([])
        Arremesso.arremessa([1])
        Arremesso.arremessa([1,2,3])
        
        retorno_esperado = Arremesso.arremessa([1,2,3,4])
        
        self.assertEqual(retorno_esperado, -1)
        
    def testa_se_lValores_retorna_valor_esperado(self):
        Arremesso.lArremessos.clear()
        retorno_esperado = Arremesso.arremessa([])
        for el in retorno_esperado:
            self.assertEqual(type(el), int)
            
        self.assertEqual(len(retorno_esperado), 5)
        
        
    def testa_se_dados_escolhidos_nao_sao_possiveis(self):
        Arremesso.lArremessos.clear()
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados
        
        self.assertEqual(Arremesso.escolhe_dados([3,1,6]),0)
        self.assertEqual(Arremesso.escolhe_dados([3,3,3]),0)


unittest.main()
    