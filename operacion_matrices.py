#Este programa hace operaciones con matrices
import numpy as np
import sys
matA=np.zeros([filasA, columnA])
matB=np.zeros([filasB, columnB])
print("Hola así que quieres hacer operaciones con matrices ;D");
action=str(input('¿Qué quieres hacer? (sumar/multiplicar, inversa/determinante o resolver_sistema_de_ecuaciones): '))
if (action=="sumar/multiplicar"):
    print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-")
    filasA=int(input('Filas de la matriz A: '))
    columnA=int(input('Columnas de la matriz A: '))
    filasB=int(input('Filas de la matriz B: '))
    columnB=int(input('Columnas de la matriz B: '))
    print("Introduce los elementos de la matriz A: ")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    print("Introduce los elementos de la matriz B: ")
    for i in range(0,filasB):
        for j in range(0,columnB):
            matB[i,j]=input('Elemento b[' + str(i+1) + str(j+1) + ']: ')
    op=str(input('¿Qué vamos a hacer con tus matrices? (sumar o multiplicar): '))
    if (op=="sumar"):
        sumar()
    else:
        multiplicar()
elif (action=="resolver_sistema_de_ecuaciones"):
    print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-")
    filasA=int(input('Filas de la matriz A: '))
    columnA=int(input('Columnas de la matriz A: '))
    filasB=int(input('Filas de la matriz B: '))
    columnB=int(input('Columnas de la matriz B: '))
    print("Introduce los elementos de la matriz A: ")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    print("Introduce los elementos de la matriz B: ")
    for i in range(0,filasB):
        for j in range(0,columnB):
            matB[i,j]=input('Elemento b[' + str(i+1) + str(j+1) + ']: ')
    resolver_sistema_de_ecuaciones()
else:
    print("A continuación pondrás el número de filas y columnas de tu matriz.-")
    filasA=int(input('Filas de la matriz: '))
    columnA=int(input('Columnas de la matriz: '))
    print("Introduce los elementos de la matriz: ")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    op1=str(input("¿Qué vamos a calcular de tu matriz? (inversa o determinante): "))
    if (op1=="inversa"):
        inversa()
    else:
        determinante()

def sumar():
    while (filasA!=filasB or columnA!=columnB):
        print("¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, vuelve a intentarlo...")
        print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-")
        filasA=int(input('Filas de la matriz A: '))
        columnA=int(input('Columnas de la matriz A: '))
        filasB=int(input('Filas de la matriz B: '))
        columnB=int(input('Columnas de la matriz B: '))
    if (filasA==filasB and columnA==columnB):
        resultS=matA+matB
        print("La matriz que resulta de sumar A y B es:"); print(resultS); print("Programa finalizado. Hasta pronto.")

def multiplicar():
    while (columnA!=filasB):
        print("¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, vuelve a intentarlo...")
        print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-")
        filasA=int(input('Filas de la matriz A: '))
        columnA=int(input('Columnas de la matriz A: '))
        filasB=int(input('Filas de la matriz B: '))
        columnB=int(input('Columnas de la matriz B: '))
    if (columnA==filasB):
        resultM=matA@matB
        print("La matriz que resulta de multiplicar A y B es:"); print(resultM); print("Programa finalizado. Hasta Pronto.")

def inversa():
    np.linalg.inv(matA)
    print("La inversa de su matriz es: "); print(np.linalg.inv(matA)); print("Programa finalizado. Hasta Pronto.")

def determinante():
    np.linalg.det(matA)
    print("El determinante de su matriz es: "); print(np.linalg.det(matA)); print("Programa finalizado. Hasta Pronto.")

def resolver_sistema_de_ecuaciones():
    np.linalg.solve(matA, matB)
    print("La solución de su sistema de ecuaciones es: "); print(np.linalg.solve(matA, matB)); print("Programa finalizado. Hasta Pronto.")