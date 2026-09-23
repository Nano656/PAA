import math
# Datos del conjunto
# Aceptó oferta: Sí = 5, No = 5
total = 10
compraron = 5
no_compraron = 5
# Probabilidades
p_si = compraron / total
p_no = no_compraron / total
# Cálculo de entropía
entropy = - (p_si * math.log2(p_si) + p_no * math.log2(p_no))
print(f"Entropía del conjunto original: {entropy:.3f}")

