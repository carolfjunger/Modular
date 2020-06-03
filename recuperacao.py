# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:27:14 2020

@author: Usuario
"""

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom


def formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def inicializa(lJogadores):
    
    jogadores = Element('jogadores')
    
    for jog in lJogadores:
        
        jogador = SubElement(jogadores, 'jogador')
        jogador.text = str(jog)
        
        jogadaDeUm = SubElement(jogador,'jogadaDeUm')
        jogadaDeUm.text = "-1"
        
        jogadaDeDois = SubElement(jogador, 'jogadaDeDois')
        jogadaDeDois.text = "-1"
        
        jogadaDeTres = SubElement(jogador, 'jogadaDeTres')
        jogadaDeTres.text = "-1"
        
        jogadaDeQuatro = SubElement(jogador, 'jogadaDeQuatro')
        jogadaDeQuatro.text = "-1"
        
        jogadaDeCinco = SubElement(jogador, 'jogadaDeCinco')
        jogadaDeCinco.text = "-1"
        
        jogadaDeSeis = SubElement(jogador, 'jogadaDeSeis')
        jogadaDeSeis.text = "-1"
        
        trinca = SubElement(jogador, 'trinca')
        trinca.text = "-1"
        
        quadra = SubElement(jogador, 'quadra')
        quadra.text = "-1"
        
        fullHouse = SubElement(jogador, 'fullHouse')
        fullHouse.text = "-1"
        
        sequenciaBaixa = SubElement(jogador, 'sequenciaBaixa')
        sequenciaBaixa.text = "-1"
        
        sequenciaAlta = SubElement(jogador,'sequenciaAlta')
        sequenciaAlta.text = "-1"
        
        general = SubElement(jogador, 'general')
        general.text = "-1"
        
        jogadaAleatoria = SubElement(jogador,'jogadaAleatoria')
        jogadaAleatoria.text = "-1"


    nome_arquivo = 'recuperacao.xml'
    with open (nome_arquivo, 'w') as file_object:
        file_object.write(formata_saida(jogadores))
        
def save(dicJogo):
    jogadores = Element('jogadores')
    
    for jog in dicJogo:
        jogador = SubElement(jogadores, 'jogador')
        jogador.text = str(jog) 
        
        jogadaDeUm = SubElement(jogador,'jogadaDeUm')
        jogadaDeUm.text = dicJogo[jog]['jogadaDeUm']
        
        jogadaDeDois = SubElement(jogador, 'jogadaDeDois')
        jogadaDeDois.text = dicJogo[jog]['jogadaDeDois']
        
        jogadaDeTres = SubElement(jogador, 'jogadaDeTres')
        jogadaDeTres.text = dicJogo[jog]['jogadaDeTres']
        
        jogadaDeQuatro = SubElement(jogador, 'jogadaDeQuatro')
        jogadaDeQuatro.text = dicJogo[jog]['jogadaDeQuatro']
        
        jogadaDeCinco = SubElement(jogador, 'jogadaDeCinco')
        jogadaDeCinco.text = dicJogo[jog]['jogadaDeCinco']
        
        jogadaDeSeis = SubElement(jogador, 'jogadaDeSeis')
        jogadaDeSeis.text = dicJogo[jog]['jogadaDeSeis']
        
        trinca = SubElement(jogador, 'trinca')
        trinca.text = dicJogo[jog]['trinca']
        
        quadra = SubElement(jogador, 'quadra')
        quadra.text = dicJogo[jog]['quadra']
        
        fullHouse = SubElement(jogador, 'fullHouse')
        fullHouse.text = dicJogo[jog]['fullHouse']
        
        sequenciaBaixa = SubElement(jogador, 'sequenciaBaixa')
        sequenciaBaixa.text = dicJogo[jog]['sequenciaBaixa']
        
        sequenciaAlta = SubElement(jogador,'sequenciaAlta')
        sequenciaAlta.text = dicJogo[jog]['sequenciaAlta']
        
        general = SubElement(jogador, 'general')
        general.text = dicJogo[jog]['general']
        
        jogadaAleatoria = SubElement(jogador,'jogadaAleatoria')
        jogadaAleatoria.text = dicJogo[jog]['jogadaAleatoria']


    nome_arquivo = 'recuperacao.xml'
    with open (nome_arquivo, 'w') as file_object:
        file_object.write(formata_saida(jogadores))
 
    
def load():
    with open('recuperacao.xml', 'rt') as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
        
    dict_jogadores = {}
    
    for jogador in root.findall('jogador'):
        dict_auxiliar = {}
        dict_auxiliar['jogadaDeUm'] = (jogador.find('jogadaDeUm').text)
        dict_auxiliar['jogadaDeDois'] = (jogador.find('jogadaDeDois').text)
        dict_auxiliar['jogadaDeTres'] = (jogador.find('jogadaDeTres').text)
        dict_auxiliar['jogadaDeQuatro'] = (jogador.find('jogadaDeQuatro').text)
        dict_auxiliar['jogadaDeCinco'] = (jogador.find('jogadaDeCinco').text)
        dict_auxiliar['jogadaDeSeis'] = (jogador.find('jogadaDeSeis').text)
        dict_auxiliar['trinca'] = (jogador.find('trinca').text)
        dict_auxiliar['quadra'] = (jogador.find('quadra').text)
        dict_auxiliar['fullHouse'] = (jogador.find('fullHouse').text)
        dict_auxiliar['sequenciaBaixa'] = (jogador.find('sequenciaBaixa').text)
        dict_auxiliar['sequenciaAlta'] = (jogador.find('sequenciaAlta').text)
        dict_auxiliar['general'] = (jogador.find('general').text)
        dict_auxiliar['jogadaAleatoria'] = (jogador.find('jogadaAleatoria').text)
        dict_jogadores[int(jogador.text)] = dict_auxiliar
        
    return dict_jogadores