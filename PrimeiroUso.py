# -*- coding: utf-8 -*-
'''
    Nome: Primeiro uso
    Descriçao: Modulo responsavel por criar as tabelas e o banco de dados
    Autores: ACJ - Ana Carolina Junger
    Historico de evolucao:
        Autor         Versao            Data              Observacao
        ACJ             1               24/05/2020          criacao do arquivo
        ACJ             2               30/05/2020          alteracao na tabelas       
'''
import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='root')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE yathzee")
            cursor.execute("use yathzee")
            db_Info = connection.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)
            cursor.execute("select database()")
            record = cursor.fetchone()
            print("Conectado ao banco de dados ", record)
            print("Criando tabela JOGADORES")
            cursor.execute("CREATE TABLE jogadores (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,  nome VARCHAR(40) NOT NULL, totalDepontos INT(6) default null);")
            print("Criando tabela PARTIDAS")
            cursor.execute("CREATE TABLE partidas ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,ativa boolean  );")
            print("Criando tabela JOGADOR_NA_PARTIDA")
            cursor.execute("CREATE TABLE jogador_na_partida (jogador_id INT(6) UNSIGNED,partida_id INT(6) UNSIGNED,CONSTRAINT fk_JogadorNaPartida FOREIGN KEY (jogador_id) REFERENCES jogadores(id),CONSTRAINT fk_PartidaJogador FOREIGN KEY (partida_id) REFERENCES partidas(id) ,campeao bool default false);")
            print("Criando tabela RODADAS")
            cursor.execute("CREATE TABLE rodadas (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,jogador_id INT(6) UNSIGNED,CONSTRAINT fk_JogadorNaRodada FOREIGN KEY (jogador_id) REFERENCES jogadores(id),numero tinyint, partida_id INT(6) UNSIGNED,CONSTRAINT fk_PartidaRodada FOREIGN KEY (partida_id) REFERENCES partidas(id));")
            print("Criando tabela POSSIVEIS PONTUAÇÕES")
            cursor.execute("CREATE TABLE possiveis_pontuaçoes_na_rodada (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,rodada_id INT(6) UNSIGNED,CONSTRAINT fk_RodadaPontuacoes FOREIGN KEY (rodada_id) REFERENCES rodadas(id),pontuacaoName varchar(20) not null,pontuacaoValor tinyint not null);")
    except Error as e:
        print("Erro de conexão", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    main()