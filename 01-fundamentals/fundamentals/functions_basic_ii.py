"""
1   Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
        Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

2   Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
        Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

3   Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
        Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

4   Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga 
    solo los valores de la lista original que sean mayores que su segundo valor.
    Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
        Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
        Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

5   Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
    La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
        Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
        Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2] """

#  1 Cuenta regresiva: 
def regresiva(n):
    for n in range(n,-1,-1):
        print(n)

regresiva(5)


#  2  imprimir_y_devolver
def imprimir_y_devolver (x, y):
    print(x)
    return(y)
    
imprimir_y_devolver(1,2)

# 3  primero_mas_longitud
def primero_mas_longitud(lista):
    print(lista[0])
    suma = lista[0] +len(lista)
    return suma

print("ejercicio 3")
lista = primero_mas_longitud([1,2,3,4,5])

print (f"suma {lista}")
print("fin de ejercicio 3")


#Valores mayores que el segundo:

def valores_mayores_que_el_segundo(lista):
    j = len(lista) -1
   
    for i in range(j):
        n1 = lista[i]
        n2 = lista[i+1]
        if n1>n2:
            listafinal.append(n1)
            print(n1, n2)
    return(listafinal)
    

print ("inicio ejecicio Valores mayores que el segundo" )
listafinal=[]
#valores_mayores_que_el_segundo([5,2,3,2,1,4])
valores_mayores_que_el_segundo([3])
print(listafinal)

#Esta longitud, ese valor:
#
def length_and_value(p,q):
    for n in range(p):
        arr.append(q)
    print(arr)

arr=[]
length_and_value(4,7)
