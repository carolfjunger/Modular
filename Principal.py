import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from ConectarBD import conecatarNoBD
import Arremesso
import Rodada
import Cartela 
import recuperacao
import Partida

__all__ = ["conecatarNoBD", "selecionaDados"]

jogadores = [(2,"maria"), (3, "clara")]
pontuacoesNomes = ['jogadaDeUm', 'jogadaDeDois', 'jogadaDeTres', 'jogadaDeQuatro', 'jogadaDeCinco', 'jogadaDeSeis', 'trinca', 'quadra', 'fullHouse', 'sequenciaAlta', 'sequenciaBaixa', 'general', 'jogadaAleatoria']
dados = [{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}]
partidaId = 10
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
        statusRodadaCria = Rodada.cria( jogadorDaVez[0], partidaId,rodadaCount, connection)
        if(statusRodadaCria != 1):
            resposta = messagebox.showerror('ERRO', 'erro rodada cria'+str(statusRodadaCria))
            if(resposta == 'ok'):
                janela.destroy()
    rodada = Rodada.pegaUltimaRodada(partidaId, jogadorDaVez[0], connection)
    lDadosAux = Rodada.handleRodada(rodada[0], dados, arremessoCount, connection)
    # exibe as possiveis pontuaçoes
    dados = lDadosAux
    clearDados(diceList)
    lAuxDiceList = handleDados(dados, diceList)
    diceList = lAuxDiceList
    arremessoCount += 1
    print('rodadaCount', rodadaCount)
    if (arremessoCount == 3 ):
        botaoJogarDados.grid_forget()
        botaoJogarDados = Button(janela,width=19, text="Jogar Dados", command=lambda: jogaDados(dados), state=DISABLED)
        botaoJogarDados.grid(row=15, column=0, columnspan=5, sticky=W)
        pontuacoesRodada = Rodada.pegaPontuacoesNaRodada(rodada[0], connection)
        desenhaTabelaPontuacoes(2, 14, pontuacoesRodada, False, jogadorDaVez)
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
            b.grid(row=i, column=j, sticky=N+S)

def pegaPontuacao(nome, pontuacoesPossiveis):
    if( pontuacoesPossiveis != {}):
        for tupla in pontuacoesPossiveis:
            if (nome == tupla[0]):
                return tupla[1]
    return 0

def defineStatusBotaoPontuacao(posicaoCartela, primeira, jogadorId):
    taLivre = Cartela.verificaSePontuacaoEstaDisponivel(jogadorId,posicaoCartela)

    if (primeira or taLivre == False):
        return DISABLED
    return NORMAL

def handleFimDeJogo():
    jogadoresIds = []
    for jogador in jogadores:
        Cartela.somaPontuacao(jogador[0], connection)
        jogadoresIds.append(jogador[0])
    statusPartidaFinaliza = Partida.finaliza(partidaId, connection)
    if(statusPartidaFinaliza == 1):
        jogCampeao = Partida.pegaJogadorCampeao(partidaId, connection)
        message = "A(o) campeã(o) foi "+jogCampeao[0]+" e fez "+str(jogCampeao[1])+' pontos'
        resposta = messagebox.showinfo('FIM DE JOGO', message)
        if(resposta == 'ok'):
            janela.destroy()

def handlePreencheCartela(joagdorId, pontuacaoNome, pontos, novaRodada):
    global pontuacoes
    global arremessoCount
    global jogadorDaVez
    global rodadaCount
    global botaoJogarDados
    print('pontuacaoNome **', pontuacaoNome)
    preenche = Cartela.preenche(joagdorId, pontuacaoNome, pontos)
    print('preenche', preenche)
    if(preenche == 1):
        desenhaTabelaPontuacoes(width, height, {}, True, jogadorDaVez)
        pontuacoes = recuperacao.load()
        desenhaTabela(3, 14)
        arremessoCount = 0
        jogadorDaVez = Rodada.defineJogadorDaVez(partidaId, jogadores, connection)
        print('jogadorDaVez',jogadorDaVez)
        if(joagdorId == jogadores[1][0]):
            rodadaCount += 1
            if(rodadaCount > 13):
                handleFimDeJogo()
        jogadorDaVezLabel = Label(janela, text="Está na vez do(a):"+jogadorDaVez[1], width=20)
        jogadorDaVezLabel.grid(row=14,column=0)
        botaoJogarDados = Button(janela,width=19, text="Jogar Dados", command=lambda: jogaDados(dados), state=NORMAL)
        botaoJogarDados.grid(row=15, column=0, columnspan=5, sticky=W)
        


