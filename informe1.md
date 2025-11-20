# Convertidor analogico digital

Descripción del funcionamiento
## Clase Lector:
Se crea una clase que encapsula el uso del ADC (convertidor analógico-digital) en un pin específico de la placa (en este caso, el pin GP26 → ADC0).
### El método tomar_lectura():
Obtiene una lectura cruda del ADC (un valor entre 0 y 65535).
Convierte ese valor en un voltaje proporcional dentro del rango de 0 a 3.3 V.
Devuelve el voltaje como un número de tipo float.
### El método muestrear(n, intervalo):
Toma n lecturas consecutivas del ADC.
Entre cada lectura espera un tiempo definido por intervalo (en segundos).
Devuelve una lista con todas las lecturas obtenidas.

## Bucle principal (while True)
El programa entra en un ciclo infinito que realiza lo siguiente:
Lectura instantánea:
Llama a tomar_lectura() y muestra en pantalla el voltaje actual leído por el ADC.
Muestreo de varias lecturas:
Llama a muestrear(5, intervalo=0.2), lo que significa que toma 5 lecturas con una pausa de 0.2 segundos entre cada una.
Imprime esas lecturas en formato de lista, con tres decimales.

## Pausa entre ciclos:
Espera 2 segundos antes de repetir el proceso, evitando que el bucle sea demasiado rápido.


````python

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

````