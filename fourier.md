# ¿Como funciona el codigo?

Esta clase TransformadaFourier agrupa una señal y dos operaciones relacionadas: calcular su transformada discreta (DFT) y obtener la magnitud de un número complejo. La idea es encapsular datos (la señal) y comportamientos (cálculo y utilidad de magnitud) para usarlos de forma ordenada.

## Atributos de la clase
self.señal Guarda la lista de muestras en el dominio del tiempo (por ejemplo amplitudes muestreadas).

self.N Número de muestras de la señal; se usa para controlar los bucles y normalizar cálculos.

self.transformada Inicialmente None. Después de ejecutar dft() contendrá la lista de valores complejos que representan la señal en el dominio de la frecuencia.

## Método dft Qué hace y por qué
Propósito Calcular la Transformada Discreta de Fourier de la señal: convertir la representación tiempo en una representación frecuencia que indica cuánto contribuye cada frecuencia a la señal original.

Entrada Usa self.señal y self.N (no recibe parámetros externos).

Salida Devuelve una lista de números complejos; además guarda ese resultado en self.transformada.

## Flujo de ejecución paso a paso

Crea una lista vacía X para almacenar los resultados por cada índice de frecuencia k.

Para cada frecuencia k entre 0 y N-1 inicia una suma acumuladora.

Recorre todas las muestras n y añade la contribución de la muestra n a la frecuencia k (esa contribución es un número complejo).

Al terminar el bucle sobre n añade la suma a X.

Guarda X en self.transformada y lo devuelve.

## Qué se busca con este método 

Obtener el espectro de la señal: identificar qué frecuencias están presentes y con qué intensidad.

Costo y limitaciones Ejecuta dos bucles anidados sobre N, por eso su coste es O(N²). Para señales largas es ineficiente; en la práctica se usa FFT para acelerar el cálculo.

## Método abs_complejo_formula Qué hace y por qué
Propósito Calcular la magnitud (valor absoluto) de un número complejo y devolverla como un complex cuya parte imaginaria es cero. Esto facilita usar magnitudes en contextos que esperan valores complejos.

Entrada Un valor z que puede ser complejo o real.

Salida Un complex con la magnitud en la parte real y 0 en la parte imaginaria.

Comportamiento

Si z es complejo extrae sus partes real e imaginaria y calcula la magnitud a partir de ellas.

Si z no es complejo intenta aplicar abs(z) y convertir el resultado a complex.

Si ocurre un error lanza TypeError con un mensaje explicativo.

En el código actual el método está definido sin self y sin @staticmethod. Para evitar errores al llamarlo desde una instancia debe declararse con @staticmethod o aceptar self como primer parámetro. Actualmente, si llamas instancia.abs_complejo_formula(...) Python intentará pasar self como primer argumento y fallará.

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
```