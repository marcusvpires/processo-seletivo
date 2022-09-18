""" 

2) Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual à soma dos seus divisores excetuando-o. (ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano. (Caso esteja escrevendo seu programa em C, considere o inteiro 0 para o booleano false e 1 para o true) 

"""

def num_perfeito (valor):
  contador = 1
  soma = 0 # equivalente ao numero perfeito
  while valor > soma:
    soma += contador
    contador += 1
  return soma == valor

numero = int(input("Valor: "))
res = num_perfeito(numero)
print(res)