#!/usr/bin/env python3
"""
test_funcional.py - Tests funcionales para la calculadora RPN.
Ejecuta el programa completo y verifica su comportamiento.
"""

import subprocess
import sys
import unittest


class TestFuncionalRPN(unittest.TestCase):
    """Tests funcionales que ejecutan el programa completo."""

    def ejecutar_rpn(self, entrada=None, argumentos=None):
        """
        Ejecuta rpn.py y retorna (codigo_salida, stdout, stderr).
        
        Args:
            entrada: String a enviar por stdin (modo interactivo)
            argumentos: Lista de argumentos (modo CLI)
        """
        cmd = [sys.executable, "rpn.py"]
        if argumentos:
            cmd.extend(argumentos)
        
        proceso = subprocess.run(
            cmd,
            input=entrada,
            capture_output=True,
            text=True,
            timeout=5
        )
        return proceso.returncode, proceso.stdout.strip(), proceso.stderr.strip()

    # ------------------------------------------------------------------
    # Casos de Prueba Funcionales
    # ------------------------------------------------------------------

    def test_caso_01_suma_basica(self):
        """Caso 01: Suma básica - 3 4 + = 7"""
        code, out, err = self.ejecutar_rpn(argumentos=["3", "4", "+"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "7")

    def test_caso_02_expresion_compleja(self):
        """Caso 02: Expresión compleja - 5 1 2 + 4 * + 3 - = 14"""
        code, out, err = self.ejecutar_rpn(argumentos=["5", "1", "2", "+", "4", "*", "+", "3", "-"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "14")

    def test_caso_03_trigonometria(self):
        """Caso 03: Trigonometría - 45 sin = 0.707106..."""
        code, out, err = self.ejecutar_rpn(argumentos=["45", "sin"])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("0.707106"))

    def test_caso_04_constante_pi(self):
        """Caso 04: Constante π - p 2 / = 1.570796..."""
        code, out, err = self.ejecutar_rpn(argumentos=["p", "2", "/"])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("1.570796"))

    def test_caso_05_memorias(self):
        """Caso 05: Uso de memorias - 5 sto 00 3 * rcl 00 + = 20"""
        code, out, err = self.ejecutar_rpn(argumentos=["5", "sto", "00", "3", "*", "rcl", "00", "+"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "20")

    def test_caso_06_error_division_cero(self):
        """Caso 06: División por cero - debe mostrar error y código 1"""
        code, out, err = self.ejecutar_rpn(argumentos=["3", "0", "/"])
        self.assertEqual(code, 1)
        self.assertIn("Error", err)

    def test_caso_07_error_token_invalido(self):
        """Caso 07: Token inválido - debe mostrar error"""
        code, out, err = self.ejecutar_rpn(argumentos=["hola"])
        self.assertEqual(code, 1)
        self.assertIn("Error", err)

    def test_caso_08_error_pila_insuficiente(self):
        """Caso 08: Pila insuficiente - 4 + debe dar error"""
        code, out, err = self.ejecutar_rpn(argumentos=["4", "+"])
        self.assertEqual(code, 1)
        self.assertIn("Error", err)

    def test_caso_09_floats_negativos(self):
        """Caso 09: Números negativos y decimales - -3.5 2.5 + = -1.0"""
        code, out, err = self.ejecutar_rpn(argumentos=["-3.5", "2.5", "+"])
        self.assertEqual(code, 0)
        # Aceptar tanto "-1" como "-1.0" (fmt() elimina .0 en enteros)
        self.assertIn(out, ["-1", "-1.0"])

    def test_caso_10_potencia(self):
        """Caso 10: Potencia - 2 3 pow = 8"""
        code, out, err = self.ejecutar_rpn(argumentos=["2", "3", "pow"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "8")

    def test_caso_11_raiz_cuadrada(self):
        """Caso 11: Raíz cuadrada - 16 sqrt = 4"""
        code, out, err = self.ejecutar_rpn(argumentos=["16", "sqrt"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "4")

    def test_caso_12_logaritmo(self):
        """Caso 12: Logaritmo base 10 - 100 log = 2"""
        code, out, err = self.ejecutar_rpn(argumentos=["100", "log"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "2")

    def test_caso_13_modo_interactivo(self):
        """Caso 13: Modo interactivo por stdin"""
        entrada = "3 4 +\n"
        code, out, err = self.ejecutar_rpn(entrada=entrada)
        self.assertEqual(code, 0)
        # El modo interactivo imprime prompts, extraer solo el resultado
        # out tiene formato: "RPN> 7\nRPN>"
        lineas = out.strip().split('\n')
        resultado = [l for l in lineas if l and not l.startswith('RPN>')]
        if not resultado:
            # Si no hay línea sin prompt, buscar el número después de "RPN> "
            for l in lineas:
                if 'RPN>' in l:
                    resultado = [l.replace('RPN>', '').strip()]
                    break
        self.assertIn("7", resultado[0] if resultado else "")

    def test_caso_14_comando_help(self):
        """Caso 14: Comando help - debe mostrar ayuda"""
        entrada = "help\n"
        code, out, err = self.ejecutar_rpn(entrada=entrada)
        self.assertEqual(code, 0)
        self.assertIn("Operadores", out)

    def test_caso_15_comando_clear(self):
        """Caso 15: Comando clear - 1 2 3 clear 5 = 5"""
        code, out, err = self.ejecutar_rpn(argumentos=["1", "2", "3", "clear", "5"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "5")


if __name__ == "__main__":
    unittest.main(verbosity=2)