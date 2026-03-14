# Titulo: Historia-de-usuario
## Descripcion:
Este codigo solicita al usuario información de un producto,
 valida los datos ingresados, calcula el costo total y muestra
 el resultado

 ### Como funciona:

1. l programa inicia y solicita al usuario el nombre del producto usando input().
2. Luego pide el precio y usa float() para convertirlo a número decimal. Si el dato es inválido, muestra un error y lo vuelve a pedir.
3. Después solicita la cantidad y usa int() para convertirla a número entero, también validando que el dato sea correcto.
4. Cuando los datos son válidos, el programa calcula el costo total multiplicando precio * cantidad.
5. Finalmente, muestra en la consola un resumen del producto con el nombre, precio, cantidad y el total calculado.
# Resultados

 Solicitar el nombre del producto

nombre = input("Ingrese el nombre del producto: ")


Solicitar y validar el precio
Se usa un bucle para asegurar que el valor ingresado sea numérico

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

 Solicitar y validar la cantidad
 Se usa un bucle para asegurar que el valor ingresado sea un número entero

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")


Operación matemática
Calcular el costo total del producto

costo_total = precio * cantidad


 Mostrar resultados en consola

print("\nResumen del producto registrado:")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")



