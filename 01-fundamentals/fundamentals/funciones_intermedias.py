""" 1. Actualiza valores en diccionarios y listas 


2) Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
3) En el directorio_deportes, cambia "Messi" por "Andrés".
4) Cambia el valor 20 en z a 30.                                          """


x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#   1) Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#   2) Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

def cambia_apellido(nombre,i):
    estudiante=estudiantes[i]
    estudiante["last_name"]=nombre

cambia_apellido('Bryant',0)
print (estudiantes)

#   3) En el directorio_deportes, cambia "Messi" por "Andrés".
def cambia_jugador(nombre, deporte):
    #for deporte in directorio_deportes:
     #   if deporte = directorio_deportes.key:
    # for depo in directorio_deportes:
    # for
    pass

cambia_jugador("messi", "futbol")