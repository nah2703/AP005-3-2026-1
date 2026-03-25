print("Bienvenido\n")

categorias = ("Tecnologia", "Hogar", "Ropa", "Alimentos")

productos = []

while True:
    print("\n MENU")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            codigo = int(input("Ingrese el código del producto: "))
        except ValueError:
            print("Error: el código debe ser un número entero")
            continue
        
        if any(p["codigo"] == codigo for p in productos):
            print("Error: ya existe un producto con ese código")
            continue

        nombre = input("Ingrese el nombre del producto: ")

        try:
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
        except ValueError:
            print("Error: precio o cantidad deben ser numéricos")
            continue

        print("Categorías disponibles:", categorias)
        categoria = input("Ingrese la categoría: ")

        if categoria not in categorias:
            print("Error: categoría no válida. Elija una de la lista.")
            continue
    
        if cantidad < 0 or precio < 0:
            print("Error: precio o cantidad inválida")
        else:
            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "categoria": categoria
            }
            productos.append(producto)
            print("Producto agregado correctamente")

    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            print("\nLista de productos:\n")
            for producto in productos:
                print("Código:", producto["codigo"])
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])
                print("Categoría:", producto["categoria"])

    elif opcion == "3":
        try:
            codigo_buscar = int(input("Ingrese el código del producto a buscar: "))
        except ValueError:
            print("Error: el código debe ser un número entero")
            continue

        encontrado = False
        for producto in productos:
            if producto["codigo"] == codigo_buscar:
                print("\nProducto encontrado:")
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])
                print("Categoría:", producto["categoria"])
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado")

    elif opcion == "4":
        try:
            codigo_eliminar = int(input("Ingrese el código del producto a eliminar: "))
        except ValueError:
            print("Error: el código debe ser un número entero")
            continue

        eliminado = False
        for producto in productos:
            if producto["codigo"] == codigo_eliminar:
                productos.remove(producto)
                print("Producto eliminado correctamente")
                eliminado = True
                break

        if not eliminado:
            print("Producto no encontrado")

    elif opcion == "5":
        print("Gracias por usar el sistema.")
        break
    
    else:
        print("Opción inválida, intente nuevamente.")