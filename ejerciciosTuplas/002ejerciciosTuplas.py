"""1. Crea una tupla con los valores (10, 20, 30, 40, 50) e 
imprímela. """

my_tuple = (0, 20, 30, 40, 50)
print(my_tuple)

"""2. Accede al segundo elemento de la tupla (100, 200, 300, 
400, 500) y muéstralo. """

print(my_tuple[2])

"""3. Intenta modificar el primer elemento de la tupla (1, 2, 
3) a 10 y observa el resultado."""

other_tuple = (1, 2, 3)
#other_tuple[0] = 10 #TypeError: 'tuple' object does not support item assignment

"""4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 
2, 3, 3, 4, 5, 3)."""

tuple1 = (1, 2, 3, 3, 4, 5, 3)
print(tuple1.count(3))

"""5. Encuentra el índice de la primera aparición de la cadena 
"Python" en la tupla ("Java", "Python", "JavaScript", 
"Python"). """

string_tupla = ("Java", "Python", "JavaScript", "Python")

print(string_tupla.index("Python"))


"""6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la 
tupla resultante. """

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

newTuple = tupla1 + tupla2
print(newTuple)

"""7. Crea una subtupla con los elementos desde la posición 2 
hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 
40, 50). """


another_tuple = (10, 20, 30, 
40, 50)

print(another_tuple[0:4])

"""8. Convierte la tupla ("rojo", "verde", "azul") en una 
lista, cambia el segundo elemento a "amarillo" y vuelve 
a convertirla en una tupla. Imprime la tupla resultante."""

colores = ("rojo", "Verde", "azul")

list_colores = list(colores)

list_colores[2] = "amarillo"

print(list_colores)

"""9. Elimina una tupla llamada my_tuple usando del y luego 
intenta imprimirla para ver el resultado."""

#del my_tuple #name 'my_tuple' is not defined
#print(my_tuple)

"""10. Crea una tupla con un solo elemento (el número 100) 
e imprímela. Asegúrate de usar la sintaxis correcta para 
crear una tupla con un solo elemento."""

just_one = (100, )
print(just_one)