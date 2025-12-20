"""1. Crea una lista con los números del 1 al 5 e imprímela."""

list = [1, 2, 3, 4, 5]
print(list)

"""2. Accede e imprime el tercer elemento de la lista [10, 20, 
30, 40, 50]. """

newList = [10, 20, 30, 40, 50]
print(newList[2])

"""3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] 
e imprímela."""

list.append(6)
print(list)

"""4. Inserta el número 15 en la posición 2 de la lista [10, 
20, 30, 40, 50]."""

newList.insert(2, 15)
print(newList)

"""5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 
40, 50]."""

newList.remove(30)
print(newList)

"""6. Usa la función pop() para eliminar el último elemento de 
la lista [1, 2, 3, 4, 5] y almacénalo en una variable. 
Imprime la variable y la lista. """

my_pop_list = list.pop()
print(my_pop_list)
print(list)

"""7. Invierte la lista [100, 200, 300, 400, 500] e imprímela. """

other_list = [100, 200, 300, 400, 500]
other_list.reverse()
print(other_list)

"""8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e 
imprímela. """

another_list = [3, 1, 4, 2, 5]
another_list.sort()
print(another_list)

"""9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el 
resultado en una nueva lista. Imprime la lista 
resultante."""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista12 = lista1 + lista2

print(lista12)

"""10. Crea una sublista con los elementos de la lista 
[10, 20, 30, 40, 50] que van desde la posición 1 hasta 
la 3 (sin incluir la posición 3)."""

sub_lista = [10, 20, 30, 40, 50]

print(sub_lista[0:3])

