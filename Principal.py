import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import Arremesso

__all__ = ["conecatarNoBD", "selecionaDados"]

jogadores = ["maria", "clara"]
pontuacoes = ['jogadaDeUm', 'jogadaDeDois', 'jogadaDeTres', 'jogadaDeQuatro', 'jogadaDeCinco', 'jogadaDeSeis', 'trinca', 'quadra', 'fullHouse', 'sequenciaAlta', 'sequenciaBaixa', 'general', 'jogadaAleatoria']
dados = [{ "valor": 1, "selecionado": 0}, { "valor": 2, "selecionado": 0}, { "valor": 3, "selecionado": 0}, { "valor": 4, "selecionado": 0}, { "valor": 5, "selecionado": 0}]
global dice1
global dice2
global dice3
global dice4
global dice5
diceList = []


#funcao a ser implementada quando formos fazer a interface
# dados = [1,2,3,4,5]
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
    

def jogaDados(dados):
    global diceList
    lDadosAux = Arremesso.arremessa(dados)
    dados = lDadosAux
    clearDados(diceList)
    lAuxDiceList = handleDados(dados, diceList)
    diceList = lAuxDiceList

def conecatarNoBD():
    connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='M0dul4rinf1301',
                                            database='yathzee')
    if connection.is_connected():
        return connection
    return -1

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

janela = Tk()
janela.title('Yathzee')
janela["bg"] = 'green'
janela.geometry('1000x300')

height = 14
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
        if (i==0):
            if (j==0):
                b = Label(janela, text="Pontuações", width=20)
            else:
                b = Label(janela, text=jogadores[j - 1], width=20)
        else:
            if (j==0):
                b = Label(janela, text=pontuacoes[i - 1], width=20)
            else:
                b = Label(janela, text="", width=20)
        b.grid(row=i, column=j)

# desenhaDados(janela,[1,2,3,4,5])
imgDado1 = ImageTk.PhotoImage(Image.open('./Dice1.png').resize((60,60)))
imgDado2 = ImageTk.PhotoImage(Image.open('./Dice2.png').resize((60,60)))
imgDado3 = ImageTk.PhotoImage(Image.open('./Dice3.png').resize((60,60)))
imgDado4 = ImageTk.PhotoImage(Image.open('./Dice4.png').resize((60,60)))
imgDado5 = ImageTk.PhotoImage(Image.open('./Dice5.png').resize((60,60)))
imgDado6 = ImageTk.PhotoImage(Image.open('./Dice6.png').resize((60,60)))
imgDados = [imgDado1, imgDado2, imgDado3, imgDado4, imgDado5, imgDado6]

# handleDados(dados)


diceList = handleDados(dados,[])

jogadorDaVez = jogadores[0]
jogadorDaVezLabel = Label(janela, text="Está na vez do(a):"+jogadorDaVez)
jogadorDaVezLabel.grid(row=7,column=5, columnspan=5)
bt = Button(janela,width=20, text="Jogar Dados", command=lambda: jogaDados(dados))
bt.grid(row=7, column=10, columnspan=5)
dadosSelecionadosTexto =  Label(janela, text="Dados Selecionados")
dadosSelecionadosTexto.grid(row=15,column=1, columnspan=5)

janela.mainloop()
    