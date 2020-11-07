"""
Archivo de pruebas de implementación por consola
"""

from distribuciones import distribuciones

def acumulada(dist_discreta, inicio, fin, valores):
    valores.insert(0, 0)
    suma = 0
    for i in range(inicio, fin + 1):
        valores[0] = i
        dist_discreta.iniciar(valores)
        suma += dist_discreta.probabilidad()
    return 1 - suma


print(acumulada(p, 0, 6, [8, .5]))