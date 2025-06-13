def calcula_energia_potencial_gravitacional(m, h, g = 10):
    """
    Calcula a energia potencial gravitacional de um corpo.

    Parâmetros:
    m (float): Massa do corpo em quilogramas.
    h (float): Altura do corpo em metros.
    g (float, opcional): Aceleração da gravidade em m/s². Padrão é 10 m/s².

    Retorna:
    float: Energia potencial gravitacional em joules.
    """
    
    e = m * g * h
    
    return e

e = calcula_energia_potencial_gravitacional(10, 5)
print(e)