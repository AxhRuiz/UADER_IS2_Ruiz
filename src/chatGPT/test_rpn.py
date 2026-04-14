
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_rpn.py - Suite de pruebas unitarias para Calculadora RPN
Versión corregida - Compatible con rpn.py compacto
"""

import unittest
import math
import sys
from io import StringIO
from unittest.mock import patch

# Importar solo lo que existe en rpn.py compacto
from rpn import CalculadoraRPN, RPNError

# Crear alias para las excepciones (en rpn.py compacto solo existe RPNError)
TokenInvalidoError = RPNError
PilaInsuficienteError = RPNError
DivisionPorCeroError = RPNError
PilaFinalIncorrectaError = RPNError
ErrorDominioMatematico = RPNError
ErrorMemoriaInvalida = RPNError
ErrorIndiceMemoria = RPNError

# ==============================================================================
#  CLASE PRINCIPAL DE PRUEBAS
# ==============================================================================

class TestCalculadoraRPNBasica(unittest.TestCase):
    """Pruebas de funcionalidades básicas."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_suma_enteros(self):
        self.assertEqual(self.calc.evaluar("3 4 +"), 7)
        self.assertEqual(self.calc.evaluar("5 1 2 + 4 * + 3 -"), 14)
        self.assertEqual(self.calc.evaluar("2 3 4 * +"), 14)
        self.assertEqual(self.calc.evaluar("10 20 +"), 30)
        self.assertEqual(self.calc.evaluar("-5 10 +"), 5)
        self.assertEqual(self.calc.evaluar("-5 -10 +"), -15)
    
    def test_resta_enteros(self):
        self.assertEqual(self.calc.evaluar("10 3 -"), 7)
        self.assertEqual(self.calc.evaluar("3 10 -"), -7)
        self.assertEqual(self.calc.evaluar("-5 3 -"), -8)
    
    def test_multiplicacion_enteros(self):
        self.assertEqual(self.calc.evaluar("4 5 *"), 20)
        self.assertEqual(self.calc.evaluar("4 5 x"), 20)
        self.assertEqual(self.calc.evaluar("4 5 X"), 20)
        self.assertEqual(self.calc.evaluar("-3 4 *"), -12)
        self.assertEqual(self.calc.evaluar("0 5 *"), 0)
    
    def test_division_enteros(self):
        self.assertEqual(self.calc.evaluar("10 2 /"), 5.0)
        self.assertEqual(self.calc.evaluar("5 2 /"), 2.5)
        self.assertEqual(self.calc.evaluar("-6 2 /"), -3.0)
        self.assertEqual(self.calc.evaluar("0 5 /"), 0.0)
    
    def test_operaciones_con_floats(self):
        self.assertEqual(self.calc.evaluar("3.5 2.5 +"), 6.0)
        self.assertEqual(self.calc.evaluar("5.5 2.2 -"), 3.3)
        self.assertAlmostEqual(self.calc.evaluar("2.5 1.5 *"), 3.75)
        self.assertEqual(self.calc.evaluar("7.5 2.5 /"), 3.0)
        self.assertEqual(self.calc.evaluar("-3.5 2.0 +"), -1.5)
    
    def test_notacion_cientifica(self):
        self.assertEqual(self.calc.evaluar("1e3 2e3 +"), 3000.0)
        self.assertEqual(self.calc.evaluar("1.5e2 2 +"), 152.0)
        self.assertEqual(self.calc.evaluar("2E-3 3 +"), 3.002)
    
    def test_error_division_por_cero(self):
        with self.assertRaises(DivisionPorCeroError):
            self.calc.evaluar("3 0 /")
        with self.assertRaises(DivisionPorCeroError):
            self.calc.evaluar("5 0 /")
    
    def test_error_pila_insuficiente(self):
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("4 +")
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("*")
    
    def test_error_token_invalido(self):
        with self.assertRaises(TokenInvalidoError):
            self.calc.evaluar("hola")
        with self.assertRaises(TokenInvalidoError):
            self.calc.evaluar("3 4 &")
    
    def test_error_pila_final_incorrecta(self):
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("1 2")
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("")
    
    def test_ejemplos_requeridos(self):
        self.assertEqual(self.calc.evaluar("3 4 +"), 7)
        self.assertEqual(self.calc.evaluar("5 1 2 + 4 * + 3 -"), 14)
        self.assertEqual(self.calc.evaluar("2 3 4 * +"), 14)
        with self.assertRaises(DivisionPorCeroError):
            self.calc.evaluar("3 0 /")


