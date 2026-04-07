"""Calculadora básica de ecuaciones diferenciales (EDO).

Si SymPy está instalado, puede resolver ecuaciones de primer y segundo orden simbólicamente.
Si no, ofrece un cálculo numérico básico para ecuaciones de primer orden en la forma y' = f(x, y).
"""

import math
import re

HAS_SYMPY = False
try:
    from sympy import (
        symbols,
        Function,
        Eq,
        dsolve,
        sympify,
        Derivative,
        pprint,
    )
    HAS_SYMPY = True
except ImportError:
    print("SymPy no está instalado. Solo resolución numérica disponible.")


def normalizar(ecuacion: str, variable: str, funcion: str) -> str:
    ecuacion = ecuacion.replace(" ", "")
    ecuacion = ecuacion.replace(f"{funcion}''", f"Derivative({funcion}({variable}), ({variable}, 2))")
    ecuacion = ecuacion.replace(f"{funcion}'", f"Derivative({funcion}({variable}), {variable})")
    pattern = rf'(?<![A-Za-z0-9_]){funcion}(?![A-Za-z0-9_\(])'
    ecuacion = re.sub(pattern, f"{funcion}({variable})", ecuacion)
    return ecuacion


if HAS_SYMPY:
    def resolver_simb():
        variable = input("Variable independiente (por defecto x): ").strip() or "x"
        funcion = input("Función dependiente (por defecto y): ").strip() or "y"

        print("\nEscribe la ecuación diferencial con y, y' y y''.")
        print("Ejemplos: y' + y = x, y'' - 3*y' + 2*y = sin(x), y' = x*y")
        ecuacion = input("Ecuación: ").strip()
        if not ecuacion:
            print("No se ingresó ninguna ecuación.")
            return

        ecuacion = normalizar(ecuacion, variable, funcion)
        try:
            if "=" in ecuacion:
                izquierda, derecha = ecuacion.split("=", 1)
                expr = Eq(
                    sympify(izquierda, locals={variable: symbols(variable), funcion: Function(funcion)(symbols(variable)), "Derivative": Derivative}),
                    sympify(derecha, locals={variable: symbols(variable), funcion: Function(funcion)(symbols(variable)), "Derivative": Derivative}),
                )
            else:
                expr = Eq(
                    sympify(ecuacion, locals={variable: symbols(variable), funcion: Function(funcion)(symbols(variable)), "Derivative": Derivative}),
                    0,
                )
            solucion = dsolve(expr, Function(funcion)(symbols(variable)))
            print("\nSolución encontrada:")
            pprint(solucion)
        except Exception as e:
            print("No se pudo resolver la ecuación:", e)
            print("Revisa la sintaxis o inténtalo con una ecuación más simple.")
else:
    def resolver_simb():
        print("La resolución simbólica no está disponible porque SymPy no está instalado.")
        print("Instala SymPy con: pip install sympy")


def evaluar_funcion(expr: str, x_val: float, y_val: float) -> float:
    funciones = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
    }
    variables = {"x": x_val, "y": y_val}
    return eval(expr, {"__builtins__": None}, {**funciones, **variables})


def resolver_num():
    print("\nResuelve ecuaciones de primer orden en la forma y' = f(x, y).")
    print("Ejemplo: y' = x + y")
    ecuacion = input("Ecuación: ").strip()
    if "=" not in ecuacion:
        print("Debes ingresar una ecuación con '='.")
        return

    izquierda, derecha = [parte.strip() for parte in ecuacion.split("=", 1)]
    if "y'" not in izquierda and "y'" not in derecha:
        print("La ecuación debe contener y'.")
        return

    if "y'" in izquierda:
        funcion_expr = derecha
    else:
        funcion_expr = izquierda

    try:
        x0 = float(input("Valor inicial x0: ").strip())
        y0 = float(input("Valor inicial y0: ").strip())
        x_fin = float(input("Valor final x: ").strip())
        pasos = int(input("Número de pasos (ej. 100): ").strip())
    except ValueError:
        print("Valores numéricos inválidos.")
        return

    detalle = input("¿Mostrar todos los pasos de Euler? (s/n): ").strip().lower() == "s"
    h = (x_fin - x0) / pasos
    x = x0
    y = y0

    if detalle:
        print("\nPaso 0: x = {:.6g}, y = {:.6g}".format(x, y))

    for paso in range(1, pasos + 1):
        try:
            dydx = evaluar_funcion(funcion_expr, x, y)
        except Exception as e:
            print("Error al evaluar la función:", e)
            return
        y = y + h * dydx
        x = x + h
        if detalle:
            print(f"Paso {paso}: x = {x:.6g}, y = {y:.6g}, y' = {dydx:.6g}")

    print("\nResultado aproximado con Euler:")
    print(f"x = {x:.6g}, y ≈ {y:.6g}")


def main():
    print("=== Calculadora básica de EDO ===")
    while True:
        print("\nOpciones:")
        if HAS_SYMPY:
            print("  1) Resolver simbólicamente")
            print("  2) Resolver numéricamente")
            print("  3) Salir")
        else:
            print("  1) Resolver numéricamente")
            print("  2) Salir")
        opcion = input("Selecciona una opción: ").strip()

        if HAS_SYMPY:
            if opcion == "1":
                resolver_simb()
            elif opcion == "2":
                resolver_num()
            elif opcion == "3":
                print("Hasta luego.")
                break
            else:
                print("Opción inválida. Ingresa 1, 2 o 3.")
        else:
            if opcion == "1":
                resolver_num()
            elif opcion == "2":
                print("Hasta luego.")
                break
            else:
                print("Opción inválida. Ingresa 1 o 2.")


if __name__ == "__main__":
    main()
