""" Crear un archivo Python que se llame bucle_for_básico1.py que realice las siguientes tareas."""

# 1)  Básico: imprime todos los números enteros del 0 al 150.
# 2)  Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
# 3)  Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar.
#    Si es divisible por 10, imprime "Coding Dojo".
# 4)  Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
# 5)  Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
# 6)  Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). """

#######  ----> 1 <---------########

for w in range(151):
    print(f"el valor es : {w} ")

#######  ----> 2 <---------########
for w in range(5, 1001, 5):
    print(w)


#######  ----> 3 <---------########
for w in range(1, 101):
    if (w % 10) == 0:
        print("Coding Dojo")
    elif (w % 5) == 0:
        print("Coding")
    else:
        print(w)

#######  ----> 4 <---------######
# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.#
sumafinal =0
for w in range(0, 500000, 2):
    sumafinal = sumafinal + w
print(f"la suma de todos los numeros es : {sumafinal}")

#######  ----> 5 <---------######
#  Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.##
for w in range(2018,0,-4):
    print(w)

#######  ----> 6 <---------######
# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum,
# imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
# El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).#

lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum,highNum+1):
    if (num % mult == 0):
        print(f"{num} es multiplo de : {mult}")

