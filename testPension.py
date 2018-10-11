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
        
    def testCalcularSemanas(self):
        self.assertEqual(self.pension.calcularSemanas(5, 4, 1990), 1488, "Se deben obtener 1488 semanas.")

    