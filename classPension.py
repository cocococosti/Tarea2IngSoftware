'''
Creado el 10 oct. 2018

@author: Constanza Abarca 13-10000
@author: Pedro Maldona 13-10790

'''

import datetime
from _datetime import date

class Pension():
    
    def calcularSemanas(self, dia, mes, anio):
        # Obtener fecha hoy
        hoy = datetime.date.today()
        fechaTrabajo = datetime.date(anio, mes, dia)
        dias = (hoy-fechaTrabajo).days
        semanas = dias/7
        return round(semanas)
    
    def esPensionado (self, genero, dia, mes, anio, edad, cond):
        
        if (isinstance(dia, float) or isinstance(mes, float) or isinstance(anio, float) or isinstance(edad, float)):
            raise ValueError("Error. No pueden ser numeros decimales")
        if (dia <= 0 or mes <= 0 or anio <= 0 or edad <= 0):
            raise ValueError("Error. No pueden ser numeros negativos o cero")
        if (dia > 31 or mes > 12 or anio > 2018):
            raise ValueError("Error. Valores invalidos para una fecha.")
        if (genero != "M" and genero != "F"):
            raise ValueError("Error. El genero solo puede ser M o F.")
        if ((datetime.date.today()-datetime.date(anio, mes, dia)).days<0):
            raise Exception("Error. La fecha no puede ser futura.")
        
        mayorEdad = datetime.date.today().year - edad + 18
        if (anio < mayorEdad):
            raise Exception("Error. La fecha inicio de trabajo debe ser posterior a haber cumplido 18 años.")
            
        
        semanas = self.calcularSemanas(dia, mes, anio)
        
        if (cond == True):
            if (semanas >= 48 and semanas < 96):
                edad = edad + 1
            elif (semanas >= 95 and semanas < 144):
                edad = edad + 2
            elif (semanas >= 144 and semanas < 192):
                edad = edad + 3
            elif (semanas >= 192 and semanas < 240):
                edad = edad + 5
            elif (semanas >= 240):
                edad = edad + 5
            else:
                pass        
        
        
        
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



    