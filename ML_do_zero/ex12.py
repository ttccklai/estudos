def le_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcula_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia
    
def calcula_litros(distancia):
    litros = distancia / 12
    return litros

def exibe_valores(velocidade, tempo, distancia, litros):
    print(f"Velocidade média: {velocidade} km/h")
    print(f"Tempo gasto: {tempo} horas")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Litros de combustível usados: {litros:.2f} litros")