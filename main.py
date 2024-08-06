import json #se importa la libreria de json ya que se trabaja con archivos json
from os import system  #se importa system de la libreria os para limpiar pantalla
from datetime import date #se importa date de la libreria datetime para poder saber la fecha del registro

with open("./productos.json", encoding="utf-8") as files:#con esto se abre el archivo de productos.json que es donde esta toda la de los productos
    Productos=json.load(files)
with open("./ventas.json", encoding="utf-8") as files:#con esto se abre el archivo de ventas.json que es donde se guarda el registro de las ventas
    Ventas=json.load(files)
bol=True #variable para cancelar el loop de while

while bol==True: #se usa un loop while para que se repita el menu y sus opciones a menos de que escoja la opcion 4

    opcion=int(input("-----Menu-----\n1. Registrar una venta\n2. Registrar compra de Proovedor\n3. Ver informes\n4. Salir\n"))

    if opcion==1:
        fechaVenta=date.today() #se usa el date.today() para saber la fecha del registro
        fecha=fechaVenta.isoformat()#como los objetos de tipo "date" no son serializables con los arcivos json de usa el .isoformat() para devolver en forma de cadena el objeto "date"
        nombreCliente=input("Ingresa el nombre del cliente\n")
        direccionCliente=input("Ingresa la direccion del cliente\n")
        nombreEmpleado=input("Ingresa el nombre del empleado que realizo la venta\n")
        nombreEmpleado=input("Ingresa el cargo del empleado que realizo la venta\n")
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
        cantidadProductoV=int(input("Ingresa la cantidad que deseas coprar del producto\n"))
    
        for i in Productos[seccionProducto]:
            if i["id"]==idProductoV:
                productoventa={"nombre":i["nombre"],"cantidad":cantidadProductoV,"precio":i["precio"]}
    
        Ventas["Historial de ventas"].append({"fecha":fecha,"nombre_cliente":nombreCliente,"direccion_cliente":direccionCliente,"nombre_empleado":nombreEmpleado,"producto":productoventa})#se agregan todos los datos solicitados anteriormente al json de ventas
        print("Venta realizada con exito 😀")
        bol=False
    elif opcion==4:
        print("hola")
        bol=False

jsonventas=json.dumps(Ventas)
with open("./ventas.json","w") as fil:
    fil.write(jsonventas)

jsonProductos=json.dumps(Productos)
with open("./productos.json","w") as files:
    files.write(jsonProductos)

