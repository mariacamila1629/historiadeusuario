# declaracion de variables
# Programa: inventario.py
# Este programa solicita al usuario información de un producto,
# valida los datos ingresados, calcula el costo total y muestra
# el resultado en pantalla.


# Solicitar el nombre del producto

nombre = input("Ingrese el nombre del producto: ")


# Solicitar y validar el precio
# Se usa un bucle para asegurar que el valor ingresado sea numérico

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")


# Solicitar y validar la cantidad
# Se usa un bucle para asegurar que el valor ingresado sea un número entero

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")


# Operación matemática
# Calcular el costo total del producto

costo_total = precio * cantidad


# Mostrar resultados en consola 

print("\nResumen del producto registrado:")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


# Comentario final:
# Este programa permite registrar un producto en un inventario.
# Primero solicita al usuario el nombre, precio y cantidad.
# Luego valida que precio y cantidad sean números válidos.
# Después calcula el costo total multiplicando precio por cantidad.
# Finalmente muestra toda la información del producto en la consola.
