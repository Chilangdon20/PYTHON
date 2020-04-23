
# Funcion `cut()`

## Parámetros:

* x: tipo matriz
La matriz de entrada que se agrupará. Debe ser unidimensional.
contenedores: int, secuencia de escalares o pandas.IntervalIndex
Los criterios para bin por:

 * **int:**
   define el número de contenedores de igual ancho en el rango de x.   El rango de x se extiende en .1% en cada lado para incluir los valores     mínimos y máximos de x.
 
* **Secuencia de escalares:** define los bordes del depósito permitiendo un ancho no uniforme. No se realiza ninguna extensión del rango de x.

* **IntervalIndex:** define las ubicaciones exactas que se utilizarán.

* **derecha:** bool, predeterminado True
  Indica si los contenedores incluyen el borde más a la derecha o no. Si     correcto == Verdadero (el valor predeterminado), los bins [1, 2, 3, 4]     indican (1,2], (2,3], (3,4]. Este argumento se ignora cuando bins es un   IntervalIndex .
  
  
* **etiquetas:** array o bool, opcional
  Especifica las etiquetas para los contenedores devueltos. Debe tener la   misma longitud que los contenedores resultantes. Si es falso, solo     devuelve indicadores enteros de los contenedores. Esto afecta el tipo del contenedor de salida (ver más abajo). Este argumento se ignora cuando bins es un IntervalIndex.
  
  
* **retbins:** bool, falso predeterminado
  Si devolver los contenedores o no. Útil cuando los contenedores se proporcionan como escalares.
  
  
*  **precisión:** int, por defecto 3
   La precisión con la que almacenar y mostrar las etiquetas de los       contenedores.
   
* **include_lowest:** bool, falso predeterminado
  Si el primer intervalo debe ser inclusivo a la izquierda o no.

