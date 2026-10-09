def clasificador(usuarios):
    for usuario in usuarios:

        if "victoria" in usuario or "derrota" in usuario:
            print("Categoría: Combate")
        elif "descubrimiento" in usuario or "sin_hallazgos" in usuario:
            print("Categoría: Exploración")
        elif "mensaje_enviado" in usuario:
            print("Categoría: Interacción Social")

usuarios = [
    ["user01", 120, "victoria"],
    ["user02", 300, "descubrimiento"],
    ["user03", 180, "mensaje_enviado"],
    ["user04", 90, "derrota"],
    ["user05", 240, "sin_hallazgos"]
]

clasificador(usuarios)