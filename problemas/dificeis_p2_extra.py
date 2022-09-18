import random

def criaTabela (tabuleiro, x, y):
  tabela = []
  for linha in tabuleiro:
    tabela.append([])
    for casa in linha:
      tabela[-1].append([4, casa])
  tabela[y][x] = [5, tabela[y][x][1]]
  return tabela

def check(y, x, pecas, tabuleiro):
  # categoria 0: casa vazia em area de ataque
  # categoria 1: bloqueio
  # categoria 2: area de ataque
  # categoria 3: fora do trabuleiro
  # categoria 4: area vazia fora da area de ataque
  # categoria 5: peca em analise
  if 0 > x or x > 7 or 0 > y or y > 7: return [3, [x, y], ""]
  cs = tabuleiro[y][x]
  if pecas.find(cs) != -1: return [2, [x, y], cs]
  elif cs == '.': return [0, [x, y], cs]
  else: return [1, [x, y], cs]

def expansao(linha, coluna, pecas, tabuleiro, tabela):
  for i in range(1, 8):
    [categoria, [x, y], casa] = check(linha(i), coluna(i), pecas, tabuleiro)
    if categoria != 3: 
      tabela[y][x] = [categoria, casa]
      if categoria == 2: return [[x, y], casa]
      elif categoria: return False
    else: return False
    

def direcionado(coordenadas, pecas, tabuleiro, tabela):
  for [linha, coluna] in coordenadas:
    [categoria, [x, y], casa] = check(linha, coluna, pecas, tabuleiro)
    if categoria == 2: 
      tabela[y][x] = [categoria, casa]
      return [[x, y], casa]
    return False

def imprimeTabela (tabela, x, y, tabuleiro):
  print(f"Peça {tabuleiro[y][x]} ({x}, {y})")
  print("\n\x1b[30m  1 2 3 4 5 6 7 8")
  for index, linha in enumerate(tabela):
    sequencia = f"\x1b[30m{index}"
    for [categoria, casa] in linha:
      match categoria:
        case 0: sequencia += f" \x1b[31m{casa}"
        case 1: sequencia += f" \x1b[34m{casa}"
        case 2: sequencia += f" \x1b[31m{casa}"
        case 4: sequencia += f" \x1b[30m{casa}"
        case 5: sequencia += f" \x1b[32m{casa}"
    print(sequencia)
  print("\n\x1b[m")

def mapear(x, y, tabuleiro, isMaiusculo = False):
  tabela = criaTabela(tabuleiro, x, y)
  mapa = {}

  pecas = ["RQ", "BQ", "P", "N"]
  if isMaiusculo: pecas = list(map(lambda peca: peca.lower(), pecas))
  mapa["norte"]    = expansao(lambda i: y - i, lambda i: x,     pecas[0], tabuleiro, tabela)
  mapa["sul"]      = expansao(lambda i: y + i, lambda i: x,     pecas[0], tabuleiro, tabela)
  mapa["leste"]    = expansao(lambda i: y,     lambda i: x + i, pecas[0], tabuleiro, tabela)
  mapa["oeste"]    = expansao(lambda i: y,     lambda i: x - i, pecas[0], tabuleiro, tabela)
  mapa["noroeste"] = expansao(lambda i: y - i, lambda i: x - i, pecas[1], tabuleiro, tabela)
  mapa["nordeste"] = expansao(lambda i: y - i, lambda i: x + i, pecas[1], tabuleiro, tabela)
  mapa["sudoeste"] = expansao(lambda i: y + i, lambda i: x - i, pecas[1], tabuleiro, tabela)
  mapa["sudeste"]  = expansao(lambda i: y + i, lambda i: x + i, pecas[1], tabuleiro, tabela)

  mapa["peao"]   = (direcionado([[y+1, x+1], [y+1, x-1]], pecas[2], tabuleiro, tabela)) # peao
  mapa["cavalo"] = (direcionado([
    [y-2, x+1], [y-2, x-1], [y+2, x+1], [y+2, x-1], 
    [y+1, x-2], [y+1, x+2], [y-1, x+2],  [y-1, x-2]], 
    pecas[3], tabuleiro, tabela)) # cavalo

  imprimeTabela(tabela, x, y, tabuleiro)
  return mapa


def imprimeResultado (resposta):
  nomes = { "k": "rei", "p": "peão", "b": "bispo", "r": "torre", "q": "rainha", "n": "cavalo" }
  xeque = { "branco": False, "preto": False }
  for peca in resposta:
    for orientacao in resposta[peca]:
      mapa = resposta[peca][orientacao]
      if mapa:
        chave = peca.split('_')
        coordenada = f"{chave[0][0]}, {chave[0][1]}"
        nome = f"{nomes[chave[1].lower()]} {'preto' if chave[1].islower() else 'branco'}"
        ataque = f"({mapa[0][0]}, {mapa[0][1]}) [ {(nomes[mapa[1].lower()]):7} ]"
        print(f"({coordenada}) [ {nome:13} ] está sobre ataque do {ataque} na direção {orientacao}")
        if nome == "rei preto": xeque["preto"] = True
        if nome == "rei branco": xeque["branco"] = True
  print('\n\x1b[31m')
  if xeque['preto'] and xeque['branco']: print("Ambos os reis estão em cheque") 
  elif xeque['preto']: print("Rei preto está em cheque") 
  elif xeque['branco']: print("Rei branco está em cheque") 
  else: print("\x1b[32mNenhum rei esta em cheque")
  print('\n\x1b[m')

def main():
  while True:
    tabuleiro = []
    resultado = {}
    estaVazio = True
    for i in range(0, 8): tabuleiro.append(input(f"{i + 1}: "))
    for y, linha in enumerate(tabuleiro):
      for x, casa in enumerate(linha):
        if casa != '.': 
          estaVazio = False
          resultado[f"{x}{y}_{casa}"] = mapear(x, y, tabuleiro, casa.isupper())
    imprimeResultado(resultado)
    if estaVazio: break

main()

def pecasAleatorias():
  pecas = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'r', 'r', 'b', 'b', 'n', 'n']
  random.shuffle(pecas)
  pecas = pecas[0: random.randint(0, 15)]
  pecas.append('k')
  return pecas

def tabuleiroAleatorio ():
  tabuleiro = [
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
    [".",".",".",".",".",".",".", "."],
  ]

  coordenadas = []
  for y in range(0, 7):
    for x in range(0, 7): coordenadas.append([x, y])
  random.shuffle(coordenadas)
  pecas = pecasAleatorias() + list(map(lambda p: p.upper(), pecasAleatorias()))
  random.shuffle(pecas)
  
  for i, peca in enumerate(pecas):
    x = int(coordenadas[i][0])
    y = int(coordenadas[i][1])
    tabuleiro[y][x] = peca

  for i, linha in enumerate(tabuleiro):
    tabuleiro[i] = ''.join(linha)

  print("\n  1 2 3 4 5 6 7 8")
  for i, linha in enumerate(tabuleiro):
    sequencia = f"{i} "
    for casa in linha:
      sequencia += f" {casa}"
    print(sequencia)
  
  print()
  return tabuleiro

def teste():
  while True:
    resultado = {}
    tabuleiro = tabuleiroAleatorio()
    for y, linha in enumerate(tabuleiro):
      for x, casa in enumerate(linha):
        if casa != '.': 
          resultado[f"{x}{y}_{casa}"] = mapear(x, y, tabuleiro, casa.isupper())
    imprimeResultado(resultado)

    if not int(input("Continuar [0/1]:")): break

# teste()
