#1
def number_of_food_groups():
    return 5
print("#1")
print(number_of_food_groups()) #llama a la funcion (number_of_food_groups)y retorna un 5, el cual se imprime
print("#1")

#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
print("#2")
print( number_of_military_branches())
print("#2")
# se llama a una primerea funcion que no está definida(number_of_days_in_a_week_silicon_or_triangle_sides()),
# y se sumaría el valor 5 que entrega la segunda funcion


#3
def number_of_books_on_hold():
    return 5
    return 10 #este return no aplica, porque ya envió en la linea anterios el valor 5 y cierra la funcion
print("#3")
print(number_of_books_on_hold()) #imprime el valor 5
print("#3")

#4
def number_of_fingers():
    return 5   #retorna en valor 5
    print(10) #esta linea no se ejecuta 
print("#4")
print(number_of_fingers()) #imprime el valor que retornó (return)  --> 5
print("#4")


#5
def number_of_great_lakes():
    print("#5")
    print(5)         # se imprime el valor 5
x = number_of_great_lakes() #llama a la funcion asignando en x el retultado, pero no se ejecuta, porque no se asigna nada...
print(x)  # no hay nada que imprimir por lo tante muestra "none"
print("#5")

#6

def add(b,c): #se declara funcion add
    print(b+c) # se muestra valor resultante de una suma de b y c


print("#6 inicio")
#print(add(1,2) + add(2,3)) # no imprime nada, pues la funcion se ejecuta imprimiría la lina dentro de la funcion, pero
                            # estalinea viene vacía, no hay retorno de valores,error('NoneType' and 'NoneType')
                            # no puede sumar valores 
print("#6 final")





#7
def concatenate(b,c):       # se define la funcion, recibe en b y c, los enteros 2 y 5 respectivamente 
    return str(b)+str(c)    # retorna convertido en string b y c
print("#7 inicio")
print(concatenate(2,5))     # muestra 25
print("#7 Final")

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100     #variable local B
    print(b)    # muestra 100
    if b < 10:  # 100<10? --> "False"
        return 5
    else:
        return 10   #retorna valor 10
    return 7

print("#8 inicio")
print(number_of_oceans_or_fingers_or_continents())  #imprime valor 10
print("#8 Final")

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # va a la funcion y retorna 7, y en esta linea se imprime
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # va a la funcion y retorna 14, y en esta linea se imprime
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
                                                        # la funcion suna  y muestra valor 21


#10
print("entra a la 10")
def addition(b,c):   #se declara la funcion, recibe en b y c
    return 10    #retorna un 10 
print(addition(3,5)) #muestra el valor 10,  no considera los argumentos
print("sale a la 10")


#11
print("entra a la 11")
b = 500             # se declara la variable b globalmente para el programa
print(b)            #  1°se muestra b  --> 500
def foobar():       # se define la funcion  foobar
    b = 300         # se declara la variable b localmente para la funcion
    print(b)        # se muestra b  3° --> 300
print(b)            # se muestra b  2° --> 500
foobar()            # se muestra b      --> 300
print(b)            # se muestra b  4° --> 500  // quedando finalmente: 500-500-300-500


#12
print("entra a la 12")
b = 500             # se declara la variable b globalmente para el programa
print(b)            #  1° se muestra b  --> 500
def foobar():       # se define la funcion  foobar()
    b = 300         # se declara la variable b localmente para la funcion foobar
    print(b)        # se muestra b  3° --> 300
    return b        # se retorna elvalor de b
print(b)            # se muestra b  2° --> 500
foobar()            # se invoca la funcion ...muestra b      --> 300
print(b)            # se muestra b  4° --> 500  // quedando finalmente: 500-  500-   300-  500, 
                    # esto porque esta"b" que se muestra es la variable de afuera la global y no la local
print("sale de la 12")


#13
b = 500             # se declara la variable b globalmente para el programa
print(b)            #  1° se muestra b  --> 500
def foobar():       # se define la funcion  foobar()
    b = 300         # se declara la variable b localmente para la funcion foobar
    print(b)        # se muestra b  3° --> 300
    return b        # se retorna elvalor de b
print(b)            # se muestra b  2° --> 500
b=foobar()          # se modifica el valor de b (global) con el valor de retorno de b local de la f()  b=300
print(b)            # se muestra b  4° --> 500  // quedando finalmente: 500-  500-   300-  300, 
print("sale de la 13")

#14
def foo():          # se define la funcion  foo()
    print(1)        # se muestra 1   1°
    bar()           # se invoca funcion bar()
    print(2)        # # se muestra 2  3°
def bar():          # se define la funcion  foo()
    print(3)        # # se muestra 3  2°
foo()               # inicio-> se invoca a la funcion  foo() quedando 1,3,2
print("sale de la 14")


#15
def foo():          #   se define la funcion  foo()
    print(1)        #   se muestra 1   1°
    x = bar()       #   x adopta el valor de la funcion bar()
    print(x)        #   se muestra x   1°
    return 10       #   retorna 10
def bar():          #   se define la funcion  bar()
    print(3)        #   se muestra 3  1°
    return 5        #   retorna 5
y = foo()           #   y adopta el valor de la funcion foo()
print(y)            #   se muestra y   1°
                    #   quedando -->  1 3 5 10