def desenhaTabelaPontuacoes(width, height, pontuacoesPossiveis, primeira, jogadorDaVez):

    for i in range(height): #Rows
        for j in range(9, width + 9): #Columns
            if (i==0):
                if (j==9):
                    b = Label(janela, text="Pontuações Possíveis", width=20)
                    b.grid(row=i, column=j, sticky=N+S+E+W )
                else:
                    b = Label(janela, text=jogadores[j - 10][1], width=20)
                    b.grid(row=i, column=10, sticky=N+S+E+W )
            else:
                if (j==9):
                    b = Label(janela, text=pontuacoesNomes[i - 1], width=20)
                    b.grid(row=i, column=j, sticky=N+S )
            
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeUm', primeira,jogadorDaVez[0])
    btJogadaDeUm = Button(janela, text= pegaPontuacao('jogadaDeUm', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeUm', pegaPontuacao('jogadaDeUm', pontuacoesPossiveis), jogadorDaVez) )
    btJogadaDeUm.grid(row=1, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeDois', primeira,jogadorDaVez[0])
    btJogadaDeDois = Button(janela, text=pegaPontuacao('jogadaDeDois', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeDois', pegaPontuacao('jogadaDeDois', pontuacoesPossiveis), jogadorDaVez) )
    btJogadaDeDois.grid(row=2, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeTres', primeira,jogadorDaVez[0])
    btJogadaDeTres = Button(janela, text=pegaPontuacao('jogadaDeTres', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeTres', pegaPontuacao('jogadaDeTres', pontuacoesPossiveis), jogadorDaVez) )
    btJogadaDeTres.grid(row=3, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeQuatro', primeira,jogadorDaVez[0])
    btjogadaDeQuatro = Button(janela, text=pegaPontuacao('jogadaDeQuatro', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeQuatro', pegaPontuacao('jogadaDeQuatro', pontuacoesPossiveis), jogadorDaVez) )
    btjogadaDeQuatro.grid(row=4, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeCinco', primeira,jogadorDaVez[0])
    btjogadaDeCinco = Button(janela, text=pegaPontuacao('jogadaDeCinco', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeCinco', pegaPontuacao('jogadaDeCinco', pontuacoesPossiveis), jogadorDaVez) )
    btjogadaDeCinco.grid(row=5, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaDeSeis', primeira,jogadorDaVez[0])
    btjogadaDeSeis = Button(janela, text=pegaPontuacao('jogadaDeSeis', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaDeSeis', pegaPontuacao('jogadaDeSeis', pontuacoesPossiveis), jogadorDaVez) )
    btjogadaDeSeis.grid(row=6, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('trinca', primeira,jogadorDaVez[0])
    bttrinca = Button(janela, text=pegaPontuacao('trinca', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'trinca', pegaPontuacao('trinca', pontuacoesPossiveis), jogadorDaVez) )
    bttrinca.grid(row=7, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('quadra', primeira,jogadorDaVez[0])
    btquadra = Button(janela, text=pegaPontuacao('quadra', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'quadra', pegaPontuacao('quadra', pontuacoesPossiveis), jogadorDaVez) )
    btquadra.grid(row=8, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('fullHouse', primeira,jogadorDaVez[0])
    btfullHouse = Button(janela, text=pegaPontuacao('fullHouse', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'fullHouse', pegaPontuacao('fullHouse', pontuacoesPossiveis), jogadorDaVez) )
    btfullHouse.grid(row=9, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('sequenciaAlta', primeira,jogadorDaVez[0])
    btsequenciaAlta = Button(janela, text=pegaPontuacao('sequenciaAlta', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'sequenciaAlta', pegaPontuacao('sequenciaAlta', pontuacoesPossiveis), jogadorDaVez) )
    btsequenciaAlta.grid(row=10, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('sequenciaBaixa', primeira,jogadorDaVez[0])
    btsequenciaBaixa = Button(janela, text=pegaPontuacao('sequenciaBaixa', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'sequenciaBaixa', pegaPontuacao('sequenciaBaixa', pontuacoesPossiveis), jogadorDaVez) )
    btsequenciaBaixa.grid(row=11, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('general', primeira,jogadorDaVez[0])
    btgeneral = Button(janela, text=pegaPontuacao('general', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'general', pegaPontuacao('general', pontuacoesPossiveis), jogadorDaVez) )
    btgeneral.grid(row=12, column=10, sticky=N+S+E+W)
    statusBotaoPontuacao = defineStatusBotaoPontuacao('jogadaAleatoria', primeira,jogadorDaVez[0])
    btjogadaAleatoria = Button(janela, text=pegaPontuacao('jogadaAleatoria', pontuacoesPossiveis), width=20, state=statusBotaoPontuacao, command=lambda: handlePreencheCartela(jogadorDaVez[0], 'jogadaAleatoria', pegaPontuacao('jogadaAleatoria', pontuacoesPossiveis), jogadorDaVez) )
    btjogadaAleatoria.grid(row=13, column=10, sticky=N+S+E+W)




janela = Tk()
janela.title('Yathzee')
janela["bg"] = 'green'
janela.geometry('1000x500')

if(pontuacoes == -1):
    resposta = messagebox.showerror('ERRO', 'erro ao carregar o xml')
    if(resposta == 'ok'):
        janela.destroy()


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
height = 14
width = 3
desenhaTabela(width, height)
desenhaTabelaPontuacoes(2, height, {}, True, jogadorDaVez)

janela.mainloop()
    