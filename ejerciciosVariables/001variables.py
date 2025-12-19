"""
Declara y asigna valores a las siguientes variables: 
name: una cadena que contenga tu nombre. 
age: un número entero que represente tu edad. 
height: un número flotante que represente tu altura. 
Imprime cada variable en una línea separada.
"""

name = "Carlos Alfredo Abea Martinez"
age = 18
height = 1.80

print(name)
print(age)
print(height)

"""
2. Convierte la variable edad de entero a cadena y 
concatenala con un texto que diga cuántos años tienes.
"""
age_to_string = str(age)
print("Yo tengo: ", age_to_string)

"""
3. Declara una variable booleana is_student que indique si 
eres estudiante o no. Usa True o False según corresponda 
e imprímela. 
"""

is_student = True
print("Eres estudiante?: ", is_student)

"""
4. Usa la función len() para calcular cuántos caracteres 
tiene tu nombre completo, almacenado en una variable. 
"""

print(len(name))

"""
 5. Declara tres variables en una sola línea que representen 
tu nombre, apellido y ciudad de origen. Luego, imprime 
estos valores. 
"""

name, last_name, ciudad_origen = "Abea", "Alfredo", "Managua"
print("My name is: ", name, "and my last name is: ", last_name, ciudad_origen)

"""
 6. Usa la función input() para solicitar al usuario su 
color favorito y almacénalo en una variable color. 
Luego, imprime el valor ingresado.
"""

#color_fav = input("What is your favorite color?: ")
#print("El color favorito del usuario es: ", color_fav)

"""7. Declara una variable fruit e inicialízala con un valor. 
Luego, cambia el valor de la fruta a otro diferente y 
vuelve a imprimirla. """

fruit = "Naranja"
#fruit = "Pera"
print(fruit)

"""8. Convierte un número decimal, almacenado en la variable 
price, a un número entero y luego imprímelo.
"""

price = 198.90
print(type(price))

price_to_float = int(price)
print(type(price_to_float))

""" 9. Declara una variable llamada address_len y almacena en 
ella la cantidad de caracteres de una dirección usando 
la función len(). Imprime el resultado. """

address_len = len("Americas2 Del Colegio las Americas una cuadra al lago")
print(address_len)

"""10. Usa un tipo de dato forzado para declarar una 
variable phone, asegurándote de que siempre será un 
número. Luego, cambia su valor a un número diferente y 
verifica el tipo de la variable con type(). 
"""
#Aclaracio, como estamod forzando a usarla en int, si la queremos cambiar despues a string , no vamos a poder porque esta forzanda a int
phone: int = 50577440592
print(phone)

phone_to_string = str(phone)
print(type(phone))