* **duplicados:** {predeterminado "subir", "soltar", opcional
  Si los bordes del contenedor no son únicos, aumente ValueError o elimine los no únicos.

Fuente: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.cut.html

## Conceptos extra:


### Tabla dinámica:


Una tabla dinámica es una tabla de estadísticas que **resume los datos de una tabla más extensa (como una base de datos, una hoja de cálculo o un programa de inteligencia empresarial)**. 

Este resumen puede incluir sumas, promedios u otras estadísticas, que la tabla dinámica agrupa de manera significativa.

Las tablas dinámicas son una técnica en el procesamiento de datos. Organizan y reorganizan (o "pivotan") las estadísticas para llamar la atención sobre información útil.

Aunque tabla dinámica es un término genérico, Microsoft registró la tabla dinámica en los Estados Unidos en 1994. 

fuente: https://en.wikipedia.org/wiki/Pivot_table


```python
import numpy as np
import pandas as pd
import seaborn as sb
```


```python
titanic = sb.load_dataset('titanic')
titanic.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Obtenemos por genero y la media de supervivencia
titanic.groupby('sex')[['survived']].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.742038</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.188908</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Obtenemos por genero ,clasesocial e investigamos la columna supervivientes y con la funcion aggregate calculamos su media
titanic.groupby(['sex','pclass'])['survived'].aggregate('mean').unstack()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
    </tr>
  </tbody>
</table>
</div>



Podemos observar que nuestro codigo ya se ve bastante tedioso para lo que queremos realizar , para que nos sea mas sencillo hacer todo esto existen las tablas de pivotaje.


```python
#Con la funcion pivot_table podemos entender mejor como organizar la tabla
titanic.pivot_table('survived', index = 'sex', columns = 'pclass')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Catalogamos la edad de los tripulantes del titanic en intervalos indicando el parametro bins = a los intervalos que nos interesan
age = pd.cut(titanic['age'], bins = [0,18,25,35,50,65,100],include_lowest = True,precision = 1,right = False)
age
```




    0      [18.0, 25.0)
    1      [35.0, 50.0)
    2      [25.0, 35.0)
    3      [35.0, 50.0)
    4      [35.0, 50.0)
    5               NaN
    6      [50.0, 65.0)
    7       [0.0, 18.0)
    8      [25.0, 35.0)
    9       [0.0, 18.0)
    10      [0.0, 18.0)
    11     [50.0, 65.0)
    12     [18.0, 25.0)
    13     [35.0, 50.0)
    14      [0.0, 18.0)
    15     [50.0, 65.0)
    16      [0.0, 18.0)
    17              NaN
    18     [25.0, 35.0)
    19              NaN
    20     [35.0, 50.0)
    21     [25.0, 35.0)
    22      [0.0, 18.0)
    23     [25.0, 35.0)
    24      [0.0, 18.0)
    25     [35.0, 50.0)
    26              NaN
    27     [18.0, 25.0)
    28              NaN
    29              NaN
               ...     
    861    [18.0, 25.0)
    862    [35.0, 50.0)
    863             NaN
    864    [18.0, 25.0)
    865    [35.0, 50.0)
    866    [25.0, 35.0)
    867    [25.0, 35.0)
    868             NaN
    869     [0.0, 18.0)
    870    [25.0, 35.0)
    871    [35.0, 50.0)
    872    [25.0, 35.0)
    873    [35.0, 50.0)
    874    [25.0, 35.0)
    875     [0.0, 18.0)
    876    [18.0, 25.0)
    877    [18.0, 25.0)
    878             NaN
    879    [50.0, 65.0)
    880    [25.0, 35.0)
    881    [25.0, 35.0)
    882    [18.0, 25.0)
    883    [25.0, 35.0)
    884    [25.0, 35.0)
    885    [35.0, 50.0)
    886    [25.0, 35.0)
    887    [18.0, 25.0)
    888             NaN
    889    [25.0, 35.0)
    890    [25.0, 35.0)
    Name: age, Length: 891, dtype: category
    Categories (6, interval[int64]): [[0, 18) < [18, 25) < [25, 35) < [35, 50) < [50, 65) < [65, 100)]



Si nosotros queremos crear una nueva tabla ahora con informacion de los supervivientes en base a su genero y a su clase social con los intervalos de edad creados anteriormente.


```python
titanic.pivot_table('survived',index = ['sex',age],columns = 'class')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>age</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">female</th>
      <th>[0, 18)</th>
      <td>0.875000</td>
      <td>1.000000</td>
      <td>0.542857</td>
    </tr>
    <tr>
      <th>[18, 25)</th>
      <td>1.000000</td>
      <td>0.933333</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>[25, 35)</th>
      <td>0.928571</td>
      <td>0.923077</td>
      <td>0.434783</td>
    </tr>
    <tr>
      <th>[35, 50)</th>
      <td>1.000000</td>
      <td>0.866667</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>[50, 65)</th>
      <td>0.933333</td>
      <td>0.833333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">male</th>
      <th>[0, 18)</th>
      <td>1.000000</td>
      <td>0.818182</td>
      <td>0.232558</td>
    </tr>
    <tr>
      <th>[18, 25)</th>
      <td>0.125000</td>
      <td>0.050000</td>
      <td>0.106667</td>
    </tr>
    <tr>
      <th>[25, 35)</th>
      <td>0.550000</td>
      <td>0.083333</td>
      <td>0.207317</td>
    </tr>
    <tr>
      <th>[35, 50)</th>
      <td>0.450000</td>
      <td>0.052632</td>
      <td>0.069767</td>
    </tr>
    <tr>
      <th>[50, 65)</th>
      <td>0.217391</td>
      <td>0.090909</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>[65, 100)</th>
      <td>0.166667</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



Tambien podemos dividir los datos en cauntiles,esto los divide automaticamente sin especificar los bins.


```python
#Podemos agregar las etiquetas de los cuantiles como q1,q2..q4 como q1 = lo suqe pagaron poco , q2 los que pagaron un poco mas etc etc para entedner mejor los datos
fare = pd.qcut(titanic['fare'],precision = 1,q = 4, labels = ["Q1","Q2","Q3","Q4"])
fare
```




    0      Q1
    1      Q4
    2      Q2
    3      Q4
    4      Q2
    5      Q2
    6      Q4
    7      Q3
    8      Q2
    9      Q3
    10     Q3
    11     Q3
    12     Q2
    13     Q4
    14     Q1
    15     Q3
    16     Q3
    17     Q2
    18     Q3
    19     Q1
    20     Q3
    21     Q2
    22     Q2
    23     Q4
    24     Q3
    25     Q4
    26     Q1
    27     Q4
    28     Q1
    29     Q1
           ..
    861    Q2
    862    Q3
    863    Q4
    864    Q2
    865    Q2
    866    Q2
    867    Q4
    868    Q2
    869    Q2
    870    Q1
    871    Q4
    872    Q1
    873    Q2
    874    Q3
    875    Q1
    876    Q2
    877    Q1
    878    Q1
    879    Q4
    880    Q3
    881    Q1
    882    Q2
    883    Q2
    884    Q1
    885    Q3
    886    Q2
    887    Q3
    888    Q3
    889    Q3
    890    Q1
    Name: fare, Length: 891, dtype: category
    Categories (4, object): [Q1 < Q2 < Q3 < Q4]




```python
# Creamos una nueva tabla de pivotaje para ver como sobrevivieron en. base a su tipo de boleto
titanic.pivot_table('survived', index = ['sex',age],columns=[fare,'pclass'])

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>fare</th>
      <th colspan="2" halign="left">Q1</th>
      <th colspan="2" halign="left">Q2</th>
      <th colspan="3" halign="left">Q3</th>
      <th colspan="3" halign="left">Q4</th>
    </tr>
    <tr>
      <th></th>
      <th>pclass</th>
      <th>1</th>
      <th>3</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>age</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">female</th>
      <th>[0, 18)</th>
      <td>NaN</td>
      <td>0.800000</td>
      <td>1.000000</td>
      <td>0.800000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>0.461538</td>
      <td>0.875000</td>
      <td>1.0</td>
      <td>0.142857</td>
    </tr>
    <tr>
      <th>[18, 25)</th>
      <td>NaN</td>
      <td>0.750000</td>
      <td>0.800000</td>
      <td>0.200000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.600000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>[25, 35)</th>
      <td>NaN</td>
      <td>0.200000</td>
      <td>1.000000</td>
      <td>0.600000</td>
      <td>1.000000</td>
      <td>0.846154</td>
      <td>0.375000</td>
      <td>0.923077</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>[35, 50)</th>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.833333</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.857143</td>
      <td>0.333333</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>[50, 65)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.666667</td>
      <td>1.000000</td>
      <td>0.500000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">male</th>
      <th>[0, 18)</th>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.454545</td>
      <td>NaN</td>
      <td>0.857143</td>
      <td>0.285714</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.076923</td>
    </tr>
    <tr>
      <th>[18, 25)</th>
      <td>NaN</td>
      <td>0.095238</td>
      <td>0.071429</td>
      <td>0.111111</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.166667</td>
      <td>0.125000</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>[25, 35)</th>
      <td>0.0</td>
      <td>0.166667</td>
      <td>0.095238</td>
      <td>0.222222</td>
      <td>0.714286</td>
      <td>0.090909</td>
      <td>0.111111</td>
      <td>0.500000</td>
      <td>0.0</td>
      <td>0.750000</td>
    </tr>
    <tr>
      <th>[35, 50)</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.111111</td>
      <td>0.200000</td>
      <td>0.615385</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.416667</td>
      <td>NaN</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>[50, 65)</th>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.125000</td>
      <td>0.000000</td>
      <td>0.200000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.230769</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>[65, 100)</th>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.500000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Con esta tabla podemos observar que ningun individuo compro el boleto. basico de primera clase a excepcion de 2 que posiblemente les pudieron regalar el boleto , se tendria que investigar quienes son para esto hariamos el filtrado de datos. 

``DataFrame.pivot_table(titanic,values = None,index = None,columns = None,aggfunc="mean",fill_value="NoExiste",margins=True,dropna=True,margins_name="All"``



```python
titanic.pivot_table(index = "sex", columns = "pclass",
                   aggfunc={"survived":sum,"fare":"mean"})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">fare</th>
      <th colspan="3" halign="left">survived</th>
    </tr>
    <tr>
      <th>pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>106.125798</td>
      <td>21.970121</td>
      <td>16.118810</td>
      <td>91</td>
      <td>70</td>
      <td>72</td>
    </tr>
    <tr>
      <th>male</th>
      <td>67.226127</td>
      <td>19.741782</td>
      <td>12.661633</td>
      <td>45</td>
      <td>17</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic.pivot_table('survived', index="sex", columns = "class",margins = True, margins_name="Ttotal")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
      <th>Ttotal</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
      <td>0.742038</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
      <td>0.188908</td>
    </tr>
    <tr>
      <th>Ttotal</th>
      <td>0.629630</td>
      <td>0.472826</td>
      <td>0.242363</td>
      <td>0.383838</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic.pivot_table('age', index = "sex", columns = "class",aggfunc = "mean")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>34.611765</td>
      <td>28.722973</td>
      <td>21.750000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>41.281386</td>
      <td>30.740707</td>
      <td>26.507589</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
