import math
# Datos del conjunto original
total = 10
aceptaron = 5
no_aceptaron = 5
# Entropía del conjunto original
p_si = aceptaron / total
p_no = no_aceptaron / total
H_S = 0
# División por el atributo 'Tiene linea fija'
# Tiene linea fija = Sí: IDs 1,3,6,8,10 → 5 personas → 5 aceptaron
# Tiene linea fija = No: IDs 2,4,5,7,9 → 5 personas → 5 no aceptaron
# Subconjunto: Tiene linea fija = Sí
total_si = 5
aceptaron_linea_si = 5
no_aceptaron_linea_si = 0
p_si_si = aceptaron_linea_si / total_si
p_no_si = 0
H_si =0
# Subconjunto: Tiene linea fija = No
total_no = 5
aceptaron_linea_no = 0
no_aceptaron_no = 5
p_si_no = aceptaron_linea_no / total_no
p_no_no = no_aceptaron_no / total_no
H_no = - (p_si_no * math.log2(p_si_no) + p_no_no * math.log2(p_no_no))
# Entropía ponderada
H_div = (total_si / total) * H_si + (total_no / total) * H_no
# Ganancia de información
gain = H_S - H_div

print("Entropía original:", H_S)
print("Entropía línea fija = Sí:", H_si)
print("Entropía línea fija = No:", H_no)
print("Entropía después de la división:", H_div)
print("Ganancia de información:", gain)