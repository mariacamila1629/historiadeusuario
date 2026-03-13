# declaracion de variables
nombre = ""
precio = 0.0
cantidad = 0 
# solicitar nombre del producto
nombre = input ("ingrese el nombre del producto: ")
# validar precio
while True:   
    try:
        precio= float (input("ingrese el precio del producto: "))
        break 
    except ValueError:
         print("valor invalido, por favor ingrese un numero valido para el precio")
#validar cantidad
while True:
    try:
        cantidad=int(input("ingrese la cantidad del producto:  "))
        break
    except ValueError:
        print("valorinvalido, favor ingresar un numero entreo para la cantidad")
# Mostrar resultado
print("\nProducto registrado correctamenyte")
print("nombre:", nombre)
print("precio:", precio)
print("cantidad", cantidad)


