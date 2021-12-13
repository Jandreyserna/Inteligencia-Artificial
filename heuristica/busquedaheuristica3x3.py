from arbol3x3 import Nodo
import copy

def busqueda_heuristica(e_inicial, e_final):
    exito = False
    nodos_frontera = []
    nodos_visitados = []
    # creacion del primer nodo inicial o un objeto de tipo Nodo
    NodoInicial = Nodo (e_inicial)
    nodos_frontera.append(NodoInicial)
    comparaciones = 0
    textoError = ""
    while len(nodos_frontera) != 0 and (not exito):
        #nodo es el nodo padre inicialmente y nodos_frontera llegaria a ser una cola por que saca el primero que estuvo en la cola y asi sucesivamente
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        print("Vuelta = ", comparaciones)
        if nodo.obtener_datos() == e_final:
            exito = True
            print("Cantidad de comparaciones: ", comparaciones)
            return nodo
        else:
            comparaciones+=1
            aux = nodo.obtener_datos()
            fila = 0
            columna = 0
            x = len(aux)
            y = len(aux[0])

            for i in range(x):
                for j in range(y):
                    if aux[i][j] == 0:
                        fila = i
                        columna = j
                        break
            
            nodos_hijos=[]
            # hallamos el centro de la matriz
            if fila == columna and ( fila + columna) == 2:
                mateux = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, -1) # movemos el cero a la izquierda
                nodo_izquierdo = Nodo(mateux)
                nodo_izquierdo.asignar_coste( costodelnodo(e_final, mateux) )

                mateux = nodoresultante3x3( copy.deepcopy(aux), fila, columna, -1, 0) # movemos el cero arriba
                nodo_arriba = Nodo(mateux)
                nodo_arriba.asignar_coste( costodelnodo(e_final, mateux) )

                mateux = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, 1) # movemos el cero a la derecha
                nodo_derecho = Nodo(mateux)
                nodo_derecho.asignar_coste( costodelnodo(e_final, mateux) )

                mateux = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 1, 0) # movemos el cero abajo
                nodo_abajo = Nodo(mateux)
                nodo_abajo.asignar_coste( costodelnodo(e_final, mateux) )

                if nodo_izquierdo.en_lista(nodos_visitados) == False:
                    nodos_hijos.append(nodo_izquierdo)
                if nodo_arriba.en_lista(nodos_visitados) == False:
                    nodos_hijos.append(nodo_arriba)
                if nodo_derecho.en_lista(nodos_visitados) == False:
                    nodos_hijos.append(nodo_derecho)
                if nodo_abajo.en_lista(nodos_visitados) == False:
                    nodos_hijos.append(nodo_abajo)

            #Buscamos el nodo con mayor items en comun
                nodo_elegido = buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_elegido)
                try:
                    nodo.asignar_hijos([nodo_elegido])
                except:
                    textoError = "Sin Nodos, No Solucionado"
                    break
            elif fila == 1 or columna == 1:
                #pillamos si en uno de los centros laterales esta el cero
                #  clon = copy.deepcopy(aux)
                if fila == 1: # detectamos que el cero este en uno de los 4 centros

                    nodo_arriba = nodoresultante3x3( copy.deepcopy(aux), fila, columna, -1, 0 )
                    nodo_abajo = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 1, 0 ) #

                    if fila > columna:
                        nodo_centro = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, 1 )
                    else:
                        nodo_centro = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, -1 ) #movemos cero hacia el centro
                    nodo_A = Nodo(nodo_arriba)
                    nodo_A.asignar_coste( costodelnodo( e_final, nodo_arriba ))
                    nodo_B = Nodo(nodo_abajo)
                    nodo_B.asignar_coste( costodelnodo( e_final, nodo_abajo ))
                    nodo_C = Nodo(nodo_centro)
                    nodo_C.asignar_coste( costodelnodo( e_final, nodo_centro ))
                    if nodo_A.en_lista( nodos_visitados ) == False:
                        nodos_hijos.append(nodo_A)
                    if nodo_B.en_lista( nodos_visitados ) == False:
                        nodos_hijos.append(nodo_B)
                    if nodo_C.en_lista( nodos_visitados ) == False:
                        nodos_hijos.append(nodo_C)
                else:
                    nodo_izquierda = nodoresultante3x3( copy.deepcopy( aux ), fila, columna, 0, -1 ) # mover cero a la izquierda
                    nodo_derecha = nodoresultante3x3( copy.deepcopy( aux ), fila, columna, 0, 1 ) # mover cero a la derecha
                    if columna > fila:
                        nodo_centro = nodoresultante3x3( copy.deepcopy( aux ), fila, columna, 1, 0 ) # mover cero al centro
                    else:
                        nodo_centro = nodoresultante3x3( copy.deepcopy( aux ), fila, columna, -1, 0 ) # mover cero al centro
                    nodo_I = Nodo(nodo_izquierda)
                    nodo_I.asignar_coste( costodelnodo( e_final, nodo_izquierda ) )
                    nodo_C = Nodo(nodo_centro)
                    nodo_C.asignar_coste( costodelnodo( e_final, nodo_centro) )
                    nodo_D = Nodo(nodo_derecha)
                    nodo_D.asignar_coste( costodelnodo( e_final, nodo_derecha ) )
                    if nodo_I.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_I)
                    if nodo_C.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_C)
                    if nodo_D.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_D)

                nodo_elegido = buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_elegido)
                try:
                    nodo.asignar_hijos([nodo_elegido])
                except:
                    textoError = "Sin Nodos, No Solucionado"
                    break
            else:
                #ubicamos si en una de las esquinas esta el cero
                if fila <= columna and ( fila + columna ) < len(aux) : # para los ceros que estan en 
                    #esquinas
                    nodo_abajo = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 1, 0) # muev
                    if columna <= fila:
                        nodo_lado = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, 1) #
                    else:
                        nodo_lado = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, -1) #
                    nodo_A = Nodo(nodo_abajo)
                    nodo_A.asignar_coste( costodelnodo( e_final, nodo_abajo ) )
                    nodo_L = Nodo(nodo_lado)
                    nodo_L.asignar_coste( costodelnodo( e_final, nodo_lado) )
                    if nodo_A.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_A)
                    if nodo_L.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_L)
                else: #ceros que estan en las esquinas inferiores
                    nodo_arriba = nodoresultante3x3( copy.deepcopy(aux), fila, columna, -1, 0) #mueve cero hacia arriba
                    if columna < fila: 
                        nodo_abajo = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, 1) #mueve cero hacia derecha
                    else:
                        nodo_abajo = nodoresultante3x3( copy.deepcopy(aux), fila, columna, 0, -1) #mueve cero hacia izquierda
                    nodo_AA = Nodo(nodo_arriba)
                    nodo_AA.asignar_coste( costodelnodo( e_final, nodo_arriba ) )
                    nodo_AAA = Nodo(nodo_abajo)
                    nodo_AAA.asignar_coste( costodelnodo( e_final, nodo_abajo) )
                    if nodo_AA.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_AA)
                    if nodo_AAA.en_lista( nodos_visitados) == False :
                        nodos_hijos.append(nodo_AAA)
                nodo_elegido = buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_elegido)
                try:
                    nodo.asignar_hijos([nodo_elegido])
                except:
                    textoError = "Sin Nodos, No Solucionado"
                    break
    return textoError           

