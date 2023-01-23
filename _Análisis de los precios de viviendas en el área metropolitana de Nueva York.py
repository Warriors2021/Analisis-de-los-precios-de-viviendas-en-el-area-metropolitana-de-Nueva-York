#!/usr/bin/env python
# coding: utf-8

# <h1> Análisis de los precios de viviendas en el área metropolitana de Nueva York </h1>

# <h3>Descripción:</h3>
# <la>Utilizar técnicas de análisis de datos para investigar los precios de viviendas en el área metropolitana de Nueva York. El objetivo es obtener los cinco (5) promedios de venta mas altos y los cinco (5) promedios de venta mas bajos.</la>
# 
# <h3>Pasos:</h3>
# 
# <li>Descargar los datos de la fuente Zillow Research (https://www.zillow.com/research/data/)</li>
# <li>Limpieza y preparación de los datos</li>
# <li>Análisis exploratorio de los datos</li>
# <li>Creación de gráficos y visualizaciones para presentar los hallazgos</li>
# <li>Identificar promedios en los precios de las viviendas</li>
# <li>Crear un informe de conclusiones y recomendaciones para inversionistas inmobiliarios.</li>
# <li>Herramientas y tecnologías utilizadas: Python, Pandas, Matplotlib, Jupyter notebook</li>

# <h4>Este segmento de código importa dos librerías importantes para el análisis de datos y la visualización de gráficos en Python: pandas y matplotlib. Pandas es una librería de código abierto que proporciona estructuras de datos y herramientas de análisis de datos fáciles de usar, mientras que matplotlib es una librería de código abierto que se utiliza para crear gráficos estáticos, animaciones y visualizaciones en 2D y 3D en Python. Estas librerías son ampliamente utilizadas en el análisis de datos y la visualización de gráficos en Python.</h4>

# In[1]:


# importamos la librería pandas
import pandas as pd

# importamos la librería matplotlib
import matplotlib.pyplot as plt


# <h4>Este segmento de código utiliza el paquete pandas para leer un archivo CSV (Comma Separated Values) y guardarlo en un DataFrame llamado 'df'. El método 'pd.read_csv' se utiliza para leer un archivo CSV y convertirlo en un DataFrame. El nombre del archivo se pasa como un argumento al método 'pd.read_csv', en este caso el nombre del archivo es "Datos.csv".</h4>
# 
# <h4>Una vez que el archivo se ha leído y convertido en un DataFrame, se imprime el DataFrame 'df' para verificar que los datos se hayan cargado correctamente.</h4>

# In[2]:


# utilizamos el método 'pd.read_csv' para leer un archivo CSV y guardarlo en un DataFrame 'df'
df = pd.read_csv("Datos.csv")

# imprimimos el DataFrame 'df' para verificar que los datos se hayan cargado correctamente
df


# <h4>Este segmento de código utiliza el DataFrame 'df' para generar un resumen estadístico y mostrar información sobre la cantidad de valores no nulos y la cantidad de valores nulos en cada columna del DataFrame 'df'.</h4>

# In[3]:


# generamos un resumen estadístico del DataFrame 'df' y lo guardamos en un nuevo DataFrame 'df1'
df1 = df.describe()

# seleccionamos la fila "count" del DataFrame 'df1' y la imprimimos
print(df1.loc["count",:])

# detectamos los valores nulos en el DataFrame 'df' y contamos cuántos hay en cada columna
# el resultado se imprime
print(df.isnull().sum())


# <h4>Este segmento de código recorre cada fila del DataFrame 'df' y reemplaza los valores nulos con el promedio de esa fila.</h4>

# In[4]:


# recorremos cada fila del DataFrame 'df'
for x in range(len(df)):
    # calculamos el promedio de cada fila utilizando el método 'loc' para seleccionar todas las columnas desde "2000-01-31" hasta el final 
    # y el método 'mean()' para calcular el promedio
    mean_row = df.loc[x, "2000-01-31":].mean()    
    # reemplazamos los valores nulos de la fila con el promedio calculado anteriormente
    df.loc[x, :] = df.loc[x, :].fillna(mean_row)


# <h4>Este segmento de código utiliza el DataFrame 'df' para generar un resumen estadístico y mostrar información sobre la cantidad de valores no nulos y la cantidad de valores nulos en cada columna del DataFrame 'df' y verificar si se ajustaron.</h4>

# In[5]:


# generamos un resumen estadístico del DataFrame 'df' y lo guardamos en un nuevo DataFrame 'df1'
df1 = df.describe()

# seleccionamos la fila "count" del DataFrame 'df1' y la imprimimos
print(df1.loc["count",:])

# detectamos los valores nulos en el DataFrame 'df' y contamos cuántos hay en cada columna
# el resultado se imprime
print(df.isnull().sum())


