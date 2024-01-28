valores = input().split()
CONSUMO_CARRO = 12

tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

consumo = tempo_gasto*velocidade_media/CONSUMO_CARRO

print(f"{consumo:.3f}")
