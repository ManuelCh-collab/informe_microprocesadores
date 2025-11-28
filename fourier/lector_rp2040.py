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