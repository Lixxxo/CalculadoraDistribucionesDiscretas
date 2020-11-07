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
        """
        Getter de la probabilidad de la distribución
        """
        return self._probabilidad

    def esperanza(self):
        """
        Getter de la esperanza de la distribución
        """
        return self._esperanza

    def varianza(self):
        """
        Getter de la varianza de la distribución
        """
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
    dict_params = {"x": "cantidad de éxitos", "n":"cantidad de repeticiones", "p":"probabilidad de éxito"}


    def __init__(self):
        super().__init__()
        self.__x = None
        self.__n = None
        self.__p = None
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.__x = lista[0]
        self.__n = lista[1]
        self.__p = lista[2]
        self._probabilidad = combinatoria(self.__n, self.__x) * (self.__p ** self.__x) * (1 - self.__p) ** (
                self.__n - self.__x)
        self._esperanza = self.__n * self.__p
        self._varianza = self.__n * self.__p * (1 - self.__p)
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
        this.x, :r cantidad de éxitos
        :p probabilidad de éxito
    """

    dict_params = {"x":'cantidad de repeticiones hasta obtener "r" exitos', "r":"cantidad de éxitos", "p":"probabilidad de éxito"}

    def __init__(self):
        super().__init__()
        self.__x = None
        self.__r = None
        self.__p = None

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.__x = lista[0]
        self.__r = lista[1]
        self.__p = lista[2]

        self._probabilidad = combinatoria(self.__x - 1, self.__r - 1) * (self.__p ** self.__r) * (1 - self.__p) ** (
                self.__x - self.__r)
        self._esperanza = self.__r / self.__p
        self._varianza = (self.__r * (1 - self.__p)) / (self.__p ** 2)

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
    dict_params = {"x":"cantidad de repeticiones hasta obtener 1 exito", "p":"probabilidad de éxito"}

    def __init__(self):
        super().__init__()
        self.__x = None
        self.__p = None
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.__x = lista[0]
        self.__p = lista[1]

        self._probabilidad = self.__p * (1 - self.__p) ** (self.__x - 1)
        self._esperanza = 1 / self.__p
        self._varianza = (1 - self.__p) / (self.__p ** 2)
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
    dict_params = {"x":"cantidad de éxitos dentro de la muestra de tamaño n", "k":"cantidad de éxitos en el conjunto grande", "N":"tamaño del conjunto grande", "n":"tamaño de la muestra"}

    def __init__(self):
        super().__init__()
        self.__x = None
        self.__k = None
        self.__N = None
        self.__n = None
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.__x = lista[0]
        self.__k = lista[1]
        self.__N = lista[2]
        self.__n = lista[3]

        self._probabilidad = combinatoria(
            self.__k, self.__x) * combinatoria(self.__N - self.__k, self.__n - self.__x) / combinatoria(self.__N,
                                                                                                        self.__n)
        self._esperanza = self.__n * self.__k / self.__N
        self._varianza = (self.__n * self.__k / self.__N) * (1 - self.__k / self.__N) * (
                (self.__N - self.__n) / (self.__N - 1))
        return

    pass


class DistPoisson(Distribucion):
    """
    Distribución de Poisson
    La probabilidad de que ocurra determinada cantidad de 
    sucesos independientes en un periodo de tiempo definido
    sea x: la cantidad de éxitos en un intervalo o región
    sea lamb: el periodo de tiempo definido
    """

    dict_params = {"x":"cantidad de éxitos en un intervalo o región", "lambda":"tasa de ocurrencia"}

    def __init__(self):
        super().__init__()
        self.__x = None
        self.__lamb = None
        return

    def iniciar(self, lista):
        """
        Asigna los valores de las variables de la distribución
        """
        self.__x = lista[0]
        self.__lamb = lista[1]
        self._probabilidad = ((self.__lamb ** self.__x) * (e ** (-self.__lamb))) / factorial(self.__x)
        self._esperanza = self.__lamb
        self._varianza = self.__lamb
        return

    pass


distribuciones = {"Binomial": DistBinomial,
                  "Binomial Negativa": DistBinomialNegativa,
                  "Geometrica": DistGeometrica,
                  "Hipergeometrica": DistHipergeometrica,
                  "Poisson": DistPoisson,
                  }
