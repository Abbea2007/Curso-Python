
first_name = "Carlos"
last_name = "Abea"

#Basicamente aqui lo que hago es decalrar dos variables con mi primer nombre y mu primr nombre y las concateno con el print
#Aunque tambien se puede solo separandolos con coma.
print(first_name, last_name)
my_age = 18
print(my_age)

adulto = True
print(adulto)

my_int_variable = 5
print(my_int_variable)

my_int_variable_to_string = str(my_int_variable)
print(my_int_variable_to_string)
print(type(my_int_variable_to_string))

print(len(last_name))

print("Este es mi nombre:", first_name, "Y esta es mi edad: ", my_age)

#Esto es para declarar varias variables en una sola linea aunque no es recomendando para buenas practicas
country, municipio, codigo = "Nicaragua", "Managua", 00

print("El pais en donde estoy es: ", country, "El municipio dond estoy es: ", municipio, "Y el codigo postal es: ", type(str((codigo))))

"""Ahora bien vamos a trabajar con "input", esto lo que hace basicamente es pedir al usuario cosas por ejemplo: """

departamento = input("Cual es el departamento donde vives: ")
print("El departamento donde vive el usuario es: ", departamento, len(departamento))


