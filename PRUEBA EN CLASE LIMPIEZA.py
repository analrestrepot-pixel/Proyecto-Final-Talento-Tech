# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 09:43:06 2025

@author: silva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importar archivos

df = pd.read_csv("desmovilizados.csv")  # Leer archivo CSV local

# Eliminamos columnas no útiles para análisis inicial

df.drop(columns=['Grupo Etario', 'FechaCorte', 'FechaActualizacion',
                 'Clasificación Componente Específico','Régimen de tenencia Vivienda',
                 'Municipio de residencia descripción','BeneficioFA',
                 'BeneficioTRV', 'BeneficioFPT','BeneficioPDT',
                 'Municipio de residencia','Tipo de Vivienda', 
                 'Tipo de ASS Vinculada','Posee Servicio Social?',
                 'Posee Cónyuge o Compañero(a)?','Máximo Nivel FpT Reportado',
                 'Línea de FpT para el Máx. Nivel','N° de Hijos','Estado ISUN',
                'Estado de la vinculación ASS','Tipo de BIE Accedido',
                'DesagregadoDesembolsoBIE','OcupacionEconomica'], inplace=True)
#Cambiar Nombres

df.rename (columns={"Tipo de Desmovilización": "tipo_desmovilizacion"}, inplace=True) # se cambia Fare por tarifa
print(df.columns)

df.rename (columns={"Ex Grupo": "grupoArmado"}, inplace=True) # se EX grupo por Grupo Armado
print(df.columns)

df.rename (columns={"Año desmovilización": "anoDesmov"}, inplace=True) # se EX grupo por Grupo Armado
print(df.columns)

df.rename (columns={"Año desmovilización": "anoDesmov"}, inplace=True) # se EX grupo por Grupo Armado
print(df.columns)










