def ler_temperatura():
    temperatura = float(input("Digite a temperatura em Celsius: "))
    return temperatura

def converter_temperatura(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrar_teperatura(fahrenheit):
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")