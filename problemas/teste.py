import math

# Valores da carga
Q1 =  1E-9
Q2 = -1E-9

# Posição da carga 1
P1x = 1.05
P1y = 1.05

# Posição da carga 2
P2x = -1.05
P2y = -1.05

x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = x1
y2 = y1

Vp = 9E9*Q1*math.sqrt((x1-P1x)**2 + (y1-P1y)**2)

# Potencial devido a uma carga positiva
Vn = 9E9*Q2*math.sqrt((x2-P2x)**2 + (y2-P2y)**2)

# Princípio da sobreposição
V = Vp + Vn

print(V)