class TestManipulacionPila(unittest.TestCase):
    """Pruebas de comandos de manipulación de pila."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_dup(self):
        """dup solo es válido si la expresión completa reduce a 1 valor."""
        self.assertEqual(self.calc.evaluar("5 dup *"), 25)
        self.assertEqual(self.calc.evaluar("3 dup dup * *"), 27)
        
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("3 dup")
        
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("dup")
    
    def test_swap(self):
        """swap intercambia dos valores."""
        self.assertEqual(self.calc.evaluar("2 3 swap -"), 1)
        self.assertEqual(self.calc.evaluar("10 20 swap /"), 2.0)
        self.assertEqual(self.calc.evaluar("5 10 swap drop"), 10)
        
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("1 2 swap")
        
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("5 swap")
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("swap")
    
    def test_drop(self):
        """drop elimina el tope de la pila."""
        self.assertEqual(self.calc.evaluar("5 2 drop"), 5)
        self.assertEqual(self.calc.evaluar("1 2 3 drop +"), 3)
        
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("drop")
    
    def test_clear(self):
        """clear vacía la pila."""
        self.assertEqual(self.calc.evaluar("1 2 3 clear 5"), 5)
        
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("1 2 clear")
        with self.assertRaises(PilaFinalIncorrectaError):
            self.calc.evaluar("clear")


class TestConstantes(unittest.TestCase):
    """Pruebas de constantes matemáticas."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_pi(self):
        self.assertEqual(self.calc.evaluar("p"), math.pi)
        self.assertEqual(self.calc.evaluar("pi"), math.pi)
        self.assertEqual(self.calc.evaluar("2 p *"), 2 * math.pi)
    
    def test_e(self):
        self.assertEqual(self.calc.evaluar("e"), math.e)
        self.assertAlmostEqual(self.calc.evaluar("e 1 +"), math.e + 1)
    
    def test_phi(self):
        phi = (1 + math.sqrt(5)) / 2
        self.assertEqual(self.calc.evaluar("j"), phi)
        self.assertEqual(self.calc.evaluar("phi"), phi)


