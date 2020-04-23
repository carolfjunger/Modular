
import unittest
import Jogador
import Partida

class VerificarPangramaTests(unittest.TestCase):
    def testa_01_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 01 Funcao Cria Jogador - Funcao retorna -1 caso o nome seja uma string vazia")
        retorno_esperado = Jogador.cria("")
        self.assertEqual(retorno_esperado, -1)

    def testa_02_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 02 Funcao Cria Jogador - Funcao retorna -1 caso o nome nao seja uma string")
        retorno_esperado = Jogador.cria(1223)
        self.assertEqual(retorno_esperado, -1)

    def testa_03_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 03 Funcao Cria Jogador - Funcao retorna -1 caso ja exista um jogador com esse nome")
        Jogador.cria("Joao")
        retorno_esperado = Jogador.cria("Joao")
        self.assertEqual(retorno_esperado, -1)

    def testa_04_funcao_cria_modulo_jogador(self):
        print("Caso de Teste 04  Funcao Cria Jogador- Funcao retorna 1 caso o jogador tem sido criado ")
        retorno_esperado = Jogador.cria("Pedro")
        self.assertEqual(retorno_esperado, 1)
    
    def teste_01_funcao_cria_modulo_partida(self):
        print("Caso de Teste 01 Funcao Cria Partida- Funcao retorna -1 caso array de jogadores tenha tamanho menor que 2")
        retorno_esperado = Partida.cria([])
        self.assertEqual(retorno_esperado, -1)

    def teste_02_funcao_cria_modulo_partida(self):
        print("Caso de Teste 02 Funcao Cria Partida - Funcao retorna -1 caso jogadores nao seja um array")
        retorno_esperado = Partida.cria(1111)
        self.assertEqual(retorno_esperado, -1)

    def teste_03_funcao_cria_modulo_partida(self):
        print("Caso de Teste 03 Funcao Cria Partida - Funcao retorna -1 caso ja tenha uma partida ativa")
        Jogador.limpa_jogadores()
        Partida.limpa_partidas()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        Partida.cria(Jogador.jogadores)
        retorno_esperado = Partida.cria(Jogador.jogadores)
        self.assertEqual(retorno_esperado, -1)

    def teste_04_funcao_cria_modulo_partida(self):
        print("Caso de Teste 04 Funcao Cria Partida - Funcao retorna 1 caso Partida seja criada com os jogadores")
        Jogador.limpa_jogadores()
        Partida.limpa_partidas()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        retorno_esperado = Partida.cria(Jogador.jogadores)
        self.assertEqual(retorno_esperado, 1)

    def teste_01_funcao_finaliza_modulo_partida(self):
        print("Caso de Teste 01 Funcao Finaliza Partida- Funcao retorna -1 caso nao tenha partidas ativas")
        Partida.limpa_partidas()
        retorno_esperado = Partida.finaliza()
        self.assertEqual(retorno_esperado, -1)
    
    def teste_02_funcao_finaliza_modulo_partida(self):
        print("Caso de Teste 02 Funcao Finaliza Partida - Funcao retorna 1 caso tenha finalizado a partida")
        Partida.limpa_partidas()
        Jogador.limpa_jogadores()
        Jogador.cria("Joao")
        Jogador.cria("Pedro")
        Partida.cria(Jogador.jogadores)
        retorno_esperado = Partida.finaliza()
        self.assertEqual(retorno_esperado, 1)
    