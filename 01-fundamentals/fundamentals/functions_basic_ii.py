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


""" RESPUESTAS:
# ! Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))
# ? Example: countdown(5) should return [5,4,3,2,1,0]

# ! Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))
# ? Example: print_and_return([1,2]) should print 1 and return 2


# ! First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))
# ? Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


# ! Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# ? Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# ? Example: values_greater_than_second([3]) should return False

# ! This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
# ? Example: length_and_value(4,7) should return [7,7,7,7]
# ? Example: length_and_value(6,2) should return [2,2,2,2,2,2]
"""