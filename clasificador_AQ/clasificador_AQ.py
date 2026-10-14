positivos = [ 
{"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Corta" }, 
{"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "Si", "distancia_trabajo": "Media"}, 
{"edad": "Mayor", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Larga"}
]

negativos = [ 
{"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "No", "distancia_trabajo": "Corta" }, 
{"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "No", "distancia_trabajo": "Media"}, 
{"edad": "Mayor", "ingreso": "Bajo", "tiene_garaje": "No", "distancia_trabajo": "Larga"}
]


regla = {}

atributos = []

ejemplo = positivos[0]

for clave in ejemplo:
    print("Clave: ", clave)
    atributos.append(clave)

for atributo in atributos:
    valores_pos = []
    valores_neg = []

    for ej in positivos:
        valor = ej[atributo]
        
        if valor not in valores_pos:
            valores_pos.append(valor)

    for ej in negativos:
        valor = ej[atributo]
        if valor not in valores_neg:
            valores_neg.append(valor)


    valores_validos = []
    for valor in valores_pos:
        encontrado = False
        for v in valores_neg:
            if valor == v:
                encontrado = True
                break
        if not encontrado:
            valores_validos.append(valor)


    if len(valores_validos) > 0:
        regla[atributo] = valores_validos


print("Prediccion:")
for atributo in regla:
    print("-", atributo, "debe ser: ", regla[atributo])

compra_auto_electrico = True

if positivos == negativos:
    compra_auto_electrico = True
    print("El cliente comprará el vehiculo")
elif atributos == regla[atributo]:
    compra_auto_electrico = True
    print("El cliente comprará el vehiculo")
else:
    compra_auto_electrico = False
    print("El cliente NO comprará el vehiculo")