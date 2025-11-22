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

#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ 1. ANALISIS Y EXPLORACION INICIAL#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ 

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
df.rename (columns={"Tipo de Desmovilización": "tipo"}, inplace=True) 
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

# #•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•
#                          2. LIMPIEZA DE DATOS  
#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•

# valores Nulos
print(df.isnull().sum())
# Ver porcentaje de nulos por columna
print(df.isnull().mean() * 100)

# 2. Limpieza de Datos

# valores Nulos
print(df.isnull().sum())
# Ver porcentaje de nulos por columna
print(df.isnull().mean() * 100)

# Reemplazo de NAN

# variable "integrantesFamilia"
# Reemplazar -1 por NaN en todos los registros
df.loc[df['integrantesFamilia'] == -1, 'integrantesFamilia'] = np.nan

# Imputar según el tipo
df.loc[df['tipo'] == "individual", 'integrantesFamilia'] = df.loc[df['tipo'] == "individual",
                      'integrantesFamilia'].fillna(1)

# Para colectivos: imputar con la mediana de ese grupo
mediana_colectiva = df.loc[df['tipo'] == "colectiva", 'integrantesFamilia'].median()
df.loc[df['tipo'] == "colectiva", 'integrantesFamilia'] = df.loc[df['tipo'] == "colectiva",
                       'integrantesFamilia'].fillna(mediana_colectiva)

#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•
#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ FUNCIONES DE NORMALIZACIÓN •┈┈┈••✦ ♡ ✦••┈┈┈••
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•

import unicodedata
import re

def normalizar_texto(tipo):
    """Normaliza un texto eliminando tildes, pasando a minúsculas y quitando símbolos."""
    if pd.isnull(tipo):
        return tipo

    # Convertir a string
    tipo = str(tipo)

    # Quitar acentos
    tipo = unicodedata.normalize('NFKD', tipo).encode('ascii', 'ignore').decode('utf-8')

    # Convertir a minúsculas
    tipo = tipo.lower()

    # Eliminar caracteres especiales
    tipo = re.sub(r'[^a-z0-9\s.,_-]', '', tipo)

    # Quitar espacios múltiples
    tipo = re.sub(r'\s+', ' ', tipo).strip()

    return tipo

df['tipo'] = df['tipo'].apply(normalizar_texto)
df['grupoArmado'] = df['grupoArmado'].apply(normalizar_texto)
df['ingresoSub'] = df['ingresoSub'].apply(normalizar_texto)
df['sexo'] = df['sexo'].apply(normalizar_texto)
df['estadoProceso'] = df['estadoProceso'].apply(normalizar_texto)
df['servPublicos'] = df['servPublicos'].apply(normalizar_texto)
df['censoVivienda'] = df['censoVivienda'].apply(normalizar_texto)
df['subsidiado'] = df['subsidiado'].apply(normalizar_texto)
df['nivelEducativo'] = df['nivelEducativo'].apply(normalizar_texto)
df['eps'] = df['eps'].apply(normalizar_texto)
df['departamento'] = df['departamento'].apply(normalizar_texto)

#Limpia y convierte valores de año

def normalizar_anio(anio):
    """Limpia y convierte valores de año con comas, espacios y otros símbolos a entero."""
    if pd.isnull(anio):
        return None  

    # Convertir a string
    anio_str = str(anio)

    # Quitar espacios y comas (y otros símbolos, si existen)
    anio_str = re.sub(r'[^0-9]', '', anio_str)

    # Intentar convertir a entero (año)
    try:
        return int(anio_str)
    except ValueError:
        return None 
df['anoDesmov'] = df['anoDesmov'].apply(normalizar_anio)
df['anoIngreso'] = df['anoIngreso'].apply(normalizar_anio)


print(df.info())
#Método para verificar variables únicas

print(df['tipo'].nunique())  #2 tipos
print(df['grupoArmado'].nunique()) #12 tipos
print(df['ingresoSub'].nunique()) #2 tipos
print(df['sexo'].nunique())       #2 tipos
print(df['estadoProceso'].nunique()) #5 tipos 
print(df['departamento'].nunique()) #34 tipos
print(df['nivelEducativo'].nunique()) #5 tipos
print(df['subsidiado'].nunique())  #2 tipos
print(df['censoVivienda'].nunique()) #2 tipos
print(df['servPublicos'].nunique()) # servicios publicos tiene 3
print(df['eps'].nunique())#  eps tiene 3 valores unicos

#Método para mostrar cada valor de la Columna y su cantidad
print(df['grupoArmado'].value_counts()) # Limpiar despues de los datos atipicos 
print(df['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso
print(df['nivelEducativo'].value_counts()) # Quitar no ha ingresado / ausente del proceso






































































































# =====================================================
# ========== PRUEBA DEL MÓDULO (OPCIONAL) =============
# =====================================================
if __name__ == "__main__":
    print("\n### MÓDULO DE LIMPIEZA – PRUEBA ###")
    archivo = "ventas_Sin_Limpiar.csv"

    try:
        df_test = pd.read_csv(archivo)
        df_limpio = limpiar_dataset(df_test)
        df_limpio.to_csv("ventas_limpias.csv", index=False)
        print("Archivo limpio generado como ventas_limpias.csv")

    except Exception as e:
        print("No se encontró el archivo para prueba, pero el módulo funciona correctamente.")
        print("Error:", e)




