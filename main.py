import json
from os import system 
from datetime import date
#hola =date.today()

with open("./productos.json", encoding="utf-8") as files:#con esto se abre el archivo de productos.json que es donde esta toda la de los productos
    Productos=json.load(files)
with open("./ventas.json", encoding="utf-8") as files:#con esto se abre el archivo de productos.json que es donde esta toda la de los productos
    Ventas=json.load(files)

bol=True

while bol==True:
    opcion=int(input("-----Menu-----\n1. Registrar una venta\n2. Registrar compra de Proovedor\n3. Ver informes\n4. Salir\n"))
    if opcion==1:
        fechaVenta=date.today()
        nombreCliente=input("Ingresa el nombre del cliente")
        direccionCliente=input("Ingresa la direccion del cliente")
        nombreEmpleado=input("Ingresa el nombre del empleado que realizo la venta")
        nombreEmpleado=input("Ingresa el cargo del empleado que realizo la venta")
        #print(productos)
        idProductoV=int(input("Ingresa el ID del producto que deseas comprar"))
        cantidadProductoV=int(input("Ingresa la cantidad que deseas coprar del producto"))
        Ventas.append({"Fecha":fechaVenta,"nombre_cliente":nombreCliente,"direccion_cliente":direccionCliente,"nombre_empleado":nombreEmpleado,"id_producto":idProductoV,"cantidad_producto":cantidadProductoV})
        bol=False
    elif opcion==4:
        print("hola")
        bol=False

jsonProductos=json.dumps(Productos)
with open("./productos.json","w") as files:
    files.write(jsonProductos)
jsonventas=json.dumps(Ventas)
with open("./ventas.json","w") as files:
    files.write(jsonventas)