import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import Arremesso
import Rodada
import recuperacao

__all__ = ["conecatarNoBD", "selecionaDados"]

jogadores = [(2,"maria"), (3, "clara")]
pontuacoesNomes = ['jogadaDeUm', 'jogadaDeDois', 'jogadaDeTres', 'jogadaDeQuatro', 'jogadaDeCinco', 'jogadaDeSeis', 'trinca', 'quadra', 'fullHouse', 'sequenciaAlta', 'sequenciaBaixa', 'general', 'jogadaAleatoria']
dados = [{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}]
partidaId = 1
arremessoCount = 0
rodadaCount = 1


pontuacoes = recuperacao.load()
global botaoJogarDados
global dice1
global dice2
global dice3
global dice4
global dice5
diceList = []
botaoJogarDadosState = NORMAL



def conecatarNoBD():
    connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='M0dul4rinf1301',
                                            database='yathzee')
    if connection.is_connected():
        return connection
    return -1

connection = conecatarNoBD()

def selecionaDados(dados):
    dadosSelecionados = []
    for dado in dados:
        if(dado["selecioado"] == 1):
            dadosSelecionados.append(dado)
    return dadosSelecionados

def selecionaDado(dado, num):
    dado.grid_forget()
    sel = dados[num]['selecionado']
    if(sel == 0):
        dado.grid(row=15, column=4+num, rowspan=4, sticky=N+S)
        dados[num]['selecionado'] = 1
    else:
        dado.grid(row=10, column=4+num, rowspan=4, sticky=N+S)
        dados[num]['selecionado'] = 0

def defineStatusDoBotaoJogarDados():
    
    if (arremessoCount == 3 ):
        return DISABLED
    return NORMAL 

def jogaDados(dados):
    global diceList
    global arremessoCount
    global botaoJogarDadosState
    global botaoJogarDados
    print('arremessoCount', arremessoCount)
    if (arremessoCount == 0):
        Rodada.cria( jogadorDaVez[0], partidaId,rodadaCount, connection)
    rodada = Rodada.pegaUltimaRodada(partidaId, jogadorDaVez[0], connection)
    lDadosAux = Rodada.handleRodada(rodada[0], dados, arremessoCount, connection)
    # exibe as possiveis pontuaçoes
    dados = lDadosAux
    clearDados(diceList)
    lAuxDiceList = handleDados(dados, diceList)
    diceList = lAuxDiceList
    arremessoCount += 1
    print('arremessoCount', arremessoCount)
    if (arremessoCount == 3 ):
        botaoJogarDados.grid_forget()
        botaoJogarDados = Button(janela,width=19, text="Jogar Dados", command=lambda: jogaDados(dados), state=DISABLED)
        botaoJogarDados.grid(row=15, column=0, columnspan=5, sticky=W)
        pontuacoesRodada = Rodada.pegaPontuacoesNaRodada(rodada[0], connection)
        desenhaTabelaPontuacoes(2, 14, pontuacoesRodada)
        arremessoCount = 0

   


def clearDados(diceList):
    for dice in diceList:
        dice.grid_forget()    


def handleRow(dado):
    if(dado["selecionado"] == 1):
        return 15
    return 10

def handleDados(dados, diceList):
    clearDados(diceList)
    dice1 = Button(janela, image = imgDados[dados[0]["valor"]-1], width=20, command= lambda: selecionaDado(dice1, 0))
    dice1.grid(row=handleRow(dados[0]), column=4, rowspan=4, sticky=N+S)
    dice2 = Button(janela, image = imgDados[dados[1]["valor"]-1], width=20, command= lambda: selecionaDado(dice2, 1))
    dice2.grid(row=handleRow(dados[1]), column=5, rowspan=4, sticky=N+S )
    dice3 = Button(janela, image = imgDados[dados[2]["valor"]-1], width=20, command= lambda: selecionaDado(dice3, 2))
    dice3.grid(row=handleRow(dados[2]), column=6, rowspan=4, sticky=N+S)
    dice4 = Button(janela, image = imgDados[dados[3]["valor"]-1], width=20, command= lambda: selecionaDado(dice4, 3))
    dice4.grid(row=handleRow(dados[3]), column=7 , rowspan=4, sticky=N+S)
    dice5 = Button(janela, image = imgDados[dados[4]["valor"]-1], width=20, command= lambda: selecionaDado(dice5, 4))
    dice5.grid(row=handleRow(dados[4]), column=8, rowspan=4 , sticky=N+S)
    return [dice1, dice2, dice3, dice4, dice5]
    # return diceList

