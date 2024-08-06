import json #se importa la libreria de json ya que se trabaja con archivos json
from os import system  #se importa system de la libreria os para limpiar pantalla
from datetime import date #se importa date de la libreria datetime para poder saber la fecha del registro

with open("./productos.json", encoding="utf-8") as files:#con esto se abre el archivo de productos.json que es donde esta toda la de los productos
    Productos=json.load(files)
with open("./ventas.json", encoding="utf-8") as files:#con esto se abre el archivo de ventas.json que es donde se guarda el registro de las ventas
    Ventas=json.load(files)
with open("./compras.json", encoding="utf-8") as files:#con esto se abre el archivo de compras.json que es donde se guarda el registro de las ventas
    Compras=json.load(files)
bol=True #variable para cancelar el loop de while

while bol==True: #se usa un loop while para que se repita el menu y sus opciones a menos de que escoja la opcion 4

    system("clear")
    opcion=int(input("-----Menu-----\n1. Registrar una venta\n2. Registrar compra de Proveedor\n3. Ver informes\n4. Salir\nSelecciona un opcion\n"))
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
        for i in Productos["panaderia"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de panaderia del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----pasteleria-----")
        for i in Productos["pasteleria"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de pasteleria del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----bebidas-----")
        for i in Productos["bebidas"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de bebidas del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----apartado de promociones-----")
        for i in Productos["apartado de promociones"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de apartadp de promociones del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        seccionProducto=input("Ingresa la secion de donde es el producto. Ejemplo: panaderia\n")
        idProductoV=int(input("Ingresa el ID del producto que deseas vender\n"))
        system("clear")
        cantidadProductoV=int(input("Ingresa la cantidad que deseas vender del producto\n"))
    
        for i in Productos[seccionProducto]:#basandose en la seccion de productos indicados por el usuario y el id del productose usa unbucle for para bucar que producto tiene ese id y esta en esa seccion
            if i["id"]==idProductoV:
                productoventa={"nombre":i["nombre"],"cantidad":cantidadProductoV,"precio":i["precio"]}#despues de encontrar el producto agrega al diccionario producto venta el nombre y precio de ese producto ademas de la cantidad indicada previamente por el usuario
    
        Ventas["Historial de ventas"].append({"fecha":fecha,"nombre_cliente":nombreCliente,"direccion_cliente":direccionCliente,"nombre_empleado":nombreEmpleado,"cargo_empleado":cargoEmpleado,"producto":productoventa})#se agregan todos los datos solicitados anteriormente al json ventas.json en la seccion de Historial de ventas

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
        print("----------Productos----------")
        print("-----panaderia-----")
        for i in Productos["panaderia"]: #se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de panaderia del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----pasteleria-----")
        for i in Productos["pasteleria"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de pasteleria del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])

        print("-----bebidas-----")
        for i in Productos["bebidas"]:#se usa un bucle for para mostrar todos los productos que se encuentran en la seccion de bebidas del json "productos.json"
            print("ID:",i["id"],"-----",i["nombre"],"      $",i["precio"])
        seccionProducto=input("Ingresa la secion de donde es el producto. Ejemplo: panaderia\n")
        idProductoC=int(input("Ingresa el ID del producto que deseas comprar\n"))
        system("clear")
        cantidadProductoC=int(input("Ingresa la cantidad que deseas comprar del producto\n"))
    
        for i in Productos[seccionProducto]:#basandose en la seccion de productos indicados por el usuario y el id del productose usa unbucle for para bucar que producto tiene ese id y esta en esa seccion
            if i["id"]==idProductoC:#despues de encontrar el producto agrega al diccionario producto venta el nombre y cantidad indicada previamente por el usuario
                productoCompra={"Nombre":i["nombre"],"Cantidad":cantidadProductoC}
        precioProductoC=int(input("Ingresa el precio del producto comprado\n"))
        system("clear")
        proveedor={"Nombre":nombreProveedor,"Contacto":contactoProveedor}

        Compras["Historial de compras"].append({"fecha":fechaCompra,"Proveedor":proveedor,"Producto comprado":productoCompra,"Precio":precioProductoC})#se agregan los datos solicitados al json compras.json en la seccion historial de compras

        system("clear")
        print("Compra realizada con exito 😀")
        input("Preciona Enter para continuar\n")

    elif opcion==3:
        opcionVista=int(input("-----Informes-----\n1. Informes de ventas\n2. Informes de compras\n¿Que informa quieres ver?\n"))
        if opcionVista==1:
            system("clear")
            print("Historial de ventas")
            for i in Ventas["Historial de ventas"]:#se usa un loop for para recorrer el json ventas.json en la seccion de "Historial de ventas" y mostrar el historial con la fecha, nombre del producto, cantidad vendida y el total de la venta
                print("Fecha de la venta:",i["fecha"],"\nProducto Vendido:",i["producto"]["nombre"],"\nCantidad Vendida:",i["producto"]["cantidad"],"\nTotal:",(i["producto"]["cantidad"]*i["producto"]["precio"]))
                print("---------------------------------")
        elif opcionVista==2:
            system("clear")
            print("--------HIstorial de compras--------")
            for i in Compras["Historial de compras"]:#se usa un loop for para recorrer el json compras.json en la seccion "Historial de compras" y mostrar el historial con los siguientes datos: nombre del proveedor, producto comprado y cantidad
                print("Proveedor:",i["Proveedor"]["Nombre"],"\nProducto Comprado:",i["Producto comprado"]["Nombre"],"\nCantidad:",i["Producto comprado"]["Cantidad"])
                print("---------------------------------")
        input("Precione Enter para continuar")
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

#Desarrollado por Luis Orlando Henao Bermon 