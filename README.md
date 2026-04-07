# 🧮 Calculadora de Ecuaciones Diferenciales (ED) - Python
Desarrollado por Jeremy Ramirez Escobar | Estudiante de Software UTNA.

Este proyecto es una herramienta avanzada de línea de comandos para la resolución de Ecuaciones Diferenciales Ordinarias (EDO). Lo que hace especial a este script es su enfoque híbrido: puede resolver ecuaciones de forma simbólica (exacta) o mediante métodos numéricos (aproximados).

# 🚀 Características Principales
Motor Simbólico (SymPy): Resolución exacta de ecuaciones de primer y segundo orden.

Normalización Inteligente: Uso de Expresiones Regulares (RegEx) para convertir la entrada del usuario (ej: y'' + y') en objetos matemáticos procesables por el sistema.

Resolución Numérica (Método de Euler): Implementación manual del algoritmo de Euler para obtener aproximaciones cuando la resolución simbólica no es posible o la librería no está presente.

Evaluador Dinámico: Capacidad de evaluar funciones matemáticas complejas (sin, exp, log, sqrt) de forma segura.

# 🛠️ Stack Tecnológico
Lenguaje: Python 3.x

Librerías Críticas: * SymPy: Computación simbólica.

re: Procesamiento de cadenas y normalización de sintaxis.

math: Operaciones matemáticas de bajo nivel para el motor numérico.
# 🚀 Desafíos Matemáticos y Lógicos

A diferencia de aplicaciones gráficas pesadas, esta herramienta se enfoca en la velocidad y el procesamiento lógico:Entrada de Datos por Consola: Interfaz interactiva donde el usuario define la ecuación y las condiciones iniciales directamente en la terminal.Resolución de Modelos Reales: Implementación de algoritmos para resolver problemas de masa-resorte y modelos de mezcla de tanques, identificando variables clave como $q(t)$.Salida de Resultados: Presentación de soluciones generales y particulares en formato legible directamente en el standard output.Cálculo Exacto: Uso de librerías científicas para evitar errores de redondeo en soluciones simbólicas complejas.

# 💻 Guía de Uso (Terminal)
Instalación
Asegúrate de tener Python instalado y las dependencias listas:


             pip install sympy
Ejecución
Para iniciar la calculadora, navega hasta la carpeta del proyecto y ejecuta:


            python main.py


            pip install sympy

Normalización con RegEx
El script utiliza patrones de búsqueda para permitir que el usuario escriba de forma natural:
Ejemplo de flujo en terminal:

            # Convierte "y'" en una derivada entendible por SymPy
            ecuacion = ecuacion.replace(f"{funcion}'", f"Derivative({funcion}({variable}), {variable})")
                   Escriba la ecuación diferencial: y'' - 3*y' + 2*y = 0
# 📦 Instalación y Uso
Clonar y preparar:

    git clone https://github.com/jeremyramirez206-max/EDO-Solver-Python
    cd EDO-Solver-Python
    
Instalar dependencias (Opcional para modo simbólico):

    pip install sympy
    
Ejecutar:

    python main.py

# 💡 Nota de Autor
Este proyecto demuestra la capacidad de integrar lógica matemática avanzada con técnicas de programación limpia, manejo de excepciones y procesamiento de texto, habilidades fundamentales para el desarrollo de software de ingeniería.

# 🎓 Propósito Académico
Este script fue desarrollado para validar resultados en la materia de Ecuaciones Diferenciales, sirviendo como puente entre el cálculo avanzado y la automatización mediante Python.

# 📬 Contacto
Portafolio: github.com/jeremyramirez206-max

LinkedIn: www.linkedin.com/in/jeremy-ramirez-escobar
