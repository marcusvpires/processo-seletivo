""" 

3) Crie uma função que recebe uma lista de números e retorne uma lista apenas com os números primos.

"""

# difinição de numero primo: aquele que é dividido apenas por um e por ele mesmo 

def is_primo (item):
  if item > 1:
    for i in range(2, item):
      # Verifica de o resto da divisão é 0, ou seja, se é divisível
      if item % i == 0: return False
    else: return True

def encontra_primo (lista):
  primos = []
  for item in lista:
    if (is_primo(item)): primos.append(item)
  return primos

res = encontra_primo([1,2,3,4,5]);
print(res)