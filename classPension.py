'''
Creado el 10 oct. 2018

@author: Constanza Abarca 13-10000
@author: Pedro Maldona 13-10790

'''

import datetime

class Pension():
    
    def calcularSemanas(self, dia, mes, anio):
        hoy = datetime.date.today()
        fechaTrabajo = datetime.date(anio, mes, dia)
        dias = (hoy-fechaTrabajo).days
        semanas = dias/7
        return round(semanas)
    
    def esPensionado (self, genero, dia, mes, anio, edad, cond):
        
        semanas = self.calcularSemanas(dia, mes, anio)
        
        if (genero == "M"):
            if (edad < 60):
                return False 
        elif (genero == "F"):
            if (edad < 55):
                return False
        if (semanas > 750):
            return True
        else:
            return False