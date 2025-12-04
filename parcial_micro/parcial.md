# Indice de los Modulos

```
C:.
│   __init__.py
│
├───modulo_fourier
│   │   fft.md
│   │   fourier_transform.py
│   │   grafica.py
│   │   informe_fourier_transform.md
│   │   informe_lector_rp2040.md
│   │   lector_rp2040.py
│   │   __init__.py
│   │
│   └───__pycache__
│           fourier_transform.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───puertos
│   │   puertos.py
│   │   __init__.py
│   │
│   └───__pycache__
│           puertos.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───signal
│   │   analyzer.py
│   │   __init__.py
│   │
│   └───__pycache__
│           analyzer.cpython-314.pyc
│           __init__.cpython-314.pyc
│
└───__pycache__
        __init__.cpython-314.pyc

```

# Informe de la estructura de módulos del proyecto

## 1. Carpeta raíz (C:.)

### __init__.py

Indica que la carpeta raíz puede ser tratada como un paquete Python.

Permite importar submódulos (modulo_fourier, puertos, signal) desde el proyecto principal.

Generalmente vacío, pero puede contener configuraciones globales.

## 2. Módulo modulo_fourier
Este módulo concentra todo lo relacionado con la transformada de Fourier y el procesamiento matemático de señales.

### fourier_transform.py

Contiene las clases y funciones para realizar la DFT (Transformada Discreta de Fourier) y la FFT (Transformada Rápida de Fourier).

Incluye métodos para calcular magnitud y fase de los números complejos resultantes.

Es el núcleo matemático del proyecto.

### grafica.py

Script dedicado a la visualización con matplotlib.

Permite graficar magnitud y fase del espectro FFT.

Se usa como herramienta de análisis visual complementaria.

### lector_rp2040.py

Encargado de la lectura de señales desde el microcontrolador RP2040 (ej. Raspberry Pi Pico).

Utiliza la librería serial para recibir datos por el puerto COM.

Actúa como puente entre hardware y software.

### fft.md

Documento de apoyo con teoría o ejemplos sobre la FFT.

Sirve como referencia conceptual.

### informe_fourier_transform.md

Informe técnico/documentación sobre la implementación de la transformada de Fourier en el proyecto.

Explica resultados, pruebas y aplicaciones.

### informe_lector_rp2040.md

Documento que describe el proceso de lectura de señales desde el RP2040.

Incluye detalles de conexión, configuración de puertos y pruebas realizadas.

__init__.py

Permite importar las funciones de este módulo como paquete (from modulo_fourier import fourier_transform).

__pycache__/

Carpeta generada automáticamente por Python con archivos compilados (.pyc).

Mejora la velocidad de ejecución, pero no se edita manualmente.

## 3. Módulo puertos
Este módulo gestiona la detección y configuración de puertos seriales.

### puertos.py

Contiene la clase Puertos, que lista los puertos disponibles en el sistema.

Permite seleccionar el puerto correcto (ej. COM3) para la comunicación con el RP2040.

__init__.py

Hace que puertos sea un paquete importable.

__pycache__/

Archivos compilados de Python para ejecución más rápida.

## 4. Módulo signal
Este módulo se encarga de la adquisición y análisis de señales.

### analyzer.py

Contiene la clase Analyzer, que lee los valores provenientes del puerto serial.

Prepara los datos para ser procesados por la transformada de Fourier.

Es el puente entre la entrada física (puerto) y el procesamiento matemático (modulo_fourier).

### __init__.py

Permite importar Analyzer como parte del paquete signal.

### __pycache__/

Archivos compilados de Python.

## 5. Carpeta raíz __pycache__/
Contiene archivos compilados de los __init__.py principales.

No se modifica manualmente, es generado automáticamente por Python.