### Strings ###

my_string = 'Hola'
myOtherString = 'Mi otro hola'

print(len(my_string))
print(len(myOtherString))

print(my_string, myOtherString)

myNewLineString = "Este es un string con\nsalto de linea"
print(myNewLineString)

myTabString = "\tEste es un string con tabulación"
print(myTabString)

### Formateo ###

name, lastName, age = "Carlos", "Abea", 18

print("My nombre es %s %s y mi edad es %d" %(name, lastName, age))
print("My Nombre es {} {} y mi edad es {}".format(name, lastName, age))
print(f"Mi nombre es {name} {lastName} y mi edad es {age}")


### Desempaquetado de caracteres ###
language = 'python'
a, b, c, d, e, e = language

print(a)
print(e)

### Division ###

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())

print("Python".lower() == "python")

