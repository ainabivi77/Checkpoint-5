# 1.Cree un bucle For de Python.

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# 2.Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(tienda, almacén, devolución):
    return tienda + almacén + devolución

resultado = suma(20, 25, 5)
print(resultado)

# 3.Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma_lambda = lambda tienda, almacen, devolucion: tienda + almacen + devolucion
resultado = suma_lambda(20, 25, 5)
print(resultado)

# 4.Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

# Verificar si el valor de nombre está en lista_nombre
if nombre in lista_nombre:
    print(f"El nombre '{nombre}' está en la lista.")
else:
    print(f"El nombre '{nombre}' no está en la lista.")
