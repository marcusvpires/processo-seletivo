def main():
  jogo = [
    "..k.....",
    "ppp.pppp",
    "........",
    ".R...B..",
    "........",
    "........",
    "PPPPPPPP",
    "K......."
  ]
  # for i in range(0, 8): jogo.append(input(f"{i + 1}: "))

  for l, linha in enumerate(jogo):
    for c, casa in enumerate(linha):
      if casa != '.': tabelaDeAtaque(l, c, jogo, casa.isupper())

def tabelaDeAtaque(l, c, jogo, preto = False):
  tabela = [[],[],[],[],[],[],[],[]]
  for index, tLinha in enumerate(jogo):
    for tCasa in tLinha: 
      tabela[index].append([1, tCasa])

  def check(y, x, ataque):
    if 0 > x or x > 7 or 0 > y or y > 7: return [3, [x, y], ""]
    cs = jogo[y][x]
    if ataque.find(cs) != -1: return [2, [x, y], cs]
    elif cs == '.': return [0, [x, y], cs]
    else: return [1, [x, y], cs]

  def expansao(linha, coluna, ataque, id):
    if preto: ataque = ataque.lower()
    for i in range(1, 8):
      [status, [x, y], casa] = check(linha(i), coluna(i), ataque)
      # print(f"{id:<2} {status} ({x:0>2}, {y:0>2}) {casa}")
      if status != 3: tabela[y][x] = [status, casa]
      if status: return False

  def especifico(cods, ataque, id):
    if preto: ataque = ataque.lower()
    for [linha, coluna] in cods:
      [status, [x, y], casa] = check(linha, coluna, ataque)
      # print(f"{id:<2} {status} ({x:0>2}, {y:0>2}) {casa}")
      if status == 2: tabela[y][x] = [status, casa]
  
  expansao(lambda i: l,     lambda i: c - i, "RQ", "o" )
  expansao(lambda i: l - i, lambda i: c - i, "BQ", "no")
  expansao(lambda i: l - i, lambda i: c,     "RQ", "n" )
  expansao(lambda i: l - i, lambda i: c + i, "BQ", "nl")
  expansao(lambda i: l,     lambda i: c + i, "RQ", "l" )
  expansao(lambda i: l + i, lambda i: c + i, "BQ", "sl")
  expansao(lambda i: l + i, lambda i: c,     "RQ", "s" )
  expansao(lambda i: l + i, lambda i: c - i, "BQ", "so")

  especifico([[l+1, c+1], [l+1, c-1]], "P", "p")
  especifico([
    [l-2, c+1], [l-2, c-1], [l+2, c+1], [l+2, c-1], 
    [l+1, c-2], [l+1, c+2], [l-1, c+2],  [l-1, c-2]], 
    "N", "n")

  print(f"Peça {jogo[l][c]}")
  print("\n\x1b[38m  1 2 3 4 5 6 7 8")
  for index, linha in enumerate(tabela):
    sequencia = f"\x1b[37m{index}"
    for [categoria, casa] in linha:
      match categoria:
        case 0: sequencia += f" \x1b[33m{casa}"
        case 1: sequencia += f" \x1b[34m{casa}"
        case 2: sequencia += f" \x1b[31m{casa}"
    print(sequencia)
  print("\n\x1b[m")

main()
