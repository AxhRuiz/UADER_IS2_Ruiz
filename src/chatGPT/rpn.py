#!/usr/bin/env python3
"""
Calculadora RPN Científica - Versión Final.

Este módulo implementa una calculadora en Notación Polaca Inversa (RPN)
con soporte para operaciones básicas, funciones científicas, trigonometría
en grados y sistema de 10 memorias (00-09).

Autor: Axel Ruiz
Fecha: 2026
"""

import math
import sys
from typing import Final  # MEJORA 4: Importar Final para variables constantes


class RPNError(Exception):
    """
    Excepción personalizada para errores de la calculadora RPN.
    CORRECCIÓN W0107: Se eliminó 'pass' innecesario y se agregó docstring.
    """


# Constantes matemáticas
_CONST = {
    "p": math.pi,
    "pi": math.pi,
    "e": math.e,
    "j": (1 + math.sqrt(5)) / 2,
    "phi": (1 + math.sqrt(5)) / 2,
}

# Texto de ayuda
_HELP = """
Operadores: + - * x /
Constantes: p/pi  e  j/phi
Funciones : sqrt log ln exp/ex 10x pow/yx/^ inv/1/x chs/neg
Trig(grad): sin cos tg/tan asin acos atg/atan
Pila      : dup swap drop clear/clr
Memoria   : sto XX  rcl XX  (XX=00..09)
Especial  : help
"""

# Tablas de despacho
# MEJORA 4: Agregado Final para indicar que son constantes (no modificables)
_STACK_CMDS: Final = {"dup", "swap", "drop", "clear", "clr"}
_MEM_CMDS: Final = {"sto", "rcl"}
_ARITH_OPS: Final = {"+", "-", "*", "x", "X", "/"}
_MATH_FNS: Final = {
    "sqrt",
    "log",
    "ln",
    "exp",
    "ex",
    "10x",
    "pow",
    "yx",
    "^",
    "inv",
    "1/x",
    "chs",
    "neg",
}
_TRIG_FNS: Final = {"sin", "cos", "tg", "tan", "asin", "acos", "atg", "atan"}


