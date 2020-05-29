# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:27:14 2020

@author: Usuario
"""
import Cartela
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

def formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def save(listaCartelas):
    cartelas = Element('cartelas')
    
    for cart in listaCartelas:
        pontuacoes = cart['pontuacoes']
        
        cartela = SubElement(cartelas, 'cartela')
        cartela.text = cart['jogadorId']
        
        jogadaDeUm = SubElement(cartela,'jogadaDeUm')
        jogadaDeUm.text = str(pontuacoes['jogadaDeUm'])
        
        jogadaDeDois = SubElement(cartela, 'jogadaDeDois')
        jogadaDeDois.text = str(pontuacoes['jogadaDeDois'])
        
        jogadaDeTres = SubElement(cartela, 'jogadaDeTres')
        jogadaDeTres.text = str(pontuacoes['jogadaDeTres'])
        
        jogadaDeQuatro = SubElement(cartela, 'jogadaDeQuatro')
        jogadaDeQuatro.text = str(pontuacoes['jogadaDeQuatro'])
        
        jogadaDeCinco = SubElement(cartela, 'jogadaDeCinco')
        jogadaDeCinco.text = str(pontuacoes['jogadaDeCinco'])
        
        jogadaDeSeis = SubElement(cartela, 'jogadaDeSeis')
        jogadaDeSeis.text = str(pontuacoes['jogadaDeSeis'])
        
        trinca = SubElement(cartela, 'trinca')
        trinca.text = str(pontuacoes['trinca'])
        
        quadra = SubElement(cartela, 'quadra')
        quadra.text = str(pontuacoes['quadra'])
        
        fullHouse = SubElement(cartela, 'fullHouse')
        fullHouse.text = str(pontuacoes['fullHouse'])
        
        sequenciaBaixa = SubElement(cartela, 'sequenciaBaixa')
        sequenciaBaixa.text = str(pontuacoes['sequenciaBaixa'])
        
        sequenciaAlta = SubElement(cartela,'sequenciaAlta')
        sequenciaAlta.text = str(pontuacoes['sequenciaAlta'])
        
        general = SubElement(cartela, 'general')
        general.text = str(pontuacoes['general'])
        
        jogadaAleatoria = SubElement(cartela,'jogadaAleatoria')
        jogadaAleatoria.text = str(pontuacoes['jogadaAleatoria'])


    nome_arquivo = 'recuperacao.xml'
    with open (nome_arquivo, 'w') as file_object:
        file_object.write(formata_saida(cartelas))
        
def load():
    with open('recuperacao.xml', 'rt') as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
        
    lista_cartelas = []
    
    for cartela in root.findall('cartela'):
        dict_cartela = {}
        dict_cartela['jogadaDeUm'] = int(cartela.find('jogadaDeUm').text)
        dict_cartela['jogadaDeDois'] = int(cartela.find('jogadaDeDois').text)
        dict_cartela['jogadaDeTres'] = int(cartela.find('jogadaDeTres').text)
        dict_cartela['jogadaDeQuatro'] = int(cartela.find('jogadaDeQuatro').text)
        dict_cartela['jogadaDeCinco'] = int(cartela.find('jogadaDeCinco').text)
        dict_cartela['jogadaDeSeis'] = int(cartela.find('jogadaDeSeis').text)
        dict_cartela['trinca'] = int(cartela.find('trinca').text)
        dict_cartela['quadra'] = int(cartela.find('quadra').text)
        dict_cartela['fullHouse'] = int(cartela.find('fullHouse').text)
        dict_cartela['sequenciaBaixa'] = int(cartela.find('sequenciaBaixa').text)
        dict_cartela['sequenciaAlta'] = int(cartela.find('sequenciaAlta').text)
        dict_cartela['general'] = int(cartela.find('general').text)
        dict_cartela['jogadaAleatoria'] = int(cartela.find('jogadaAleatoria').text)
        
        lista_cartelas.append(dict_cartela)
        
        
    return lista_cartelas
    
