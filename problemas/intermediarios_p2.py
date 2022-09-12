""" 

2) Escreva uma função que receba uma lista de números e que retorne a lista sem números repetidos.

"""

def removeDuplicatas (lista):
  return list(set(lista))

res = removeDuplicatas([1, 2, 5, 9, 2])
print(res)

def removeDuplicatasOrdenado (lista):
  lt = []
  [ lt.append(i) if i not in lt else 0 for i in lista ]
  return lt

res2 = removeDuplicatasOrdenado([1, 2, 5, 9, 2])
print(res2)

