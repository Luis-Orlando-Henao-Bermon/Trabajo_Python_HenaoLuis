import json #se importa la libreria de json ya que se trabaja con archivos json
from os import system  #se importa system de la libreria os para limpiar pantalla
from datetime import date #se importa date de la libreria datetime para poder saber la fecha del registro

with open("./productos.json", encoding="utf-8") as files:#con esto se abre el archivo de productos.json que es donde esta toda la de los productos
    Productos=json.load(files)
with open("./ventas.json", encoding="utf-8") as files:#con esto se abre el archivo de ventas.json que es donde se guarda el registro de las ventas
    Ventas=json.load(files)
with open("./compras.json", encoding="utf-8") as files:#con esto se abre el archivo de ventas.json que es donde se guarda el registro de las ventas
    Compras=json.load(files)
bol=True #variable para cancelar el loop de while

while bol==True: #se usa un loop while para que se repita el menu y sus opciones a menos de que escoja la opcion 4

    system("clear")
    opcion=int(input("-----Menu-----\n1. Registrar una venta\n2. Registrar compra de Proveedor\n3. Ver informes\n4. Salir\n"))
    system("clear")
    if opcion==1:
        fechaVenta=date.today() #se usa el date.today() para saber la fecha del registro
        fecha=fechaVenta.isoformat()#como los objetos de tipo "date" no son serializables con los arcivos json de usa el .isoformat() para devolver en forma de cadena el objeto "date"
        nombreCliente=input("Ingresa el nombre del cliente\n")
        system("clear")
        direccionCliente=input("Ingresa la direccion del cliente\n")
        system("clear")
        nombreEmpleado=input("Ingresa el nombre del empleado que realizo la venta\n")
        system("clear")
        cargoEmpleado=input("Ingresa el cargo del empleado que realizo la venta\n")
        system("clear")
        print("----------Productos----------")
        print("-----panaderia-----")
        for i in Productos["panaderia"]:
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----pasteleria-----")
        for i in Productos["pasteleria"]:
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----bebidas-----")
        for i in Productos["bebidas"]:
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----apartado de promociones-----")
        for i in Productos["apartado de promociones"]:
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        seccionProducto=input("Ingresa la secion de donde es el producto. Ejemplo: panaderia\n")
        idProductoV=int(input("Ingresa el ID del producto que deseas comprar\n"))
        system("clear")
        cantidadProductoV=int(input("Ingresa la cantidad que deseas comprar del producto\n"))
    
        for i in Productos[seccionProducto]:
            if i["id"]==idProductoV:
                productoventa={"nombre":i["nombre"],"cantidad":cantidadProductoV,"precio":i["precio"]}
    
        Ventas["Historial de ventas"].append({"fecha":fecha,"nombre_cliente":nombreCliente,"direccion_cliente":direccionCliente,"nombre_empleado":nombreEmpleado,"cargo_empleado":cargoEmpleado,"producto":productoventa})#se agregan todos los datos solicitados anteriormente al json de ventas
        system("clear")
        print("Venta realizada con exito 😀")
        input("Preciona cualquier tecla para continuar\n")
    elif opcion==2:
        fechaCompra=date.today() #se usa el date.today() para saber la fecha del registro
        fecha=fechaCompra.isoformat()#como los objetos de tipo "date" no son serializables con los arcivos json de usa el .isoformat() para devolver en forma de cadena el objeto "date"
        nombreProveedor=input("Ingresa el nombre del proveedor\n")
        system("clear")
        contactoProveedor=input("Ingresa el numero de contacto del proveedor\n")
        system("clear")
        nombreProductoC=input("Ingresa el nombre del producto comprado\n")
        system("clear")
        cantidadProductoC=input("Ingresa la cantidad del producto comprado\n")
        system("clear")
        precioProductoC=int(input("Ingresa el precio del producto comprado\n"))
        system("clear")
        proveedor={"Nombre":nombreProveedor,"Contacto":contactoProveedor}
        productoComprado={"Nombre":nombreProductoC,"Cantidad":cantidadProductoC,"Precio":precioProductoC}
        Compras["Historial de compras"].append({"Proveedor":proveedor,"Producto comprado":productoComprado})
        system("clear")
        print("Compra realizada con exito 😀")
        input("Preciona cualquier tecla para continuar\n")

    elif opcion==3:
        ""
    elif opcion==4:
        bol=False

jsonventas=json.dumps(Ventas)
with open("./ventas.json","w") as fil:
    fil.write(jsonventas)

jsonProductos=json.dumps(Productos)
with open("./productos.json","w") as files:
    files.write(jsonProductos)

jsonCompras=json.dumps(Compras)
with open("./compras.json","w") as files:
    files.write(jsonCompras)
