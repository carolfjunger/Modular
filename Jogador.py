
__all__ = ["cria", "limpa_jogadores"]

jogadores = []

def cria (nome):
    if (nome == "" or type(nome) != str ):
        return -1
    for jog in jogadores:
        if (jog["nome"] == nome):
            return -1
    index = len(jogadores) - 1
    if (index > 0):
        lastId = jogadores[len(jogadores) - 1]["id"]
    else:
        lastId = -1
    jogador = { "id": lastId + 1, "nome": nome, "totalDePontos": 0, "rodadas": []}
    jogadores.append(jogador)
    return 1

def limpa_jogadores ():
    while(jogadores != []):
        jogadores.pop()

