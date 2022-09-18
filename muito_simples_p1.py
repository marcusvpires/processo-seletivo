"""

1) Crie uma função que recebe dois pontos do plano cartesiano e retorna a distância entre eles.

"""

def distancia(p1, p2):
  # Equação de pitágoras
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

res = distancia([1,2],[5,6])
print(f"{res:.2f}")