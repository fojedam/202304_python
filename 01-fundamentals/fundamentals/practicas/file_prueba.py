num1 = 42               #- variable declaration num1, integer
num2 = 2.3              #- variable declaration num2, float
string = 'Hello World'  #- variable declaration string, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- inicializacion de lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- inicialización de diccionario
fruit = ('blueberry', 'strawberry', 'banana')   #- inicialización de tuplas
print(pizza_toppings[1])                        # - accesa e imprime (muestra) desde la lista pizza_topping
pizza_toppings.append('Mushrooms')              # agrega un elemento a la lista
print(person['name'])                           #muestra por pantalla del Diccionario el nombre, apareciendo  John
person['name'] = 'George'                       #cambia el valor de nombre, que era John por George

person['eye_color'] = 'blue'        # agrega en el diccionario un campo eye_color y un valor "blue"
print(person['eye_color'])          # agrega en el diccionario un campo eye_color y un valor "blue"

print(fruit[2])                     # muestra el cvalor de la lista parala posicion 3 (parte del 0)

if num1 > 45:       #condicional SI, si valor de num1 (42) es mayor que 45, imprimira "It's greater"
    print("It's greater")
else:               #condicional else: de lo contrario imprimirá  "It's lower"
    print("It's lower")
print (len(string)) #muestra el largo de string
if len(string) < 5:  # - length check, permite saber el largo de la palabra 'Hello World'  que es 11
    print("It's  short word!")  #condicional SI, si valor 11<5 (false) no muetra  "It's  short word!"
    print("It's a long word!") #condicional SI, si valor 11<5 (false) no muetra  "It's a long word!""
else:
    print("Just right!")# condicional que cumple la condicion else, porque 11 es mayor que 5


for x in range(5):      # for loop, adopta pra el valor de x : 0,1,2,3,4   el 5 se excluye
    print(x)            # muestra los valores del 0 hasta el 4
print("desde aca")

for x in range(2,5):    # for loop, 
    print(x)            # muestra los valores del 2 hasta el 4   2,3,4
for x in range(2,10,3): # for loop, parte del 2, terminando en el 9, con un step (salto) de 3 en 3)
    print(x)            # muestra  2,5,8
x = 0
while(x < 5):           # while loop itera mientras se cumpla la condicion x < 5 , donde x se declara como entero con valor 0
    print(x)            # muestra el valor de x, mostrando 0,1,2,3,4
    x += 1              # suma a la variable "x" una unidad


pizza_toppings.pop()    # delete value - elimina el ultimo registro de la lista, 

pizza_toppings.pop(1)   # delete value - elimina el registro con el indice (1) de la lista, es decir el segundo registro 


print(person)           # muestra por pantalla del Diccionario "person", en forma completa
person.pop('eye_color') # delete value elimina del diccionario el utimo 
print(person)           # muestra por pantalla del Diccionario "person", en forma completa ("sin Eye_color")

for topping in pizza_toppings:  #para la nueva variable topping recorre pizza_toppings
    if topping == 'Pepperoni':
        continue                    # contunua con el bucle de repeticion
    print('After 1st if statement') # muestra mensaje sin considerar la sentencia IF, porque está fuera de la indentación
    if topping == 'Olives':         # cumple el la cuarta iteracion
        break                       # sale del bucle, forzado por el break



def print_hello_ten_times(): # declare function print_hello_ten_times y no recibe y envía nada
    for num in range(10):   # for loop, donde num recorre de 0,1,2,3,4,5,6,7,8,9
        print('Hello')      #muestra por pantalla palabra hello 10 veces cuando sea llamada la funcion

print_hello_ten_times()     # se llama  a la funcion , la cual imprime 10 vese "Hello"


def print_hello_x_times(x): # declare function print_hello_x_times y  recibe un parametro y envía nada

    for num in range(x):        # num adopta de 0 hasta X-1
        print('hello')          # 

print_hello_x_times(4)          # invoca a la funcio con un valor 4, lo que hará que imprima en la funcion 4 vese "hello"

def print_hello_x_or_ten_times(x = 10): # definie una funcion "x o 10" define un valor por defecto que es 10, 
                                        # si invoca con valor(4) aplica x=4
    for num in range(x):        # num adopta de 0 hasta X-1 siendo x=4 o x=10
        print('Hello')

print_hello_x_or_ten_times()    # invoca la funcion sin valor, asumirá 10
print_hello_x_or_ten_times(4)   # invoca la funcion con valor, asumirá 4


"""
Bonus section
"""

# print(num3) # error de compilación, esto porque no se ha declarado num3
# num3 = 72   # se asigna a num3 el 72 (integer)

# fruit[0] = 'cranberry' # se intenta cambial la tupla, pero éstas son inmutables, no cambian
# print(person['favorite_team']) # se intenta mosrtra el valor del diccionario que no existe, implica error
# print(pizza_toppings[7]) ## no puede mustrar un valor porque el indice esta fuera de rango, si tuvieramos 8 registros si
# print(boolean)            # no pude represent a #¡"boolean", lo considera una variable no definida
# fruit.append('raspberry') # es una tupla, por lo tando es inmutable

# fruit.pop (1)            # es una tupla, por lo tando es inmutable


