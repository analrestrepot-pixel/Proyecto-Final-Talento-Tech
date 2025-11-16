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

#▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰  3. Limpieza de Datos ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
# valores Nulos
print(df.isnull().sum())

# Ver porcentaje de nulos por columna
print(df.isnull().mean() * 100)

# Eliminamos columnas no útiles para análisis inicial
df.drop(columns=['CC', 'NUMERO DOCUMENTO', 'TELEFONO'], inplace=True)


# Se convirtio columna sexo de tipo object a category
df['SEXO']=df ['SEXO'].astype('category')
print(df.info())

moda = df['DESPLAZ'].mode()
df['DESPLAZ']= df['DESPLAZ'].str.upper()
df.loc[df['DESPLAZ'] == 'P', 'DESPLAZ'] = moda
# Eliminamos columnas no útiles para análisis inicial
df.drop(columns=['columna'], inplace=True)

# Imputación de valores nulos en variables seleccionadas
# 'Age': usamos la mediana porque es robusta ante outliers
df['DESPLAZ']=df ['DESPLAZ'].astype('category')

#'Embarked': usamos la moda (valor más frecuente) para conservar la categoría dominante
df['DESPLAZ'].fillna(df['DESPLAZ'].mode()[0], inplace=True)  # Moda para Embarque
print(df.isnull().sum())
df['DESPLAZ'].mode()


print(df.info())
