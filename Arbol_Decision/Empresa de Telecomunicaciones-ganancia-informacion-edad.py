import math
# Datos del conjunto original
total = 10
aceptaron_total = 5
no_aceptaron_total = 5
# Entropía del conjunto original
p_si = aceptaron_total / total
p_no = no_aceptaron_total / total
H_S = - (p_si * math.log2(p_si) + p_no * math.log2(p_no))
# Agrupamos edades en rangos: Joven (≤30), Adulto (31–50), Mayor (>50)
# Datos por grupo:
# Joven: ID 1,3,8 → edades 24,29,36 → 3 personas → 0 aceptaron, 3 no
# Adulto: ID 2,4,6,7,9,10→ edades 38,45,33,41,36,31 → 6 personas → 4 aceptaron, 2 no
# Mayor: ID 5, → edad 52 → 1 persona → 1 aceptó, 0 no
# Entropía de cada grupo
def entropy(p1, p2):
    total = p1 + p2
    if total == 0 or p1 == 0 or p2 == 0:
        return 0.0
    p1 /= total
    p2 /= total
    return - (p1 * math.log2(p1) + p2 * math.log2(p2))
# Joven: 0 sí, 3 no
H_joven = entropy(0, 3)
# Adulto: 4 sí, 2 no
H_adulto = entropy(4, 2)
# Mayor: 1 sí, 0 no
H_mayor = entropy(1, 0)
# Entropía ponderada
H_division = (3/10)*H_joven + (6/10)*H_adulto + (1/10)*H_mayor
# Ganancia de información
ganancia_edad = H_S - H_division
ganancia_edad
print("H_S: ", H_S)
print("H_division/entropia ponderada: ", H_division)
print("ganancia_edad: ", ganancia_edad)