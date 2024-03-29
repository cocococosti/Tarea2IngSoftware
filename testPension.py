'''
Creado el 10 oct. 2018

@author: Constanza Abarca 13-10000
@author: Pedro Maldona 13-10790


'''

from classPension import *
import unittest



class testPension(unittest.TestCase):
    
    def setUp(self):
        self.pension = Pension()
#    Prueba 0
    def testCalculoSemanas(self):
        self.assertEqual(self.pension.calcularSemanas(5, 4, 1990), 1488, "Se deben obtener 1488 semanas.")
#    Prueba 1  
    def testEdadAceptadaHombre(self):
        self.assertTrue(self.pension.esPensionado("M", 10, 10, 1997, 65, False), "La persona cumple con los requisitos para el pago de pension")
#    Prueba 2
    def testEdadAceptadaMujer(self):
        self.assertTrue(self.pension.esPensionado("F", 10, 10, 1997, 60, False), "La persona cumple con los requisitos para el pago de pension")
#    Prueba 3
    def testEdadNoAceptadaHombre(self):
        self.assertFalse(self.pension.esPensionado("M", 10, 10, 1997, 50, False), "La persona no cumple con los requisitos para el pago de pension")
#    Prueba 4
    def testEdadNoAceptadaMujer(self):
        self.assertFalse(self.pension.esPensionado("F", 10, 10, 1997, 45, False), "La persona no cumple con los requisitos para el pago de pension")
#    Prueba 5
    def testSemanasIncompletasHombre(self):
        self.assertFalse(self.pension.esPensionado("M", 10, 10, 2005, 65, False), "La persona no cumple con los requisitos para el pago de pension")
#    Prueba 6
    def testSemanasIncompletasMujer(self):
        self.assertFalse(self.pension.esPensionado("F", 10, 10, 2005, 60, False), "La persona no cumple con los requisitos para el pago de pension")

#    Prueba 7
    def testTrabajoInsalubre(self):
        self.assertTrue(self.pension.esPensionado("F", 5, 5, 1995, 60, True), "La persona cumple con los requisitos para el pago de pension")
#    Prueba 8
    def testTrabajoInsalubreAceptadoMujer(self):
        self.assertTrue(self.pension.esPensionado("F", 5, 5, 1995, 53, True), "La persona cumple con los requisitos para el pago de pension")
#    Prueba 9
    def testTrabajoInsalubreAceptadoHombre(self):
        self.assertTrue(self.pension.esPensionado("M", 5, 5, 1995, 57, True), "La persona cumple con los requisitos para el pago de pension")
#    Prueba 10
    def testTrabajoInsalubreAceptadoHombreFrontera(self):
        self.assertTrue(self.pension.esPensionado("M", 5, 5, 1995, 59, True), "La persona cumple con los requisitos para el pago de pension")
#   Prueba 11
    def testTrabajoInsalubreNoAceptadoHombre(self):
        self.assertFalse(self.pension.esPensionado("M", 5, 5, 2016, 59, True), "La persona no cumple con los requisitos para el pago de pension")
#   Prueba 12
    def testTrabajoInsalubreAceptadoMujerFrontera(self):
        self.assertTrue(self.pension.esPensionado("F", 5, 5, 1995, 54, True), "La persona cumple con los requisitos para el pago de pension")
#   Prueba 13
    def testTrabajoInsalubreNoAceptadoMujer(self):
        self.assertFalse(self.pension.esPensionado("F", 5, 5, 2016, 54, True), "La persona no cumple con los requisitos para el pago de pension")
#    Prueba 14
    def testFechaTrabajoHoy(self):
        hoy = datetime.date.today()
        self.assertFalse(self.pension.esPensionado("F", hoy.day, hoy.month, hoy.year, 60, False),"La persona no cumple con los requisitos para el pago de pension")
#    Prueba 15
    def testNingunValorCumpleReq(self):
        self.assertFalse(self.pension.esPensionado("F", 2, 5, 2017, 30, False), "La persona no cumple con los requisitos para el pago de pension")
#    Prueba 16
    def testDecimales(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 2.5, 5, 2017, 30, False)
#    Prueba 17
    def testNegativos(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 2, 5, 2017, -30, False)
#    Prueba 18
    def testCero(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 0, 5, 2017, 30, False)
#    Prueba 19
    def testValorDia(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 32, 5, 2017, 30, False)
#    Prueba 20
    def testValorMes(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 4, 17, 2017, 30, False)
#    Prueba 21
    def testValorAnio(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "F", 3, 5, 2020, 30, False)
#    Prueba 22
    def testValorGenero(self):
        self.assertRaises(ValueError, self.pension.esPensionado, "G", 3, 5, 2018, 30, False)
#    Prueba 23
    def testFechaFuturo(self):
        hoy = datetime.date.today()+datetime.timedelta(days=1)
        self.assertRaises(Exception, self.pension.esPensionado, "F", hoy.day, hoy.month, hoy.year, 60, False)
#    Prueba 24
    def testFechaMayorEdad(self):
        self.assertRaises(Exception, self.pension.esPensionado, "F", 6, 5, 1970, 55, False)
                        