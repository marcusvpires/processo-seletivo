"""

2) Você deverá escrever um programa que leia um tabuleiro de xadrez e identifique se o
Rei está em xeque. Um rei está sob xeque caso esteja ocupando uma posição no tabuleiro
que pode ser ocupada pelo oponente no próximo movimento dele. Considerando que a
entrada do programa consistirá em caracteres, para diferenciar as peças pretas das brancas
será feito o seguinte. As peças brancas serão representadas por letras maiúsculas,
enquanto as pretas por minúsculas. O lado do tabuleiro ocupado inicialmente pelas peças
brancas será sempre a parte inferior, enquanto a superior será a ocupada inicialmente
pelas pretas.

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

"""


from platform import mac_ver


def main():
    jogo = [
        "........",
        ".2..3..4",
        "..a.a.a.",
        "........",
        ".1B.k.a5",
        "........",
        "..B.a.a.",
        ".9..7..6",
    ]
    # for i in range(0, 8): jogo.append(input(f"{i + 1}: "))
    checkXeque(jogo)


def checkXeque(jogo):
    for l, linha in enumerate(jogo):
        for c, casa in enumerate(linha):
            if casa == 'k':
                check = checkBranco(l, c, jogo)
                print(check)


def checkBranco(l, c, jogo):
    tabela = [[], [], [], [], [], [], [], []]

    def check(y, x, ataque):
        if 0 > x or x > 7 or 0 > y or y > 7: return [1, [x, y], ""]
        cs = jogo[y][x]
        if ataque.find(cs) != -1: return [2, [x, y], cs]
        elif cs == '.': return [0, [x, y], cs]
        else: return [1, [x, y], cs]

    def expansao (linha, coluna, ataque, id):
        for i in range(1, 8):
            [status, [x, y], casa] = check(linha(i), coluna(i), ataque)
            print(f"{id} {status} ({x:0>2}, {y:0>2}) {casa}")
            # tabela[y][x] = [sta]
            if status: return [status, [x, y], casa]

    """ 
            
    NO  N   NL    
      - | -
    O---|---L
      - | -
    SO  S   SL
    
    """

    ex = {}
    
    ex["o" ] = expansao (lambda i: l,     lambda i: c - i, "RQ", "<<")
    ex["no"] = expansao (lambda i: l - i, lambda i: c - i, "BQ", "^<")
    ex["n" ] = expansao (lambda i: l - i, lambda i: c,     "RQ", "^^")
    ex["nl"] = expansao (lambda i: l - i, lambda i: c + i, "BQ", ">^")
    ex["l" ] = expansao (lambda i: l,     lambda i: c + i, "RQ", ">>")
    ex["sl"] = expansao (lambda i: l + i, lambda i: c + i, "BQ", ",>")
    ex["s" ] = expansao (lambda i: l + i, lambda i: c,     "RQ", ",,")
    ex["so"] = expansao (lambda i: l + i, lambda i: c - i, "BQ", "<,")

main()
