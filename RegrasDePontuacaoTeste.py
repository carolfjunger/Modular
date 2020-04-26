# -*- coding: utf-8 -*-
'''
    Nome: RegrasDePontuacaoTeste
    Descriçao: Módulo responsavel testar as funções do Módulo RegrasDePontuacao.
    Autores: AB - Alexandra Bugarin
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        AB             1               26/04/2020          criacao da função
        
'''

import unittest
import RegrasDePontuacao

class RegrasDePontuacaoTeste(unittest.TestCase):
    
    def teste01(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,1,2,1]),[3,2,3,0,0,0,8,0,0,0,0,0,8])
        
    def teste02(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([2,3,1,2,1]),[3,2,3,0,0,0,8,0,0,0,0,0,8])
    
unittest.main()