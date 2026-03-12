#inventario en python 

#solcitar nombre del producto
producto = input("Ingrese el nombre del prodcuto: ")

#validar el precio del producto
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except:
        print("Error: debe ingresar un número valido.")

#validar cantidad del producto
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except:
        print("Error: ingrese un número valido.") 

#calcular el costo
costo_total = precio * cantidad

#resumen del producto 
print("\n===== RESUMEN DEL PRODUCTO =====")
print(f"producto: {producto}")
print(f"precio: {precio}")
print(f"cantidad: {cantidad}")
print(f"total: {costo_total}")

#comentario general:

# mediante este programa de invetario se le pide al usuario el nombre del producto,
# precio del prodcuto y la cantidad. Lo que hace el sistema es validar el precio y 
# la cantidad, pero que sean valores correctos por medio del int y float. Despues de
# validar los datos, procede a calcular el costo total mediante un operación donde se
# multiplica el precio por la cantidad, para finalmente arrojar un resumen con toda la información.