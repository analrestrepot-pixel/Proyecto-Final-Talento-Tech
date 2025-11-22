# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 15:17:31 2025

@author: silva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unicodedata
import re

#Importar archivos

df1 = pd.read_csv("desmovilizados.csv")  # Leer archivo CSV local

# ===================================== 1. ANALISIS Y EXPLORACION INICIAL =====================

# Eliminamos columnas no útiles para análisis inicial
df1.drop(columns=['Grupo Etario', 'FechaCorte', 'FechaActualizacion',
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
df1.rename (columns={"Tipo de Desmovilización": "tipo"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Ex Grupo": "grupoArmado"}, inplace=True)
print(df1.columns)

df1.rename (columns={"Año desmovilización": "anoDesmov"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Sexo": "sexo"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Situación Final frente al proceso": "estadoProceso"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Régimen de salud": "eps"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Posee Serv. Públicos Básicos": "servPublicos"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Departamento de residencia descripción": "departamento"}, inplace=True)
print(df1.columns)

df1.rename (columns={"Desembolso BIE": "subsidiado"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Total Integrantes grupo familiar": "integrantesFamilia"}, inplace=True)
print(df1.columns)

df1.rename (columns={"Posee Censo de Habitabilidad?": "censoVivienda"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Ingresó/No ingresó": "ingresoSub"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Año de Independización/Ingreso": "anoIngreso"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Departamento de residencia": "codigoDepartamento"}, inplace=True) 
print(df1.columns)

df1.rename (columns={"Nivel Educativo": "nivelEducativo"}, inplace=True) 
print(df1.columns)

# 2. Limpieza de Datos

# valores Nulos
print(df1.isnull().sum())
# Ver porcentaje de nulos por columna
print(df1.isnull().mean() * 100)

#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•
#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ FUNCIONES DE NORMALIZACIÓN •┈┈┈••✦ ♡ ✦••┈┈┈••
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•



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

df1['tipo'] = df1['tipo'].apply(normalizar_texto)
df1['grupoArmado'] = df1['grupoArmado'].apply(normalizar_texto)
df1['ingresoSub'] = df1['ingresoSub'].apply(normalizar_texto)
df1['sexo'] = df1['sexo'].apply(normalizar_texto)
df1['estadoProceso'] = df1['estadoProceso'].apply(normalizar_texto)
df1['servPublicos'] = df1['servPublicos'].apply(normalizar_texto)
df1['censoVivienda'] = df1['censoVivienda'].apply(normalizar_texto)
df1['subsidiado'] = df1['subsidiado'].apply(normalizar_texto)
df1['nivelEducativo'] = df1['nivelEducativo'].apply(normalizar_texto)
df1['eps'] = df1['eps'].apply(normalizar_texto)
df1['departamento'] = df1['departamento'].apply(normalizar_texto)

print(df1.info())

#Método para verificar variables únicas

print(df1['tipo'].nunique())  #2 tipos
print(df1['grupoArmado'].nunique()) #12 tipos
print(df1['ingresoSub'].nunique()) #2 tipos
print(df1['sexo'].nunique())       #2 tipos
print(df1['estadoProceso'].nunique()) #5 tipos 
print(df1['departamento'].nunique()) #34 tipos
print(df1['nivelEducativo'].nunique()) #5 tipos
print(df1['subsidiado'].nunique())  #2 tipos
print(df1['censoVivienda'].nunique()) #2 tipos
print(df1['servPublicos'].nunique()) # servicios publicos tiene 3
print(df1['eps'].nunique())#  eps tiene 3 valores unicos

#Método para mostrar cada valor de la Columna y su cantidad
print(df1['grupoArmado'].value_counts()) # Limpiar despues de los datos atipicos 
print(df1['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso
print(df1['nivelEducativo'].value_counts()) # Quitar no ha ingresado / ausente del proceso

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
df1['anoDesmov'] = df1['anoDesmov'].apply(normalizar_anio)
df1['anoIngreso'] = df1['anoIngreso'].apply(normalizar_anio)


#•┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•1. LIBRERÍAS •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈•

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
#import category_encoders as ce

plt.style.use("ggplot")


# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈
# 2. CARGA DE DATOS
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈

# Selección de columnas relevantes
df1 = df1[["tipo","grupoArmado","anoDesmov","ingresoSub","anoIngreso","sexo","estadoProceso",
           "departamento","codigoDepartamento","nivelEducativo","subsidiado","integrantesFamilia",
           "censoVivienda","servPublicos","eps"]]

print("\n==== INFORMACIÓN ORIGINAL ====")
print(df1.info())
print(df1.head())


# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈
# 5. ELIMINACIÓN DE OUTLIERS – IQR PARA NÚMEROS 
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈

##Visualizar datos atipicos y gráfica de frecuencias en números en la variable "anoDesmov"

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df1["anoDesmov"],palette=["#DB7093"])
plt.title("Boxplot año de desplazamiento.")
plt.tight_layout()
plt.show()

print(df1['anoDesmov'].value_counts()) # Limpiar despues de los datos atipicos (quitar valores menores a 200)

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df1 = remove_outliers_iqr(df1, "anoDesmov")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df1["anoDesmov"],palette = ["#FA8072"])
plt.title("Boxplot Año de desplazamiento (sin outliers)")
plt.tight_layout()
plt.show()

print("\nTamaño original:", df1.shape)
print("Tamaño sin outliers:", df1.shape)

#Visualizar datos atipicos y gráfica de frecuencias en números en la variable "anoIngreso"

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df1["anoIngreso"],palette=["#DB7093"])
plt.title("Boxplot año de ingreso al programa.")
plt.tight_layout()
plt.show()

print(df1['anoIngreso'].value_counts()) # Limpiar despues de los datos atipicos (quitar valores menores a 200)

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df1 = remove_outliers_iqr(df1, "anoIngreso")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df1["anoIngreso"],palette = ["#F08080"])
plt.title("Boxplot Año de ingreso al programa (sin outliers)")
plt.tight_layout()
plt.show()

print("\nTamaño original:", df1.shape)
print("Tamaño sin outliers:", df1.shape)

# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈
# 5. ELIMINACIÓN DE OUTLIERS – IQR PARA TEXTO 
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈

#Revisión de cantidad de tipos por columna para hacer su respectiva limpieza

print(df1['grupoArmado'].value_counts()) # Limpiar despues de los datos atipicos (quitar valores menores a 200)
print(df1['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso
print(df1['nivelEducativo'].value_counts()) # Quitar por establecer / alfabetizacion

#Funcion para eliminar valores atipicos de tipo string con cantidades menores a 146
def remove_outliers_str(df, column, min_count=146):
    counts = df[column].value_counts()
    valid_categories = counts[counts > min_count].index
    return df[df[column].isin(valid_categories)]

df1 = remove_outliers_str(df1, "grupoArmado", min_count=146)
print(df1['grupoArmado'].value_counts()) # Limpiar despues de los datos atipicos


print(df1['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso
df1 = df1[df1['estadoProceso'] != 'ausente del proceso']
print(df1['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso

print(df1['grupoArmado'].value_counts()) # Limpiar despues de los datos atipicos (quitar valores menores a 200)
print(df1['estadoProceso'].value_counts()) # Quitar no ha ingresado / ausente del proceso
print(df1['nivelEducativo'].value_counts()) # Quitar por establecer / alfabetizacion

#Visualización sin Outliers IQR para textos.

#Grupo Armado
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df1["grupoArmado"], palette=["#FFB6C1"])
plt.title("Grupo Armado")
plt.show()

plt.figure(figsize=(12, 5))


#Estado Proceso

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df1["estadoProceso"], palette=["#DDA0DD"])
plt.title("Estado Proceso")
plt.show()

#Nivel Educativo

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df1["nivelEducativo"], palette=["#FF1493"])
plt.title("Nivel Educativo")
plt.show()

# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈
# lIMPIEZA DE DATOS(FALTANTE)
# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈

# Reemplazo de NAN
# variable "integrantesFamilia"
# Reemplazar -1 por NaN en todos los registros
df1.loc[df1['integrantesFamilia'] == -1, 'integrantesFamilia'] = np.nan

# Imputar según el tipo
df1.loc[df1['tipo'] == "individual", 'integrantesFamilia'] = df1.loc[df1['tipo'] == "individual",
                                                                     'integrantesFamilia'].fillna(1)
# Para colectivos: imputar con la mediana de ese grupo
mediana_colectiva = df1.loc[df1['tipo'] == "colectiva", 'integrantesFamilia'].median()
df1.loc[df1['tipo'] == "colectiva", 'integrantesFamilia'] = df1.loc[df1['tipo'] == "colectiva",
                       'integrantesFamilia'].fillna(mediana_colectiva)

#Remplazo de palabras por su respectiva inicial

df1['eps'] = df1['eps'].str.replace('subsidiado', '', regex=False).str.strip()
df1['eps'] = df1['eps'].str.replace('contributivo', '', regex=False).str.strip()

df1['eps'] = df1['eps'].replace('no registra', 'n')

print(df1['eps'].value_counts()) 

df1['eps'] = df1['eps'].str.replace(' -', '', regex=False).str.strip()

#Exprtar dataframe limpio sin codificar.
df1.to_csv("desmovilizados.csv",index=True)





#  •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈ •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈
# 6. CODIFICACIÓN DE VARIABLES CATEGÓRICAS
# # •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈# •┈┈┈••✦ ♡ ✦••┈┈┈••┈┈┈••✦ ♡ ✦••┈┈┈

data = df1.copy()

# One-Hot Encoder

ohe = OneHotEncoder(sparse_output=False, drop="first")
ohe_cols = ohe.fit_transform(data[["sexo"]])
data["sexo"] = ohe_cols

# Label Encoder
le = LabelEncoder()
data["tipo"] = le.fit_transform(data["tipo"])














# Label Encoder
le = LabelEncoder()
data["Sex_label"] = le.fit_transform(data["Sex"])
data["Embarked_label"] = le.fit_transform(data["Embarked"].astype(str))

# One-Hot Encoding
ohe = OneHotEncoder(sparse_output=False, drop="first")
ohe_cols = ohe.fit_transform(data[["Sex"]])
data["Sex_ohe"] = ohe_cols

# Ordinal Encoder
ord_encoder = OrdinalEncoder(categories=[["male", "female"]])
data["Sex_ordinal"] = ord_encoder.fit_transform(data[["Sex"]])

# Frequency Encoder
freq_encoder = data["Sex"].value_counts(normalize=True)
data["Sex_freq"] = data["Sex"].map(freq_encoder)

# Target Encoder
target_encoder = ce.TargetEncoder(cols=["Sex"])
data["Sex_target"] = target_encoder.fit_transform(data["Sex"], data["Survived"])

# Binary Encoder
bin_encoder = ce.BinaryEncoder(cols=["Sex"])
bin_out = bin_encoder.fit_transform(data[["Sex"]])
data = pd.concat([data, bin_out], axis=1)

print("\n==== DATOS CODIFICADOS ====")
print(data.head())

# ==================================================
# 7. SELECCIÓN DE CARACTERÍSTICAS
# ==================================================
data_sel = df_no_outliers.copy()
data_sel["Sex_label"] = le.fit_transform(data_sel["Sex"])
data_sel["Embarked_label"] = le.fit_transform(data_sel["Embarked"].astype(str))

X = data_sel[["Age", "Fare", "Pclass", "Sex_label", "Embarked_label"]]
y = data_sel["Survived"]

# Varianza
selector = VarianceThreshold(threshold=0.5)
_ = selector.fit_transform(X)
features_var = X.columns[selector.get_support()]
print("\nVariables con varianza aceptada:", list(features_var))

# Correlación
xy = X.copy()
xy["Survived"] = y

correlacion = xy.corr()["Survived"].abs().sort_values(ascending=False)
relevant_features = correlacion[correlacion > 0.15].index.tolist()
relevant_features.remove("Survived")

print("\nVariables con correlación > 0.15:", relevant_features)

sns.heatmap(xy[relevant_features + ["Survived"]].corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()




