""" 

1) Crie uma função que receba as coordenadas (x,y) de 3 pontos, (A, B, C), e retorne o angulo entre elas ∠ABC.

"""

import math

"""
  math.atan2(y, x) retornando arctan [y/x]
  ou seja:
  se tg [angulo (rad)] = inclicação então arctg inclinação = [angulo (rad)]

  Vetor BA(y, x) = A[1]-B[1], A[0]-B[0]
  angulo do vetor BA em relação ao x = arctg(BA[y], BA[x])

  inclinação de BA - BC = angulo entre os vetores (red)
"""

def getAngle(A, B, C):
  ang = math.degrees(math.atan2(C[1]-B[1], C[0]-B[0]) - math.atan2(A[1]-B[1], A[0]-B[0]))
  # se o angulo for negativo, troca o sentido (horário, antihorário)
  return ang + 360 if ang < 0 else ang

res = getAngle((5, 0), (0, 0), (0, 5))
print(f"{res:.1f}°")