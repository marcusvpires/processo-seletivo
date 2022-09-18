"""

2) Você deverá escrever um programa que leia um tabuleiro de xadrez e identifique se o Rei está em xeque. Um rei está sob xeque caso esteja ocupando uma posição no tabuleiro
que pode ser ocupada pelo oponente no próximo movimento dele. Considerando que a entrada do programa consistirá em caracteres, para diferenciar as peças pretas das brancas
será feito o seguinte. As peças brancas serão representadas por letras maiúsculas, enquanto as pretas por minúsculas. O lado do tabuleiro ocupado inicialmente pelas peças
brancas será sempre a parte inferior, enquanto a superior será a ocupada inicialmente pelas pretas.

Peão:     Torre:    Bispo:    Rainha:   Rei:      Cavalo:
........  ...*....  .......*  ...*...*  ........  ........
........  ...*....  *.....*.  *..*..*.  ........  ........
........  ...*....  .*...*..  .*.*.*..  ........  ..*.*...
........  ...*....  ..*.*...  ..***...  ..***...  .*...*..
...p....  ***r****  ...b....  ***q****  ..*k*...  ...n....
..*.*...  ...*....  ..*.*...  ..***...  ..***...  .*...*..
........  ...*....  .*...*..  .*.*.*..  ........  ..*.*...
........  ...*....  *.....*.  *..*..*.  ........  ........

Mapeamento:
    c0   c1   c2   c3   c4   c5   c6   c7
l0 0[0] 0[1] 0[2] 0[3] 0[4] 0[5] 0[6] 0[7]
l1 1[0] 1[1] 1[2] 1[3] 1[4] 1[5] 1[6] 1[7]
l2 2[0] 2[1] 2[2] 2[3] 2[4] 2[5] 2[6] 2[7]
l3 3[0] 3[1] 3[2] 3[3] 3[4] 3[5] 3[6] 3[7]
l4 4[0] 4[1] 4[2] 4[3] 4[4] 4[5] 4[6] 4[7]
l5 5[0] 5[1] 5[2] 5[3] 5[4] 5[5] 5[6] 5[7]
l6 6[0] 6[1] 6[2] 6[3] 6[4] 6[5] 6[6] 6[7]
l7 7[0] 7[1] 7[2] 7[3] 7[4] 7[5] 7[6] 7[7]

      0       1       2      3 0     4 1     5 2     6 3     7 4
------------------------------------------------------------------
0   |  BQ | |  .  | |  .  | |  RQ | |  .  | |  .  | |  BQ | |  .  |
------------------------------------------------------------------
1   |  .  | |  BQ | |  .  | |  RQ | |  .  | |  BQ | |  .  | |  .  |
------------------------------------------------------------------
2   |  .  | |  .  | |  BQ | |  RQ | |  BQ | |  .  | |  .  | |  .  |
------------------------------------------------------------------
3 0 |  RQ | |  RQ | |  RQ | |  k  | |  RQ | |  RQ | |  RQ | |  RQ |
------------------------------------------------------------------
4 1 |  .  | |  .  | | PBQ | |  RQ | | PBQ | |  .  | |  .  | |  .  |
------------------------------------------------------------------
5 2 |  .  | |  BQ | |  .  | |  RQ | |  .  | |  BQ | |  .  | |  .  |
------------------------------------------------------------------
6 3 |  BQ | |  .  | |  .  | |  RQ | |  .  | |  .  | |  BQ | |  .  |
------------------------------------------------------------------
7 4 |  .  | |  .  | |  .  | |  RQ | |  .  | |  .  | |  .  | |  B  |


..k.....
ppp.pppp
........
.R...B..
........
........
PPPPPPPP
K.......
rnbqk.nr
ppp..ppp
....p...
...p....
.bPP....
.....N..
PP..PPPP
RNBQKB.R
........
........
........
........
........
........
........
........

"""

def checkXeque(l, c, tabuleiro, preto = False):
  def check(y, x, ataque):
    # categoria null: casa vazia
    # categoria 1: bloqueio ou fora do trabuleiro
    # categoria 2: xeque
    if 0 > x or x > 7 or 0 > y or y > 7: return 1
    cs = tabuleiro[y][x]
    if ataque.find(cs) != -1: return 2
    if cs != '.': return 1

  def expansao(linha, coluna, ataque, id):
    # linha e coluna são f(i) que expande da coordenada da peça para uma determinada direção
    # as direções estão representadas pela rosa dos ventos no arquivo "./dificeis_p2_extra.py"
    # ataque são as peças que podem atacar na respectiva direção (ex: bispo em [l - i, c + i])
    if preto: ataque = ataque.lower()
    for i in range(1, 8):
      res = check(linha(i), coluna(i), ataque)
      match res:
        case 1: return False # bloqueio ou fora do trabuleiro
        case 2: return True #xeque

  def especifico(cods, ataque, id):
    # cods são coordenadas das peças com movimentos específicos
    if preto: ataque = ataque.lower()
    for [linha, coluna] in cods:
      res = check(linha, coluna, ataque)
      match res:
        # não existe bloquio para o cavalo ou o peão
        # case 1: return False
        case 2: return True # Xeque
  
  if expansao(lambda i: l - i, lambda i: c,     "RQ", "n" ) : return True # norte
  if expansao(lambda i: l + i, lambda i: c,     "RQ", "s" ) : return True # sul
  if expansao(lambda i: l,     lambda i: c + i, "RQ", "l" ) : return True # leste
  if expansao(lambda i: l,     lambda i: c - i, "RQ", "o" ) : return True # oeste
  if expansao(lambda i: l - i, lambda i: c - i, "BQ", "no") : return True # noroeste
  if expansao(lambda i: l - i, lambda i: c + i, "BQ", "nl") : return True # nordeste
  if expansao(lambda i: l + i, lambda i: c - i, "BQ", "so") : return True # sudoeste
  if expansao(lambda i: l + i, lambda i: c + i, "BQ", "sl") : return True # sudeste

  if especifico([[l+1, c+1], [l+1, c-1]], "P", "p") : return True # Peão
  if especifico([[l-2, c+1], [l-2, c-1], [l+2, c+1], [l+2, c-1], [l+1, c-2], [l+1, c+2], [l-1, c+2],  [l-1, c-2]], "N", "n") : return True # cavalo

def main ():
  resultados = []
  while True:
    tabuleiro = []
    estaVazio = True
    nenhumRei = True

    for i in range(0, 8): tabuleiro.append(input(f"{i + 1}: "))
    for l, linha in enumerate(tabuleiro):
      for c, casa in enumerate(linha):
        if casa != '.':
          # passa por cada casa do tabuleiro
          # l = linha (y) e c = coluna (x)
          estaVazio = False
          if casa == 'k' and checkXeque(l, c, tabuleiro):
            nenhumRei = False
            resultados.append("Rei preto está em cheque")
          elif casa == 'K' and checkXeque(l, c, tabuleiro, True):
            nenhumRei = False
            resultados.append("Rei branco está em cheque")

    if not estaVazio and nenhumRei: resultados.append("Nenhum rei esta em cheque.")
    print('')

    if estaVazio:
      for index, resultado in enumerate(resultados):
        print(f"Jogo {index}: {resultado}")
      break
  
main()