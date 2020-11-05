"""
Libreria de distribuciones notables para Estadistica
"""
from math import factorial, e


def combinatoria(n, x):
    """
    Entrega el valor de la combinatoria entre dos numeros dados
    """
    return factorial(n) / (factorial(x) * factorial(n - x))


class Distribucion:
    """
    Clase abstracta de distibucciones
    """

    def __init__(self):
        self._varianza = 0
        self._esperanza = 0
        self._probabilidad = 0
        return

    def probabilidad(self):
        return self._probabilidad

    def esperanza(self):
        return self._esperanza

    def varianza(self):
        return self._varianza

    def __str__(self):
        return '''
probabilidad: %s
esperanza: %s
varianza: %s
''' % (str(self._probabilidad), str(self._esperanza), str(self._varianza))
    
    pass


class DistBinomial(Distribucion):
    """
    La distribución binomial presenta solo 2 posibles resultados
    Las repeticiones son independientes la una de la otra
    Sus repeticiones son fijas
    La probabilidad es constante

    P(X = x)
    x = 1, 2, 3, ... , n

        :x cantidad de éxitos
        :n cantidad de repeticiones
        :p probabilidad de éxito
    """

    def __init__(self, x, n, p):
        super().__init__()
        self._probabilidad = combinatoria(n, x) * (p ** x) * (1 - p) ** (n - x)
        self._esperanza = n * p
        self._varianza = n * p * (1 - p)

        return

    pass


class DistBinomialNegativa(Distribucion):
    """
    La distribución binomial negativa presenta solo 2 posibles resultados
    Las repeticiones son independientes la una de la otra
    la cantidad de éxitos es fija
    La probabilidad es constante

    P(X = x)
    x = r, r + 1, r + 2, r + 3 ...

        :x cantidad de repeticiones hasta obtener "r" exitos
        :r cantidad de éxitos
        :p probabilidad de éxito
    """

    def __init__(self, x, r, p):
        super().__init__()
        self._probabilidad = combinatoria(x - 1, r - 1) * (p ** r) * (1 - p) ** (x - r)
        self._esperanza = r / p
        self._varianza = (r * (1 - p)) / (p ** 2)

        return

    pass


class DistGeometrica(Distribucion):
    """
    La distribución geométrica presenta solo 2 posibles resultados
    Las repeticiones son independientes la una de la otra
    P(X = x)
    x = 1, 2, 3 ...

        :x cantidad de repeticiones hasta obtener 1 exito
        :p probabilidad de éxito
    """

    def __init__(self, x, p):
        super().__init__()
        self._probabilidad = p * (1 - p) ** (x - 1)
        self._esperanza = 1 / p
        self._varianza = (1 - p) / (p ** 2)
        return

    pass


class DistHipergeometrica(Distribucion):
    """
    La distribución hipergeométrica presenta solo 2 posibles resultados
    Las repeticiones NO son independientes la una de la otra
    La cantidad de repeticiones es fija
    Se ocupa para obtener la probabilidad de éxitos en una sub muestra

    P(X = x)
    x = 1, 2, 3 ...
    min {n , k}

        :x cantidad de éxitos dentro de la muestra de tamaño n
        :k cantidad de éxitos en el conjunto grande
        :N tamaño del conjunto grande
        :n tamaño de la muestra
    """

    def __init__(self, x, k, N, n):
        super().__init__()
        self._probabilidad = combinatoria(
            k, x) * combinatoria(N - k, n - x) / combinatoria(N, n)
        self._esperanza = n * k / N
        self._varianza = (n * k / N) * (1 - k / N) * (N - n / N - 1)
        return

    pass


class DistPoisson(Distribucion):
    """
    Distribución de Poisson
    La probabilidad de que ocurra determinada cantidad de 
    sucesos independientes en un periodo de tiempo definido
    sea X: la cantidad de éxitos
    sea lamb: el periodo de tiempo definido
    """

    def __init__(self, x, lamb):
        super().__init__()
        self._probabilidad = ( ( lamb ** x )*( e**(-lamb) ) ) / factorial(x)
        self._esperanza = lamb
        self._varianza = lamb
        return

    pass


distribuciones = {"Binomial": DistBinomial,
                  "Binomial Negativa": DistBinomialNegativa,
                  "Geometrica": DistGeometrica,
                  "Hipergeometrica": DistHipergeometrica,
                  "Poisson": DistPoisson,
                  }
