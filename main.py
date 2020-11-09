"""
Archivo de pruebas de implementación por consola
"""

from distribuciones import distribuciones, calcular_acumulada

p = distribuciones["Binomial"]()
print(calcular_acumulada(p, 0, 6, [8, .5]))