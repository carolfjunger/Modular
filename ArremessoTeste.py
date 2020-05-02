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
    
    def testa_se_quantidade_de_valores_eh_igual_qnt_de_dados(self):
        qnt_dados = 5
        lValoresGerados = Arremesso.arremessa(qnt_dados)
        self.assertEqual(len(lValoresGerados),qnt_dados)
        
    def testa_se_dados_escolhidos_sao_possiveis(self):
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados        

        self.assertEqual(Arremesso.escolhe_dados([3,1,5]) ,1)
        
    def testa_se_dados_escolhidos_nao_sao_possiveis(self):
        lValoresGerados = [3,2,4,1,5]
        Arremesso.lValores = lValoresGerados
        
        self.assertEqual(Arremesso.escolhe_dados([3,1,6]),0)
        self.assertEqual(Arremesso.escolhe_dados([3,3,3]),0)
    
    def testa_se_funcao_geraPontuacao_eh_chamada_corretamente(self):
        self.assertEqual(type(Arremesso.possiveis_pontuacoes([3,1,2,3,4])), dict)

unittest.main()
        
            
        
        
    
    