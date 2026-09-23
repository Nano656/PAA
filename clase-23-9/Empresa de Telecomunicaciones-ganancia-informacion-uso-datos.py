import math
# Datos del conjunto original
total = 10
aceptaron_total = 5
no_aceptaron_total = 5
# Entropía del conjunto original
p_si = aceptaron_total / total
p_no = no_aceptaron_total / total
H_S = - (p_si * math.log2(p_si) + p_no * math.log2(p_no))
# Agrupamos uso de datos en rangos: Bajo (≤3GB), Medio (3.1–6GB), Alto (>6GB)
# Datos por grupo:
# bajo: ID 1, 3, 8 → uso de datos 2.5, 3.0, 2.0 GB → 3 personas → 0 aceptaron, 3 no
# medio: ID 2, 6, 7, 10 → uso de datos 6.0, 4.0, 5.5, 3.5 GB → 4 personas → 2 aceptaron, 2 no
# alto: ID 4, 5, 9 → uso de datos 8.0, 7.5, 6.5 GB → 3 personas → 3 aceptaron, 0 no
def entropy(p1, p2):
    total = p1 + p2
    if total == 0 or p1 == 0 or p2 == 0:
        return 0.0
    p1 /= total
    p2 /= total
    return - (p1 * math.log2(p1) + p2 * math.log2(p2))
# bajo: 3 sí, 0 no
H_bajo= entropy(3, 0)
# medio: 2 sí, 2 no
H_medio = entropy(2, 2)
# alto: 3 sí, 0 no
H_alto = entropy(3, 0)
# Entropía ponderada
H_division = (3/10)*H_bajo + (4/10)*H_medio + (3/10)*H_alto
# Ganancia de información
ganancia_datos = H_S - H_division
ganancia_datos
print("H_S: ", H_S)
print("H_division/entropia ponderada: ", H_division)
print("ganancia_edad: ", ganancia_datos)