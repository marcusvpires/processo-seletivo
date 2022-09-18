""" 

1) Leia um vetor de 10 posições e em seguida ler também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

"""

def perguntaLista():
  lista = []
  print("Digite uma lista de 10 numeros")
  
  for i in range(0, 10):
    numero = input(f"{i + 1}: ")
    
    # pergunta o valor até que seja possível converter para inteiro
    while not numero.isdigit():
      print("Digite um numero válido")
      numero = input(f"{i + 1}: ")
    lista.append(int(numero))
  
  return lista


def perguntaPosicao (menssagem):
  while True:
    try:
      valor = int(input(menssagem))
      if valor >= 0 and valor <= 9: return valor
      raise ValueError('Posição inexistente')
    except ValueError: print("Digite um número entre 0 e 9")

def main():
  # lista = [13, 5, 7, 6, 4, 8, 16, 31, 9, 21]
  lista = perguntaLista()
  x = perguntaPosicao("Digite x: ")
  y = perguntaPosicao("Digite y: ")

  soma = lista[x] + lista[y]
  print("Soma: ", soma)
  return soma

main()