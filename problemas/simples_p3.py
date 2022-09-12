""" 

3) Crie uma função que recebe uma lista de números e retorne uma lista apenas com os números primos.

"""

def is_primo (num):
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
          return False
    else:
      return True

def encontra_primo (lista):
  primos = []
  for num in lista:
    if (is_primo(num)): primos.append(num)
  return primos

res = encontra_primo([1,2,3,4,5]);
print(res)