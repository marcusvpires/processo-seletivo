""" 

4) Crie uma função que receba uma letra e uma string e retorne a quantidade de vezes que aquela letra está presente na string passada. 

"""

def encontra_letra(letra, frase):
  return sum(caractere == letra for caractere in frase)

res = encontra_letra('a ', 'uma frase generica de questões de programação')
print(res)