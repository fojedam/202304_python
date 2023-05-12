first_name = "Zen"
last_name = "Coder"
age = 27
print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")
first_name = "Zen"
last_name = "Coder"
age = 27
print("Mi nombre es {} {} y tengo {} años de edad.".format(first_name, last_name, age))
# salida: Mi nombres es Zen Coder y tengo 27 años de edad.
print("Mi nombre es {} {} y tengo {} años de edad.".format(age, first_name, last_name))
# salida: Mi nombre es 27 Zen y tengo Coder años de edad.
"""
hw = "Hola %s" % "mundo" 	# con valores literales
py = Me encanta Python %d " % 3 
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# salida: Mi nombre es Zen y tengo 27
"""
x = "hola mundo"
print(x.title())
# salida:
r="HOlOafggGGGggola Mundo"
lista =[ "sdfsdf","ttttt","rrrr","iiii","ppppp"]
#p= string.join(lista)
rr="HLA"
print(r.upper())
print(r.lower())
#  print(r.count(substring)) preguntar
print(r.isalpha())
if rr.isupper():
    print("Es upper ")
else: 
    print(" noes upper")
    

frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
print("ENUMERATE")
ttt= (enumerate(frutas_y_vegetales))
print(ttt)
      
ensalada = 3 * vegetales
print(ensalada)
x = [99,4,2,5,-3]
print(x[:])
print(x)                    #  ESTO ES IMPORTANTE....
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])
# la salida sería [99,4,2,5]
print(x[2:4])
# la salida sería [2,5]