class CalculadoraRPN:
    """
    Calculadora en Notación Polaca Inversa (RPN).

    Atributos:
        pila: Lista que actúa como stack LIFO para operandos.
        mem: Lista de 10 posiciones para memorias 00-09.
    """

    def __init__(self):
        """Inicializa pila vacía y 10 memorias en cero."""
        self.pila = []
        self.mem = [0.0] * 10

    def _error(self, msg):
        """Lanza una excepción RPNError con el mensaje dado."""
        raise RPNError(msg)

    def _to_num(self, token):
        """
        Convierte un token a número (int o float).

        Args:
            token: Cadena a convertir.

        Returns:
            int o float si es válido, None en caso contrario.
        """
        try:
            return float(token) if "." in token or "e" in token.lower() else int(token)
        except ValueError:
            return None

    def _pop1(self):
        """Extrae y retorna el tope de la pila. Lanza error si está vacía."""
        if not self.pila:
            self._error("Pila vacía, se necesita 1 valor")
        return self.pila.pop()

    def _pop2(self):
        """Extrae y retorna los dos valores del tope de la pila."""
        if len(self.pila) < 2:
            self._error("Se necesitan 2 valores en la pila")
        b, a = self.pila.pop(), self.pila.pop()
        return a, b

    # ------------------------------------------------------------------
    # Manejadores por categoría
    # ------------------------------------------------------------------

    def _handle_stack(self, tl):
        """Ejecuta comandos de manipulación de pila: dup, swap, drop, clear."""
        if tl == "dup":
            x = self._pop1()
            self.pila.extend([x, x])
        elif tl == "swap":
            a, b = self._pop2()
            self.pila.extend([b, a])
        elif tl == "drop":
            self._pop1()
        else:  # clear, clr
            self.pila.clear()

    def _handle_mem(self, tl, tokens, i):
        """Ejecuta comandos de memoria STO/RCL."""
        if i + 1 >= len(tokens):
            self._error(f"{tl.upper()} requiere índice 00-09")
        idx = tokens[i + 1]
        # MEJORA 6: Validación más estricta del índice de memoria
        if not (len(idx) == 2 and idx[0] == "0" and idx[1] in "0123456789"):
            self._error(f"Índice inválido: '{idx}'. Use formato 00-09.")
        addr = int(idx[1])
        if tl == "sto":
            if not self.pila:
                self._error("STO: pila vacía")
            self.mem[addr] = self.pila[-1]
        else:  # rcl
            self.pila.append(self.mem[addr])
        return i + 1

    def _handle_arith(self, tl):
        """Ejecuta operaciones aritméticas básicas: +, -, *, /."""
        a, b = self._pop2()
        if tl == "+":
            self.pila.append(a + b)
        elif tl == "-":
            self.pila.append(a - b)
        elif tl in ("*", "x", "X"):
            self.pila.append(a * b)
        else:  # "/"
            if b == 0:
                self._error("División por cero")
            self.pila.append(a / b)

    # CORRECCIÓN C0116: Se agregó docstring a la función _handle_math
    # ANTES: def _handle_math(self, tl): (sin docstring)
    def _handle_math(self, tl):
        """
        Ejecuta funciones matemáticas: sqrt, log, ln, exp, 10x, pow, inv, chs.

        NOTA PYLINT R0912: Esta función tiene 14 ramificaciones (supera las 12
        recomendadas). Se decidió NO refactorizar porque maneja 8 funciones
        matemáticas distintas, cada una con validaciones de dominio específicas.
        Separarlas aumentaría la complejidad total del módulo.
        """
        # MEJORA 7: Uso de match/case (Python 3.11) en lugar de if/elif
        match tl:
            case "chs" | "neg":
                self.pila.append(-self._pop1())
            case "inv" | "1/x":
                x = self._pop1()
                if x == 0:
                    self._error("División por cero")
                self.pila.append(1 / x)
            case "sqrt":
                x = self._pop1()
                if x < 0:
                    self._error("sqrt de negativo")
                self.pila.append(math.sqrt(x))
            case "ln":
                x = self._pop1()
                if x <= 0:
                    self._error("ln de no positivo")
                self.pila.append(math.log(x))
            case "log":
                x = self._pop1()
                if x <= 0:
                    self._error("log de no positivo")
                self.pila.append(math.log10(x))
            case "exp" | "ex":
                self.pila.append(math.exp(self._pop1()))
            case "10x":
                self.pila.append(10 ** self._pop1())
            case "pow" | "yx" | "^":
                a, b = self._pop2()
                if a == 0 and b <= 0:
                    self._error("0^<=0 inválido")
                if a < 0 and isinstance(b, float) and not b.is_integer():
                    self._error("Base negativa con exponente fraccionario")
                self.pila.append(a**b)

    def _handle_trig(self, tl):
        """Ejecuta funciones trigonométricas en grados"""
        x = self._pop1()
        if tl == "sin":
            self.pila.append(math.sin(math.radians(x)))
        elif tl == "cos":
            self.pila.append(math.cos(math.radians(x)))
        elif tl in ("tg", "tan"):
            if abs(x % 180 - 90) < 1e-12:
                self._error("tan indefinida en 90°")
            self.pila.append(math.tan(math.radians(x)))
        elif tl == "asin":
            if not -1 <= x <= 1:
                self._error("asin fuera de [-1,1]")
            self.pila.append(math.degrees(math.asin(max(-1, min(1, x)))))
        elif tl == "acos":
            if not -1 <= x <= 1:
                self._error("acos fuera de [-1,1]")
            self.pila.append(math.degrees(math.acos(max(-1, min(1, x)))))
        elif tl in ("atg", "atan"):
            self.pila.append(math.degrees(math.atan(x)))

    # ------------------------------------------------------------------
    # Evaluación principal
    # ------------------------------------------------------------------

    def evaluar(self, expr):
        """
        Evalúa una expresión RPN y retorna el resultado.

        Args:
            expr: Cadena con la expresión en notación polaca inversa.

        Returns:
            El valor resultante (int o float).

        Raises:
            RPNError: Si hay errores de sintaxis, pila insuficiente, etc.
        """
        self.pila.clear()
        tokens = expr.strip().split()
        i = 0

        while i < len(tokens):
            t = tokens[i]
            tl = t.lower()

            if tl == "help":
                print(_HELP)
                i += 1
                continue
            if tl in _CONST:
                self.pila.append(_CONST[tl])
            elif tl in _STACK_CMDS:
                self._handle_stack(tl)
            elif tl in _MEM_CMDS:
                i = self._handle_mem(tl, tokens, i)
            elif tl in _ARITH_OPS:
                self._handle_arith(tl)
            elif tl in _MATH_FNS:
                self._handle_math(tl)
            elif tl in _TRIG_FNS:
                self._handle_trig(tl)
            elif (num := self._to_num(t)) is not None:
                self.pila.append(num)
            else:
                self._error(f"Token inválido: {t}")
            i += 1

        if len(self.pila) != 1:
            self._error(f"Pila final debe tener 1 elemento, tiene {len(self.pila)}")
        return self.pila[0]


# CORRECCIÓN C0116: Se agregó docstring a la función fmt
# ANTES: def fmt(valor): (sin docstring)
def fmt(valor):
    """
    Formatea el resultado: entero sin .0, float normal.

    Args:
        valor: Número a formatear.

    Returns:
        int si es entero, float en caso contrario.
    """
    return int(valor) if isinstance(valor, float) and valor.is_integer() else valor


def main():
    """
    Punto de entrada principal.

    Modo 1: python rpn.py "3 4 +"  (argumentos)
    Modo 2: python rpn.py           (stdin interactivo)
    """
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        try:
            print(fmt(CalculadoraRPN().evaluar(expr)))
        except RPNError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("RPN> ", end="")
        # MEJORA 5: Manejo de KeyboardInterrupt para salida limpia con Ctrl+C
        try:
            for linea in sys.stdin:
                linea = linea.strip()
                if not linea:
                    break
                try:
                    print(fmt(CalculadoraRPN().evaluar(linea)))
                except RPNError as e:
                    print(f"Error: {e}")
                print("RPN> ", end="")
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            sys.exit(0)


if __name__ == "__main__":
    main()

# CORRECCIÓN C0304: Se agregó nueva línea al final del archivo
# ANTES: El archivo terminaba en la línea anterior sin salto de línea