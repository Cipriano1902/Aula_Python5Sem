transporte = input("Escolha um transporte (carro, bicicleta, a pé): ").strip().lower()

if transporte == "carro":
    print("Velocidade média aproximada: 60 km/h.")
elif transporte == "bicicleta":
    print("Velocidade média aproximada: 20 km/h.")
elif transporte in ("a pé", "a pe"):
    print("Velocidade média aproximada: 5 km/h.")
else:
    print("Modo de transporte inválido.")