def nodoresultante3x3( nodo, posicionx, posiciony, sumaorestaX, sumaorestaY ): #se intercambia el cero a otra celda especifica
    nodo[posicionx][posiciony] = nodo[posicionx + sumaorestaX][posiciony + sumaorestaY]
    nodo[posicionx + sumaorestaX][posiciony + sumaorestaY] = 0
    return nodo

def costodelnodo(nodooriginal, nodohijo): #obtenemod los numeros de celdass parecidas a la matriz resultante
    costo = 0
    for i in range (len(nodooriginal)):
        for j in range( len(nodooriginal[0] )):
            if nodooriginal[i][j] == nodohijo[i][j]:
                costo+=1
    return costo

def buscar_nodo_elegido(lista_nodos_hijos): #de todos los nodos y matricez resultantes solo el que tiene mayor costo sera el ideal
    coste = 0
    nodo_eficiente = []
    for item in lista_nodos_hijos:
        if( item.obtener_coste()>coste):
            nodo_eficiente = item
            coste = item.obtener_coste()
        elif item.obtener_coste() == coste:
            lista1 = encontrar_cero( item.obtener_datos() )
            x1 = lista1[0] #fiula
            y1 = lista1[1] #columna
            if (x1 + y1) >= 2 and x1 > 0 and y1 > 0 and x1 < 3 and y1 < 3:
                nodo_eficiente = item
    return nodo_eficiente

def encontrar_cero(nodo):
    fila = 0
    columna = 0
    for i in range( len(nodo)):
        for j in range( len(nodo[0])):
            if nodo[i][j] == 0:
                fila = i
                columna = j
                break
    return [fila, columna]

estado_inicial = ([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
estado_final = ([[1, 2, 3], [4, 8, 6], [7, 5, 0]])

solucion = busqueda_heuristica(estado_inicial, estado_final)

print("la solucion es ->: ", solucion)
nivel = 0
datos_camino = []
nodo_aux = solucion
if (solucion != "Sin Nodos, No Solucionado"):
    while(nodo_aux.obtener_padre()!= None):
        datos_camino.append(nodo_aux.obtener_datos())
        lista = nodo_aux.obtener_datos()
        nodo_aux=nodo_aux.obtener_padre()
    datos_camino.append(estado_inicial)
    datos_camino.reverse()
    print ("el camino Es: ")
    for i in range( len(datos_camino)):
        for j in range(len(datos_camino[0])):
            print("\033[1;33m"+"[ ",datos_camino[i][j][0],",",datos_camino[i][j][1],",",datos_camino[i][j][2]," ]"+ '\033[0;m')
            print(" ")














