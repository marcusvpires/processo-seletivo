""" 

1) João está trabalhando em uma mina, tentando retirar o máximo que consegue de
diamantes "<>". Ele deve excluir todas as partículas de areia "." do processo e a cada
retirada de diamante, novos diamantes poderão se formar. Se ele tem como uma entrada
.<...<<..>>....>....>>>., três diamantes são formados. O primeiro é retirado de <..>,
resultando .<...<>....>....>>>. Em seguida o segundo diamante é retirado, restando
.<.......>....>>>. O terceiro diamante é então retirado, restando no final .....>>>., sem
possibilidade de extração de novo diamante.

"""

def mine (str):
  str = str.replace(".", "")
  dim = 0
  while len(str) > 1 and str.find("<>") != -1:
    str = str.replace("<>", "", 1)
    dim += 1
  return dim

def main ():
  res = []

  N = input("Numero de casos: ")
  while not N.isdigit(): N = input("Numero de casos: ")

  for c in range(0, int(N)):
    teste = input(f"Teste {c}: ")
    while len(teste) > 1000: teste = input(f"Teste {c}: ")
    res.append(mine(teste))
  
  for r in res: print(r)

main()