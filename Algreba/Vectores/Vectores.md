
# Vectores

Para crear un vector en python es necesario importar la libreria numpy.


```python
import numpy as np
```


```python
#Indicamos una lista ya que se trata de una sola columna.
x = np.array([1,2,3,4,5,6])
print(x)
```

    [1 2 3 4 5 6]



```python
#Dimension del vector
len(x)
```




    6




```python
#Suma
y = np.array([2,6,89,3,4,5])
print(x + y)
#Resta
print(x - y)
```

    [ 3  8 92  7  9 11]
    [ -1  -4 -86   1   1   1]



```python
#Producto por escalar
print(2*x)
print(3*2*x)
print(3**x)
```

    [ 2  4  6  8 10 12]
    [ 6 12 18 24 30 36]
    [  3   9  27  81 243 729]


## Producto escalar & Norma


```python
def productoEsca(x,y):
    if len(x) == len(y):
        suma = 0
        for i in range(0,len(x)):
            suma = suma + x[i]*y[i]
            return suma
        else:
            return "ERROR"

productoEsca(x,y)
```




    2




```python
#Norma euclidea 
np.linalg.norm(x)
```




    9.539392014169456



## Distancia entre 2 puntos.


```python
def distancia(x,y):
    import numpy as np
    if len(x) == len(y):
        dist = np.linalg.norm(x-y)
        return dist
    else:
        return"Error"
```


```python
distancia(x,y)
```




    86.11620056644394



## Angulo entre 2 vectores.


```python
def Angulo(x,y):
    import numpy as np
    import math
    if len(x) == len(y):
        angulo = math.acos(productoEsca(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)))
        return angulo/(2*math.pi)*360
    else:
        return "ERROR"
```


```python
Angulo(x,y)
```




    89.86578873703736



## Proyeccion ortogonal.


```python
def proyOrt(u,v):
    import numpy as np
    if len(u) == len(v):
        proy = (productoEsca(u,v)/pow(np.linalg.norm(u),2))*u
        return proy
    else:
        return "ERROR"
    
print(proyOrt(x,y))
```

    [0.02197802 0.04395604 0.06593407 0.08791209 0.10989011 0.13186813]


## Producto vectorial


```python
def prodV(x,y):
    import numpy as np
    if len(x) == len(y) and len(x) == 3:
        z = np.array(x[1]*y[2] - x[2]*x[1], -(x[o]*y[2]-x[2]*y[0]), x[0]*y[1]-x[1]*y[0])
        return z
    else:
        return "ERROR"
prodV(x,y)    
        
```




    'ERROR'




```python

```
