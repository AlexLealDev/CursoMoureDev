# Strings

my_string = "Mi String"
my_other_string = 'Mi otra String'
print(len(my_string))
print(len(my_other_string))
print(my_string, my_other_string)
print(my_string + " y " + my_other_string)

my_new_line_string = "Este es un String \ncon un salto de línea"
print(my_new_line_string)
my_tab_string = "\tEste es un String con una tabulación"
print(my_tab_string)
my_scape_string = "\tEste es un String \nescapado"
print(my_scape_string)

# Formateo
name, surname, age = "Alex", "Leal", 34
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # Esta opción lo pasa todo a string
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))  # Esta opción mantiene el formato original
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # Esto es una inferencia de datos. Es la mejor forma.

# Desempaquetado de carácteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
language_slice = language[0:6]
print(language_slice)

language_slice = language[1:]  # Imprime todo menos la primera
print(language_slice)

language_slice = language[-2]  # Imprime la segunda por el final
print(language_slice)

language_slice = language[0:6:2]  # Evita carácteres dentro del rango
print(language_slice)

# Reverse
revesed_language = language[::-1]
print(revesed_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.isnumeric())
print(language.upper().isupper)  # Comprueba si está en mayúsculas
print(language.lower().isupper)
print(language.startswith("py"))
