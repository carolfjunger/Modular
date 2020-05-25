import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='M0dul4rinf1301')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE yathzee")
            cursor.execute("use yathzee")
            db_Info = connection.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)
            cursor.execute("select database()")
            record = cursor.fetchone()
            print("Conectado ao banco de dados ", record)
            cursor.execute(" CREATE TABLE jogadores (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,  nome VARCHAR(40) NOT NULL, totalDepontos INT(6) default null); CREATE TABLE partidas ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,ativa boolean default true );CREATE TABLE jogador_na_partida (jogador_id INT(6) UNSIGNED,partida_id INT(6) UNSIGNED,CONSTRAINT fk_JogadorNaPartida FOREIGN KEY (jogador_id) REFERENCES jogadores(id),CONSTRAINT fk_PartidaJogador FOREIGN KEY (partida_id) REFERENCES partidas(id) ,campeao bool default false);CREATE TABLE rodadas (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,jogador_id INT(6) UNSIGNED,CONSTRAINT fk_JogadorNaRodada FOREIGN KEY (jogador_id) REFERENCES jogadores(id),numero tinyint,ativa bool);CREATE TABLE possiveis_pontuaçoes_na_rodada (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,rodada_id INT(6) UNSIGNED,CONSTRAINT fk_RodadaPontuacoes FOREIGN KEY (rodada_id) REFERENCES rodadas(id),pontuacaoName varchar(20) not null,pontuacaoValor tinyint not null);")
    except Error as e:
        print("Erro de conexão", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    main()