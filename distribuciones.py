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
Probabilidad: %s
Esperanza: %s
Varianza: %s
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
    dict_params = ["x", "n", "p"]

    def __init__(self):
        super().__init__()
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.x = lista[0]
        self.n = lista[1]
        self.p = lista[2]
        self._probabilidad = combinatoria(self.n, self.x) * (self.p ** self.x) * (1 - self.p) ** (self.n - self.x)
        self._esperanza = self.n * self.p
        self._varianza = self.n * self.p * (1 - self.p)
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

    dict_params = ["x", "r", "p"]

    def __init__(self):
        super().__init__()

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.x = lista[0]
        self.r = lista[0]
        self.p = lista[0]

        self._probabilidad = combinatoria(self.x - 1, self.r - 1) * (self.p ** self.r) * (1 - self.p) ** (
                self.x - self.r)
        self._esperanza = self.r / self.p
        self._varianza = (self.r * (1 - self.p)) / (self.p ** 2)

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
    dict_params = ["x", "p"]

    def __init__(self):
        super().__init__()
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.x = lista[0]
        self.p = lista[1]

        self._probabilidad = self.p * (1 - self.p) ** (self.x - 1)
        self._esperanza = 1 / self.p
        self._varianza = (1 - self.p) / (self.p ** 2)
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
    dict_params = ["x", "k", "N", "n"]

    def __init__(self):
        super().__init__()
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.x = lista[0]
        self.k = lista[1]
        self.N = lista[2]
        self.n = lista[3]

        self._probabilidad = combinatoria(
            self.k, self.x) * combinatoria(self.N - self.k, self.n - self.x) / combinatoria(self.N, self.n)
        self._esperanza = self.n * self.k / self.N
        self._varianza = (self.n * self.k / self.N) * (1 - self.k / self.N) * (self.N - self.n / self.N - 1)
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

    dict_params = ["x", "lamb"]

    def __init__(self):
        super().__init__()
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.x = lista[0]
        self.lamb = lista[1]
        self._probabilidad = ((self.lamb ** self.x) * (e ** (-self.lamb))) / factorial(self.x)
        self._esperanza = self.lamb
        self._varianza = self.lamb
        return

    pass


distribuciones = {"Binomial": DistBinomial,
                  "Binomial Negativa": DistBinomialNegativa,
                  "Geometrica": DistGeometrica,
                  "Hipergeometrica": DistHipergeometrica,
                  "Poisson": DistPoisson,
                  }
