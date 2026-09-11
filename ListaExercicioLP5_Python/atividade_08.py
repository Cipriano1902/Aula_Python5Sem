estado_civil = input(
    "Digite o estado civil (solteiro, casado, divorciado, viúvo): "
).strip().lower()

if estado_civil == "solteiro":
    print("Estado civil: solteiro.")
elif estado_civil == "casado":
    print("Estado civil: casado.")
elif estado_civil == "divorciado":
    print("Estado civil: divorciado.")
elif estado_civil in ("viúvo", "viuvo"):
    print("Estado civil: viúvo.")
else:
    print("Estado civil inválido.")
