""" 

1) João está trabalhando em uma mina, tentando retirar o máximo que consegue de
diamantes "<>". Ele deve excluir todas as partículas de areia "." do processo e a cada
retirada de diamante, novos diamantes poderão se formar. Se ele tem como uma entrada
.<...<<..>>....>....>>>., três diamantes são formados. O primeiro é retirado de <..>,
resultando .<...<>....>....>>>. Em seguida o segundo diamante é retirado, restando
.<.......>....>>>. O terceiro diamante é então retirado, restando no final .....>>>., sem
possibilidade de extração de novo diamante.

"""

def encontra_letra(letra, frase):
  return sum(caractere == letra for caractere in frase)

def minerar (str):
  str = str.replace(".", "")
  esquerdo = encontra_letra("<", str)
  direito  = encontra_letra(">", str)
  return esquerdo if esquerdo < direito else direito

def main ():
  res = []

  N = input("Numero de casos: ")
  while not N.isdigit(): N = input("Numero de casos: ")

  for contador in range(0, int(N)):
    teste = input(f"Teste {contador}: ")
    while len(teste) > 1000: teste = input(f"Teste {contador}: ")
    res.append(minerar(teste))
  
  for r in res: print(r)

main()