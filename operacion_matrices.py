#Este programa hace operaciones con matrices
import numpy as np
import sys

def sumar(matA, matB):
    if (filasA==filasB and columnA==columnB):
        resultS=matA+matB
    print("\n----------------------\n"); print("La matriz que resulta de sumar A y B es:"); print(resultS); print("Programa finalizado. Hasta pronto.\n")
        

def multiplicar( matA, matB):
    if (columnA==filasB):
        resultM=matA@matB
    print("\n----------------------\n"); print("La matriz que resulta de multiplicar A y B es:"); print(resultM); print("Programa finalizado. Hasta pronto.\n")

def inversa(matA):
    if (np.linalg.det(matA)==0):
        print("\nNo puedes calcular la inversa de la matriz, porque no es una matriz singular."); print("Es decir, el determinante de tu matriz no es distinto de cero. Programa finalizado. Hasta pronto.\n")
    else:
        invA=np.linalg.inv(matA)
        print("\n----------------------\n"); print("La inversa de su matriz es:"); print(invA); print("Programa finalizado. Hasta pronto.\n")

def determinante(matA):
    determ=np.linalg.det(matA)
    print("\n----------------------\n"); print("El determinante de su matriz es:"); print(determ); print("Programa finalizado. Hasta Pronto.\n")

def resolver_sistema_de_ecuaciones(matA, matB):
    np.linalg.solve(matA, matB)
    print("\n----------------------\n"); print("La solución de su sistema de ecuaciones es:"); print(np.linalg.solve(matA, matB)); print("Programa finalizado. Hasta pronto.\n")

print("\nHola así que quieres hacer operaciones con matrices ;D" );
action=str(input('¿Qué quieres hacer? (sumar, multiplicar, inversa, determinante o resolver sistema de ecuaciones): '))
if (action=='sumar'):
    print("\n-------------------------------------")
    print("\nA continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-\n")
    filasA=int(input('Filas de la matriz A: '))
    columnA=int(input('Columnas de la matriz A: '))
    filasB=int(input('Filas de la matriz B: '))
    columnB=int(input('Columnas de la matriz B: '))
    while filasA!=filasB or columnA!=columnB:
        print("\n¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, vuelve a intentarlo...");
        print("\n----------------------");
        print("\nA continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-\n")
        filasA=int(input('Filas de la matriz A: '))
        columnA=int(input('Columnas de la matriz A: '))
        filasB=int(input('Filas de la matriz B: '))
        columnB=int(input('Columnas de la matriz B: '))
    matA=np.zeros([filasA, columnA])
    matB=np.zeros([filasB, columnB])
    print("\n----------------------\n");
    print("Introduce los elementos de la matriz A:\n")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    print("\nIntroduce los elementos de la matriz B:\n")
    for i in range(0,filasB):
        for j in range(0,columnB):
            matB[i,j]=input('Elemento b[' + str(i+1) + str(j+1) + ']: ')
    sumar(matA, matB)
elif (action=='multiplicar'):
    print("\n-------------------------------------\n");
    print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-\n")
    filasA=int(input('Filas de la matriz A: '))
    columnA=int(input('Columnas de la matriz A: '))
    filasB=int(input('Filas de la matriz B: '))
    columnB=int(input('Columnas de la matriz B: '))
    while columnA!=filasB:
        print("\n¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, vuelve a intentarlo...");
        print("\n----------------------\n");
        print("A continuación pondrás los numeros de las filas y columnas de las matrices respectivamente.-\n")
        filasA=int(input('Filas de la matriz A: '))
        columnA=int(input('Columnas de la matriz A: '))
        filasB=int(input('Filas de la matriz B: '))
        columnB=int(input('Columnas de la matriz B: '))
    matA=np.zeros([filasA, columnA])
    matB=np.zeros([filasB, columnB])
    print("\n----------------------\n");
    print("Introduce los elementos de la matriz A:\n")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    print("\nIntroduce los elementos de la matriz B:\n")
    for i in range(0,filasB):
        for j in range(0,columnB):
            matB[i,j]=input('Elemento b[' + str(i+1) + str(j+1) + ']: ')
    multiplicar(matA, matB)
elif (action=='inversa'):
    print("\n-------------------------------------\n");
    print("A continuación pondrás el número de filas y columnas de tu matriz a la que calcularemos su inversa.-\n")
    filasA=int(input('Filas de la matriz: '))
    columnA=int(input('Columnas de la matriz: '))
    while filasA!=columnA:
        print("\n¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, la matriz debe ser cuadrada, vuelve a intentarlo...");
        print("\n----------------------\n");
        print("A continuación pondrás el número de filas y columnas de tu matriz a la que calcularemos su inversa.-\n")
        filasA=int(input('Filas de la matriz: '))
        columnA=int(input('Columnas de la matriz: '))
    matA=np.zeros([filasA, columnA])
    print("\n----------------------\n");
    print("Introduce los elementos de la matriz:\n")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    inversa(matA)
elif (action=='determinante'):
    print("\n-------------------------------------\n");
    print("A continuación pondrás el número de filas y columnas de tu matriz que le calcularemos su determinante.-\n")
    filasA=int(input('Filas de la matriz: '))
    columnA=int(input('Columnas de la matriz: '))
    while filasA!=columnA:
        print("\n¡¡NO PUEDES REALIZAR LA OPERACIÓN!!, la matriz debe ser cuadrada, vuelve a intentarlo...");
        print("\n----------------------\n");
        print("A continuación pondrás el número de filas y columnas de tu matriz que le calcularemos su determinante.-\n")
        filasA=int(input('Filas de la matriz: '))
        columnA=int(input('Columnas de la matriz: '))
    matA=np.zeros([filasA, columnA])
    print("\n----------------------\n");
    print("Introduce los elementos de la matriz:\n")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    determinante(matA)
elif (action=='resolver sistema de ecuaciones'):
    print("\n-------------------------------------\n");
    print("A continuación pondrás los numeros de las filas y columnas de las matrices para resolver el sistema.-\n")
    filasA=int(input('Filas de la matriz A: '))
    columnA=int(input('Columnas de la matriz A: '))
    filasB=int(input('Filas de la matriz B: '))
    columnB=int(input('Columnas de la matriz B: '))
    matA=np.zeros([filasA, columnA])
    matB=np.zeros([filasB, columnB])
    print("\n----------------------\n"); print("NOTA: Si te marca error después de que ingreses los elementos de tu sistema, es porque tu sistema no tiene solución o porque tiene infinidad de soluciones.")
    print("Introduce los elementos de la matriz A:\n")
    for i in range(0,filasA):
        for j in range(0,columnA):
            matA[i,j]=input('Elemento a[' + str(i+1) + str(j+1) + ']: ')
    print("\nIntroduce los elementos de la matriz B: \n")
    for i in range(0,filasB):
        for j in range(0,columnB):
            matB[i,j]=input('Elemento b[' + str(i+1) + str(j+1) + ']: ')
    resolver_sistema_de_ecuaciones(matA, matB)
else:
    print("\nGracias vuelva pronto. Programa finalizado.")