def desenhaTabela(width, height):
    for i in range(height): #Rows
        for j in range(width): #Columns
            if (i==0):
                if (j==0):
                    b = Label(janela, text="Pontuações", width=20)
                else:
                    b = Label(janela, text=jogadores[j - 1][1], width=20)
            else:
                if (j==0):
                    b = Label(janela, text=pontuacoesNomes[i - 1], width=20)
                else:
                    pontuacaoJog = pontuacoes[jogadores[j - 1][0]][pontuacoesNomes[i - 1]]
                    b = Label(janela, text=pontuacaoJog, width=20)
            b.grid(row=i, column=j)

def pegaPontuacao(nome, pontuacoesPossiveis):
    if( pontuacoesPossiveis != {}):
        for tupla in pontuacoesPossiveis:
            if (nome == tupla[0]):
                return tupla[1]
    return 0

def desenhaTabelaPontuacoes(width, height, pontuacoesPossiveis):
    for i in range(height): #Rows
        print('i -1', i - 1)
        print('pontuacoes', pontuacoes)
        for j in range(9, width + 9): #Columns
            if (i==0):
                if (j==9):
                    b = Label(janela, text="Pontuações Possíveis", width=20)
                else:
                    b = Label(janela, text=jogadores[j - 10][1], width=20)
            else:
                if (j==9):
                    b = Label(janela, text=pontuacoesNomes[i - 1], width=20)
                else:
                    pontuacaoPossivel = pegaPontuacao(pontuacoesNomes[i - 1], pontuacoesPossiveis)
                    b = Label(janela, text=pontuacaoPossivel, width=20)
            b.grid(row=i, column=j)


janela = Tk()
janela.title('Yathzee')
janela["bg"] = 'green'
janela.geometry('1000x300')

height = 14
width = 3
desenhaTabela(width, height)
desenhaTabelaPontuacoes(2, height, {})
# for i in range(height): #Rows
#     for j in range(width): #Columns
#         if (i==0):
#             if (j==0):
#                 b = Label(janela, text="Pontuações", width=20)
#             else:
#                 b = Label(janela, text=jogadores[j - 1][1], width=20)
#         else:
#             if (j==0):
#                 b = Label(janela, text=pontuacoesNomes[i - 1], width=20)
#             else:
#                 pontuacaoJog = pontuacoes[jogadores[j - 1][0]][pontuacoesNomes[i - 1]]
#                 b = Label(janela, text=pontuacaoJog, width=20)
#         b.grid(row=i, column=j)

# desenhaDados(janela,[1,2,3,4,5])


# handleDados(dados)
imgDado1 = ImageTk.PhotoImage(Image.open('./Dice1.png').resize((60,60)))
imgDado2 = ImageTk.PhotoImage(Image.open('./Dice2.png').resize((60,60)))
imgDado3 = ImageTk.PhotoImage(Image.open('./Dice3.png').resize((60,60)))
imgDado4 = ImageTk.PhotoImage(Image.open('./Dice4.png').resize((60,60)))
imgDado5 = ImageTk.PhotoImage(Image.open('./Dice5.png').resize((60,60)))
imgDado6 = ImageTk.PhotoImage(Image.open('./Dice6.png').resize((60,60)))
imgDados = [imgDado1, imgDado2, imgDado3, imgDado4, imgDado5, imgDado6]

diceList = handleDados(dados,[])

jogadorDaVez = Rodada.defineJogadorDaVez(partidaId, jogadores, conecatarNoBD())
jogadorDaVezLabel = Label(janela, text="Está na vez do(a):"+jogadorDaVez[1], width=20)
jogadorDaVezLabel.grid(row=14,column=0)
botaoJogarDados = Button(janela,width=19, text="Jogar Dados", command=lambda: jogaDados(dados))
botaoJogarDados.grid(row=15, column=0, columnspan=5, sticky=W)
dadosSelecionadosTexto =  Label(janela, text="Dados Selecionados")
dadosSelecionadosTexto.grid(row=14,column=2)

janela.mainloop()
    