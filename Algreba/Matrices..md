# Matrices con Numpy


```python
import numpy as np
```


```python
#Creamos una matriz fila
row = [1,2,3]
row
```




    [1, 2, 3]




```python
#Matriz colmna
col = [[1],[2],[3]]
col
```




    [[1], [2], [3]]




```python
#Crear una matriz.
M = [[1,2,3],[4,5,6],[8,7,6]]
M
```




    [[1, 2, 3], [4, 5, 6], [8, 7, 6]]




```python
#Para llamar a un elemento se usa la siguiente sintaxis:
M[0][0]
```




    1



Cambiamos la sintaxis de la matriz para poder trabajar correctamente con ella:



```python
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(M)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


Algo interesante de numpy es que en la funcion ``np.array()`` tiene un parametro `dtype` en el cual podemos indicar el tipo de dato de la matriz.


```python
M = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
print(M)
```

    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]



```python
M = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=complex)
print(M)
```

    [[1.+0.j 2.+0.j 3.+0.j]
     [4.+0.j 5.+0.j 6.+0.j]
     [7.+0.j 8.+0.j 9.+0.j]]



```python
#Si queremos crar una matriz de ceros usamos la funcion `np.zeros((fil,col))
print(np.zeros((5,10)))
#Si queremos crar una matriz de ceros usamos la funcion `np.ones((fil,col))
print(np.ones((5,10)))
```

    [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
    [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]



```python
#Matriz diagonal
x = [1,2,3,4]
N = np.diag(x)
N
```




    array([[1, 0, 0, 0],
           [0, 2, 0, 0],
           [0, 0, 3, 0],
           [0, 0, 0, 4]])




```python
#Dimension de una matriz
np.shape(M)
```




    (3, 3)




```python

```
