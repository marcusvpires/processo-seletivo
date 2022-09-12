""" 

2) Crie uma função que receba uma temperatura em graus fahrenheit e retorne a temperatura em graus Celsius.

"""

def converte_temperatura(fahrenheit): 
  return (fahrenheit - 32) * 5.0/9.0

res = converte_temperatura(77.2)
print(res);
