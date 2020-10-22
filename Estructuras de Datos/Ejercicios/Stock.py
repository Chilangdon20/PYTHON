def VenderComprarAccion(precio, n): 
    """
    Funcionamiento:
    
    Esta funcion sirve para 
    encontrar el maximo beneficio en la compra y venta de acciones.
    

    toma como argumentos la lista de acciones y el tamaño de nuestra lista de precios de acciones.

    parametros:
    
    precio 

    n 

    salida:

    compra el dia:  n   vende el dia: n

    """      
    # En esta funcion primero verificamos que los precios se den por almenos 2 dias, de lo contrario regresamos.
 
    if (n == 1): 
        return
      
    

    i = 0
    # creamos este loop , mientras que i sea mas pequeño que n-1 , esto significa que si i es mas pequeño que n-1 , entonces aun hay mas elementos a procesar dentro de nuestra lista de acciones.

    while (i < (n - 1)): 
          
        # Ahora trataremos de encontrar un minimo local , para eso ejecutamos un ciclo while con la condicion de que el precio de la siguiente accion sea menor que el elemento actual. Hasta que se cumpla esta condicion incrementaremos el valor de i.

        while ((i < (n - 1)) and (precio[i + 1] <= precio[i])): 
            i += 1
          
        # Una vez terminado el ciclo , verificamos si i es igual a n-1 if(i == n-1):break , si este es el caso significa que no hay mas soluciones posibles y por lo tanto rompemos el ciclo.

        if (i == n - 1): 
            break
          
        # De lo contrario almacenamos el indice de nuestros minimos locale
        comprar = i 
        i += 1
          
        # buscaremos los maximos locales con un while , mientras que el precio del elemento actual sea mayor que el elemento anterior  y hasta que se cumpla esta condicion , seguimos incrementando el valor de i.

        while ((i < n) and (precio[i] >= precio[i - 1])): 
          # Una vez salimos de este ciclo , guardamos el indice de maximos como i-
            i += 1
              
        # Almacenar el índice de máximos
        vender = i - 1
          
        print("Compra accion el dia: ",comprar,"\t", 
                "Vende accion  el dia: ",vender) 
          

# precios de acciones
precio = [1183
,1159.45
,1185.17
,1193.8
,1195.82
,1195.35
,1191.83
,1180.79
,1168.43
,1176.07
,1174.35
,1180
,1199.995
,1186.43
,1157.8
,1165.52
,1172.97
,1203
,1217.63
,1224.87
,1227
,1242.5
,1228
,1138.95
,1132.62
,1143.45
,1135.47
,1149.32
,1142
,1150.92
,1146.73
,1145.34
,1142.93
,1146.16
,1132.32
,1110.32
,1125.87
,1119.37
,1118.5
,1104.83
,1101.04
,1077.23
,1086.75
,1091
,1115.08
,1120
,1109.86
,1121.7
,1107.24
,1111.5
,1089.1
,1089.74
,1084.71
,1079.95
,1096.99
,1077
,1054.28
,1046.21
,1055
,1044.49
,1066.93
,1105.64
,1120.15
,1132.7
,1141.48
,1152
,1146.07
,1151.25
,1154.48
,1153
,1175.83
,1084.02
,1107.3
,1083.49
,1055.02
,1072.53
,1089
,1091.4
,1068.2
,1020.01
,1096.54
,1048.33
,1080.3
,1115
,1091.29
,1112.51
,1103.71
,1130
,1140
,1113.48
,1118
,1119.64
,1079.04
,1136.4
,1151.31
,1160
,1176
,1205.03
,1212
,1206.67
,1213
,1204.09
,1200
,1193.69
,1184.25
,1159.41
,1194.92
,1180.67
,1168.96
,1162.66
,1177.77
,1188
,1179.7
,1182
,1171.1
,1184.2
,1172
,1198.57
,1209.22
,1222.52
,1252.21
,1263.4
,1255
,1255.9
,1244.14] 
n = len(precio) 
  
VenderComprarAccion(precio, n) 
