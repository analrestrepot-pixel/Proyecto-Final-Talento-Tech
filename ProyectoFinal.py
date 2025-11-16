



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. Importación de archivos y fuentes de datos. Secargó la base de datos

df= pd.read_csv("Yanacona.csv")
print(df)

# 2. Exploración Inicial
#primeras 5 filas

print(df.head())

#ultimas 5 filas
print(df.tail())

#dimensiones del data set
print(df.shape)

#nombre de las columnas
print(df.columns)

#tipo de datos y valores nulos
print(df.info())

#estadistica basica
print(df.describe())

# Estadísticas para columnas categóricas (tipo object o string)
print("Estadísticas de variables categóricas:")
print(df.describe(include='object'))

# Conteo de filas duplicadas
print("Número de filas duplicadas:")
print(df.duplicated().sum())

# Ver primeras filas duplicadas si existen
print("Filas duplicadas (si existen):")
print(df[df.duplicated()].head())

# Si quieres ver la correlación entre variables numéricas:
print("Correlación entre variables numéricas:")
print(df.corr(numeric_only=True))


