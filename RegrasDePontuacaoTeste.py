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

def transformaEmDicionario (lPontuacao):
    DicPosicoes = {'jogadaDeUm': 0, 'jogadaDeDois' : 0, 'jogadaDeTres': 0, 'jogadaDeQuatro': 0, 'jogadaDeCinco': 0, 'jogadaDeSeis': 0, 'trinca': 0, 'quadra': 0, 'fullHouse': 0, 'sequenciaAlta': 0, 'sequenciaBaixa': 0, 'general': 0, 'jogadaAleatoria': 0}
    
    i = 0
    for posicao in DicPosicoes:
        DicPosicoes[posicao] = lPontuacao[i]
        i+=1
        
    return DicPosicoes

class RegrasDePontuacaoTeste(unittest.TestCase):
    
    def teste01(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,1,2,1]),transformaEmDicionario([3,2,3,0,0,0,8,0,0,0,0,0,8]))
        
    def teste02(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([2,3,1,2,1]),transformaEmDicionario([2,4,3,0,0,0,0,0,0,0,0,0,9]))
        
    def teste03(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([2,3,1,2,1]),transformaEmDicionario([2,4,3,0,0,0,0,0,0,0,0,0,9]))
        
    def teste04(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,1,2,4]),transformaEmDicionario([2,2,3,4,0,0,0,0,0,0,0,0,11]))
    
    def teste05(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([4,5,1,2,6]), transformaEmDicionario([1,2,0,4,5,6,0,0,0,0,0,0,18]))
        
    def teste06(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([4,5,6,2,6]), transformaEmDicionario([0,2,0,4,5,12,0,0,0,0,0,0,23]))
        
    def teste07(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,5,6,2,6]), transformaEmDicionario([0,2,0,0,5,18,25,0,0,0,0,0,25]))
        
    def teste08(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,6,6,2,6]), transformaEmDicionario([0,2,0,0,0,24,26,26,0,0,0,0,26]))
        
    def teste09(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([6,6,2,2,6]), transformaEmDicionario([0,4,0,0,0,18,22,0,25,0,0,0,22]))
    
    def teste10(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([3,2,4,6,5]), transformaEmDicionario([0,2,3,4,5,6,0,0,0,30,0,0,20]))
        
    def teste11(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,3,2,5,4]), transformaEmDicionario([1,2,3,4,5,0,0,0,0,0,40,0,15]))
        
    def teste12(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,1,1,1,1]), transformaEmDicionario([5,0,0,0,0,0,5,5,0,0,0,50,5]))
        
    def teste13(self):
        self.assertEqual(RegrasDePontuacao.geraPontuacoes([1,2,3,4,5]), transformaEmDicionario([1,2,3,4,5,0,0,0,0,0,40,0,15]))
        
    
unittest.main()