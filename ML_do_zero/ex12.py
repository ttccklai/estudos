def le_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcula_litros_usados(tempo, velocidade):
    distancia = velocidade * tempo
    litros = distancia / 12
    return litros

def exibe_valores(velocidade, tempo, litros):
    print(f"Velocidade média: {velocidade} km/h")
    print(f"Tempo gasto: {tempo} horas")
    print(f"Litros de combustível usados: {litros:.2f} litros")