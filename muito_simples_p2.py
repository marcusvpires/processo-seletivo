""" 

2) Crie uma função que receba uma temperatura em graus fahrenheit e retorne a temperatura em graus Celsius.

"""

def fahrenheitParaCelsius(fahrenheit): 
  return (fahrenheit - 32) * 5.0/9.0

res = fahrenheitParaCelsius(77.2)
print(f"{res:.2f}°C")
