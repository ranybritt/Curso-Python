''' Exercício Python 14:
Escreva um programa que converta uma temperatura digitando em graus
Celsius e converta para graus Fahrenheit.
    Resolução:
'''
print('-'*25)
print('Conversor de Temperatura')
print('-'*25)
celsius = int(input('Informe a temperatura em °C: '))
fahr = (celsius * 1.8) + 32
kelvin = celsius + 273.15
print(f'A temperatura {celsius}°C equivale a: ')
print(f'Fahrenheit: {fahr}°F\nKelvin: {kelvin} K')
