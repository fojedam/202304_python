class Usuario:		
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):  # toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	

guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael
guido.name = "Guido"
print(guido.name) # salida: Guido
print(guido.nombre_banco ) 
monty.name = "Monty"
print(monty.nombre_banco ) 
monty.name = "Monty"
print(monty.name)

#CAMBIANDO DATOS por instancia
guido.nombre_banco = "Dojo Credit Union"
print(guido.nombre_banco) # salida: Dojo Credit Union 
print(monty.nombre_banco) # salida: Primer Dojo Nacional


#CAMBIANDO TODOS LOS DATOS 
Usuario.nombre_banco = "Banco del Dojo"
print(f"guido", guido.nombre_banco) # salida: Banco del Dojo
print(f"monty", monty.nombre_banco) # salida: Banco del Dojo
print(f"guido", guido.nombre_banco) # salida: Banco del Dojo
print(f"monty", monty.nombre_banco) # salida: Banco del Dojo

###################

    # los atributos de clase se definen en la clase   
    # ¡ahora nuestro método tiene 2 parámetros!

#guidos = Usuario("Guido van Rossum", "guido@python.com")
#montys = Usuario("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Pythonx

guido.hacer_depósito(100)
guido.hacer_depósito(200)
monty.hacer_depósito(50)
monty.hacer_depósito(1000)
print(guido.balance_cuenta)	# salida: 300
print(monty.balance_cuenta)	# salida: 50