# <h4>Este  segmento de código utiliza el DataFrame 'df' para calcular el promedio de los precios de las viviendas para cada región, crear un nuevo DataFrame con esos valores y ordenarlo en orden descendiente para seleccionar las 5 regiones con el promedio más alto.</h4>

# In[6]:


# seleccionamos la columna "RegionName" del DataFrame 'df' y la almacenamos en una lista
Region_name = list(df.loc[:,"RegionName"])

# creamos una lista vacía para almacenar los promedios de los precios de las viviendas
means = []

# recorremos cada fila del DataFrame 'df'
for x in range(len(df)):
    
    # utilizamos el método 'loc' para seleccionar todas las columnas desde "2000-01-31" hasta el final y calculamos el promedio
    # convertimos el resultado a entero y lo añadimos a la lista 'means'
    means.append(int(df.loc[x, "2000-01-31":].mean()))

# creamos un diccionario con dos claves: "RegionName" y "PriceMean"
# asignamos como valor para la clave "RegionName" la lista "Region_name" y como valor para la clave "PriceMean" la lista "means"
diccionario = {"RegionName":Region_name, "PriceMean":means}

# creamos un nuevo DataFrame llamado 'df2' utilizando el diccionario creado anteriormente
df2 = pd.DataFrame(diccionario)

# ordenamos el DataFrame 'df2' en orden descendiente utilizando el método 'sort_values' y seleccionamos las primeras 5 filas con 'head(5)'
# guardamos el resultado en un nuevo DataFrame 'df3'
df3 = df2.sort_values(by='PriceMean', ascending=False).head(5)

# imprimimos el DataFrame 'df3'
df3


# <h4>Este segmento de código utiliza la librería matplotlib para crear un gráfico de barras con el DataFrame 'df3', donde en el eje x se encuentra la columna 'RegionName' y en el eje y se encuentra la columna 'PriceMean', se agrega el título "Promedio de precios mas altos por región" y las etiquetas "Región" y "Promedio de precios" al eje x e y respectivamente.</h4>

# In[7]:


colores = ['red', 'yellow', 'blue', 'purple', 'green']

# utilizamos el método 'plot' con el argumento kind='bar' para crear un gráfico de barras
df3.plot(x='RegionName', y='PriceMean', kind='bar', legend=False, color=colores)

# agregamos título y etiquetas a los ejes
plt.title("Promedio de precios mas altos por región")
plt.xlabel("Región")
plt.ylabel("Promedio de precios")

# mostramos el gráfico
plt.show()


# <h4>Este segmento de código utiliza el paquete pandas para ordenar un DataFrame llamado 'df2' en orden ascendente utilizando la columna 'Mean' como criterio de ordenamiento, luego selecciona las primeras 5 filas del DataFrame ordenado y guarda el resultado en un nuevo DataFrame llamado 'df4' y finalmente se imprime el DataFrame 'df4' para mostrar las primeras 5 filas del DataFrame 'df2' ordenadas de manera ascendente utilizando la columna 'Mean' como criterio de ordenamiento.</h4>

# In[8]:


# ordenamos el DataFrame 'df2' en orden ascendente utilizando la columna 'Mean' como criterio de ordenamiento
df4 = df2.sort_values(by='PriceMean', ascending=True)

# seleccionamos las primeras 5 filas del DataFrame ordenado
df4 = df4.head(5)

# imprimimos el DataFrame 'df4' para mostrar las primeras 5 filas del DataFrame 'df2' ordenadas de manera ascendente utilizando la columna 'Mean' como criterio de ordenamiento
print(df4)


# <h4>Este segmento de código utiliza la librería matplotlib para crear un gráfico de barras con el DataFrame 'df4', donde en el eje x se encuentra la columna 'RegionName' y en el eje y se encuentra la columna 'PriceMean', se agrega el título "Promedio de precios mas altos por región" y las etiquetas "Región" y "Promedio de precios" al eje x e y respectivamente.</h4>

# In[9]:


colores = ['red', 'yellow', 'blue', 'purple', 'green']

# utilizamos el método 'plot' con el argumento kind='bar' para crear un gráfico de barras
df4.plot(x='RegionName', y='PriceMean', kind='bar', legend=False, color=colores)

# agregamos título y etiquetas a los ejes
plt.title("Promedio de precios mas bajos por región")
plt.xlabel("Región")
plt.ylabel("Promedio de precios")

# mostramos el gráfico
plt.show()


# <h4>Este segmento de código guarda los DataFrames 'df3' y 'df4' en archivos CSV llamados "Promedio_Precios_Altos_Por_Region.csv" y "Promedio_Precios_Bajos_Por_Region.csv" respectivamente, los índices no son guardados en los archivos CSV.</h4>

# In[10]:


df3.to_csv("Promedio_Precios_Altos_Por_Region.csv", index=False)
df4.to_csv("Promedio_Precios_Bajos_Por_Region.csv", index=False)

