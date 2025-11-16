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
                'DesagregadoDesembolsoBIE','OcupacionEconomica','Posee Censo de Familia?'], inplace=True)

#Cambiar Nombres de los encabezados de las Columnas y asignación de los nombbres de las variables

df.rename (columns={"Tipo de Desmovilización": "tipo_desmovilizacion"}, inplace=True) 
print(df.columns)

df.rename (columns={"Ex Grupo": "grupoArmado"}, inplace=True)
print(df.columns)

df.rename (columns={"Año desmovilización": "anoDesmov"}, inplace=True) 
print(df.columns)

df.rename (columns={"Sexo": "sexo"}, inplace=True) 
print(df.columns)

df.rename (columns={"Situación Final frente al proceso": "estadoProceso"}, inplace=True) 
print(df.columns)

df.rename (columns={"Régimen de salud": "eps"}, inplace=True) 
print(df.columns)

df.rename (columns={"Posee Serv. Públicos Básicos": "servPublicos"}, inplace=True) 
print(df.columns)

df.rename (columns={"Departamento de residencia descripción": "departamento"}, inplace=True)
print(df.columns)

df.rename (columns={"Desembolso BIE": "subsidiado"}, inplace=True) 
print(df.columns)

df.rename (columns={"Total Integrantes grupo familiar": "integrantesFamilia"}, inplace=True)
print(df.columns)

df.rename (columns={"Posee Censo de Habitabilidad?": "censoVivienda"}, inplace=True) 
print(df.columns)


df.rename (columns={"Ingresó/No ingresó": "ingresoSub"}, inplace=True) 
print(df.columns)

df.rename (columns={"Año de Independización/Ingreso": "anoIngreso"}, inplace=True) 
print(df.columns)

df.rename (columns={"Departamento de residencia": "codigoDepartamento"}, inplace=True) 
print(df.columns)

df.rename (columns={"Nivel Educativo": "nivelEducativo"}, inplace=True) 
print(df.columns)