class TestFuncionesMatematicas(unittest.TestCase):
    """Pruebas de funciones matemáticas."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_sqrt(self):
        self.assertEqual(self.calc.evaluar("9 sqrt"), 3.0)
        self.assertEqual(self.calc.evaluar("0 sqrt"), 0.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("-1 sqrt")
    
    def test_ln(self):
        self.assertEqual(self.calc.evaluar("1 ln"), 0.0)
        self.assertEqual(self.calc.evaluar("e ln"), 1.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("0 ln")
    
    def test_log(self):
        self.assertEqual(self.calc.evaluar("1 log"), 0.0)
        self.assertEqual(self.calc.evaluar("10 log"), 1.0)
        self.assertEqual(self.calc.evaluar("100 log"), 2.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("0 log")
    
    def test_exp(self):
        self.assertEqual(self.calc.evaluar("0 exp"), 1.0)
        self.assertEqual(self.calc.evaluar("1 exp"), math.e)
        self.assertAlmostEqual(self.calc.evaluar("2 exp"), math.e ** 2)
    
    def test_10x(self):
        self.assertEqual(self.calc.evaluar("0 10x"), 1.0)
        self.assertEqual(self.calc.evaluar("1 10x"), 10.0)
        self.assertEqual(self.calc.evaluar("2 10x"), 100.0)
    
    def test_pow_yx(self):
        self.assertEqual(self.calc.evaluar("2 3 pow"), 8.0)
        self.assertEqual(self.calc.evaluar("3 2 yx"), 9.0)
        self.assertEqual(self.calc.evaluar("-2 3 pow"), -8.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("0 0 pow")
        with self.assertRaises(DivisionPorCeroError):
            self.calc.evaluar("0 -1 pow")
    
    def test_inv_1x(self):
        self.assertEqual(self.calc.evaluar("4 inv"), 0.25)
        self.assertEqual(self.calc.evaluar("2 1/x"), 0.5)
        
        with self.assertRaises(DivisionPorCeroError):
            self.calc.evaluar("0 inv")
    
    def test_chs(self):
        self.assertEqual(self.calc.evaluar("5 chs"), -5)
        self.assertEqual(self.calc.evaluar("-3 chs"), 3)
        self.assertEqual(self.calc.evaluar("0 chs"), 0)


class TestTrigonometria(unittest.TestCase):
    """Pruebas de funciones trigonométricas en grados."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_sin(self):
        self.assertAlmostEqual(self.calc.evaluar("0 sin"), 0.0)
        self.assertAlmostEqual(self.calc.evaluar("30 sin"), 0.5)
        self.assertAlmostEqual(self.calc.evaluar("90 sin"), 1.0)
        self.assertAlmostEqual(self.calc.evaluar("180 sin"), 0.0)
    
    def test_cos(self):
        self.assertAlmostEqual(self.calc.evaluar("0 cos"), 1.0)
        self.assertAlmostEqual(self.calc.evaluar("60 cos"), 0.5)
        self.assertAlmostEqual(self.calc.evaluar("90 cos"), 0.0)
    
    def test_tg_tan(self):
        self.assertAlmostEqual(self.calc.evaluar("0 tg"), 0.0)
        self.assertAlmostEqual(self.calc.evaluar("45 tg"), 1.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("90 tg")
    
    def test_asin(self):
        self.assertAlmostEqual(self.calc.evaluar("0 asin"), 0.0)
        self.assertAlmostEqual(self.calc.evaluar("0.5 asin"), 30.0)
        self.assertAlmostEqual(self.calc.evaluar("1 asin"), 90.0)
        
        with self.assertRaises(ErrorDominioMatematico):
            self.calc.evaluar("2 asin")
    
    def test_acos(self):
        self.assertAlmostEqual(self.calc.evaluar("1 acos"), 0.0)
        self.assertAlmostEqual(self.calc.evaluar("0.5 acos"), 60.0)
        self.assertAlmostEqual(self.calc.evaluar("0 acos"), 90.0)
    
    def test_atg_atan(self):
        self.assertAlmostEqual(self.calc.evaluar("0 atg"), 0.0)
        self.assertAlmostEqual(self.calc.evaluar("1 atg"), 45.0)
    
    def test_identidades_trigonometricas(self):
        resultado = self.calc.evaluar("30 sin 2 pow 30 cos 2 pow +")
        self.assertAlmostEqual(resultado, 1.0)


class TestMemorias(unittest.TestCase):
    """Pruebas del sistema de memorias STO/RCL."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_sto_rcl_basico(self):
        self.assertEqual(self.calc.evaluar("5 sto 00 2 * rcl 00 +"), 15)
        self.calc.evaluar("42 sto 01")
        self.assertEqual(self.calc.evaluar("rcl 01"), 42)
    
    def test_sto_no_consume_pila(self):
        self.assertEqual(self.calc.evaluar("7 sto 03 2 *"), 14)
    
    def test_multiples_memorias(self):
        self.assertEqual(self.calc.evaluar("3 sto 00"), 3)
        self.assertEqual(self.calc.evaluar("4 sto 01"), 4)
        self.assertEqual(self.calc.evaluar("rcl 00"), 3)
        self.assertEqual(self.calc.evaluar("rcl 01"), 4)
        resultado = self.calc.evaluar("rcl 00 rcl 01 *")
        self.assertEqual(resultado, 12)
    
    def test_error_sto_pila_vacia(self):
        with self.assertRaises(PilaInsuficienteError):
            self.calc.evaluar("sto 00")
    
    def test_error_rcl_memoria_vacia(self):
        """RCL de memoria no inicializada devuelve 0.0 (valor por defecto)."""
        self.assertEqual(self.calc.evaluar("rcl 05"), 0.0)
    
    def test_error_indice_invalido(self):
        with self.assertRaises(ErrorIndiceMemoria):
            self.calc.evaluar("5 sto 10")
        with self.assertRaises(ErrorIndiceMemoria):
            self.calc.evaluar("5 sto abc")
    
    def test_error_sto_rcl_sin_indice(self):
        with self.assertRaises((TokenInvalidoError, ErrorIndiceMemoria)):
            self.calc.evaluar("sto")
        with self.assertRaises((TokenInvalidoError, ErrorIndiceMemoria)):
            self.calc.evaluar("rcl")


class TestCasosIntegracion(unittest.TestCase):
    """Pruebas de integración complejas."""
    
    def setUp(self):
        self.calc = CalculadoraRPN()
    
    def test_calculo_compuesto_1(self):
        resultado = self.calc.evaluar("3 4 + 5 2 - *")
        self.assertEqual(resultado, 21)
    
    def test_calculo_compuesto_2(self):
        resultado = self.calc.evaluar("30 sin e *")
        self.assertAlmostEqual(resultado, 0.5 * math.e)
    
    def test_calculo_compuesto_3(self):
        self.calc.evaluar("p sto 00")
        self.assertAlmostEqual(self.calc.evaluar("90 sin"), 1.0)
        self.assertAlmostEqual(self.calc.evaluar("rcl 00"), math.pi)
    
    def test_ecuacion_cuadratica(self):
        resultado = self.calc.evaluar("2 dup * 5 2 * - 6 +")
        self.assertEqual(resultado, 0)
    
    def test_area_circulo(self):
        resultado = self.calc.evaluar("5 dup * p *")
        self.assertAlmostEqual(resultado, 25 * math.pi)


# ==============================================================================
#  EJECUCIÓN DE PRUEBAS
# ==============================================================================

if __name__ == '__main__':
    unittest.main(verbosity=2)