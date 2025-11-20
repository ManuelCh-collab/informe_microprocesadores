#  Titulo del informe

```python
from machine import ADC, Pin
import time

class Lector:
    def __init__(self, pin:int):
        # Inicializa el ADC en el pin indicado
        self.adc = ADC(Pin(pin))

    def tomar_lectura(self) -> float:
        # Lectura cruda (0–65535) convertida a voltaje (0–3.3 V)
        valor = self.adc.read_u16()
        voltaje = (valor / 65535) * 3.3
        return voltaje

    def muestrear(self, n:int, intervalo:float=0.1):
        # Toma n muestras con un intervalo en segundos
        muestra = []
        for _ in range(n):
            l = self.tomar_lectura()
            muestra.append(l)
            time.sleep(intervalo)
        return muestra

````
# -------------------------------
# Uso en un bucle infinito
# -------------------------------

lector = Lector(26)  # GP26 → ADC0

while True:
    # Lectura continua
    lectura = lector.tomar_lectura()
    print(f"Voltaje instantáneo: {lectura:.3f} V")

    # Bloque de muestreo (ejemplo: 5 muestras cada ciclo)
    datos = lector.muestrear(5, intervalo=0.2)
    print("Muestras:", [f"{d:.3f}" for d in datos])

    # Pausa entre ciclos
    time.sleep(2)
```