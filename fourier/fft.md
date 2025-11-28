# FFT

El objetivo principal de esta función es tomar una señal (una secuencia de valores en el dominio del tiempo o del espacio) y transformarla en su representación en el dominio de la frecuencia. Esto significa que te dice qué frecuencias componen la señal original y con qué intensidad.

``` python

def fft(self) -> List[complex]:
        """
        Calcula la Transformada Rápida de Fourier (FFT) usando el algoritmo recursivo Cooley–Tukey.
        Requiere que la longitud de la señal sea potencia de 2.
        """
        def _fft(x: List[complex]) -> List[complex]:
            n = len(x)
            if n <= 1:
                return x
            even = _fft(x[0::2])
            odd = _fft(x[1::2])
            T = [cmath.exp(-2j * math.pi * k / n) * odd[k] for k in range(n // 2)]
            return [even[k] + T[k] for k in range(n // 2)] + \
                   [even[k] - T[k] for k in range(n // 2)]

        # Convertimos la señal a complejos
        señal_c: List[complex] = [complex(x, 0) for x in self.señal]
        X: List[complex] = _fft(señal_c)
        self.transformada = X
        return X

```

