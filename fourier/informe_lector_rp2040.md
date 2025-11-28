¿Que Hace?
 
 Esta clase Lector que encapsula el acceso a un convertidor analógico‑digital (ADC). Al instanciarla con un número de pin, crea un objeto ADC ligado a ese pin. Ofrece dos operaciones principales: leer un valor crudo (tomar_lectura_bits) y tomar una secuencia de lecturas (muestrear_bits) con un retardo entre cada lectura. La salida es una lista de enteros que representan la conversión analógica→digital.
```python
from machine import ADC, Pin
import time

class Lector:
    def __init__(self, pin:int):   # aseguramos init
        self.adc = ADC(Pin(pin))

    def tomar_lectura_bits(self) -> int:
        # Lectura cruda en bits (0–65535)
        return self.adc.read_u16()

    def muestrear_bits(self, n:int, intervalo:float=0.001):
        # Toma n muestras en bits
        muestra = []
        for _ in range(n):
            l = self.tomar_lectura_bits()
            muestra.append(l)
            time.sleep(intervalo)
        return muestra
```