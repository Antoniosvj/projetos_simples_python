

# def celsius_para_fahrenheit(celsius):
#     fahrenheit = (9/5) * celsius + 32
#     return fahrenheit

# celsius = int(input('Digite a temperatura: '))
# fahrenheit = celsius_para_fahrenheit(celsius)
# print(f'{celsius}º Celsius é equivalente a {fahrenheit}º Fahrenheit ')

def fahrenheit_para_celsius(fahrenheit):
    fahrenheit = int(input('Digite a temperatura: '))
    celsius = (5/9) * (fahrenheit - 32)
    print(f'{fahrenheit}º Fahrenheit é equivalente a {celsius}º Celsius')

