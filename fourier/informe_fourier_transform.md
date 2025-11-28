# ¿Que hace este codigo?

Este código define una clase siendo esta Class TransformadaFourier la cual recibe una señal discreta y calcula su Transformada Discreta de Fourier (DFT), además de ofrecer funciones para obtener la magnitud y la fase de números complejos. La DFT descompone la señal en componentes de frecuencia y el resultado se guarda en self.transformada para uso posterior.

```python
import math
import cmath

class TransformadaFourier:
    def __init__(self, señal: list):
        """
        Inicializa la clase con una señal (lista de números).
        """
        self.señal = señal
        self.N = len(señal)
        self.transformada = None

    def dft(self) -> list:
        """
        Calcula la Transformada Discreta de Fourier (DFT) de la señal.
        """
        X = []
        for k in range(self.N):
            suma = 0
            for n in range(self.N):
                angulo = -2j * math.pi * k * n / self.N
                suma += self.señal[n] * cmath.exp(angulo)
            X.append(suma)
        self.transformada = X
        return X

    def abs_complejo_formula(z: complex) -> complex:
        """
        Calcula el valor absoluto de un número complejo y lo devuelve como complejo.
        """
        if isinstance(z, complex):
            a = z.real
            b = z.imag
            magnitud = math.sqrt(a*a + b*b)
            return complex(magnitud, 0)
        try:
            return complex(abs(z), 0)
        except Exception as e:
            raise TypeError(f"No se pudo calcular |z| para tipo {type(z)}: {e}")

    def fase(z: complex) -> float:
        """
        Calcula la fase (argumento) de un número complejo en radianes.
        """
        return cmath.phase(z)
```