""" 

1) Crie uma função que receba as coordenadas (x,y) de 3 pontos, (A, B, C), e retorne o angulo entre elas ∠ABC.

"""

import math
 
def getAngle(a, b, c):
  ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
  return ang + 360 if ang < 0 else ang

res = getAngle((5, 0), (0, 0), (0, 5))
print(str(res) + "°")