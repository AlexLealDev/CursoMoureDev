# Variables
my_string_variable = "Esta es una variable de tipo string"
print(my_string_variable)
my_int_variable = 5
print(my_int_variable)
my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables
print(my_string_variable, my_int_variable, my_bool_variable)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  # te devuelve el tipo de la variable
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))  # te devuelve la longitud de una variable

# Variables en una sola línea
name, surname, age = "Alejandro", "Leal", 34
print("Mi nombre es", name, surname, "y tengo", age, "años")

# Inputs
nombre = input("¿Como te llamas?: ")
edad = input("¿Cuantos años tienes?: ")
print(nombre)
print(edad)