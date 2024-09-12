import json

#defino una funcion para cargar el inventario
def load_inv():
    with open('inventario.json','r') as file:
        return json.load(file)

#defino una funcion para guardar el inventario    
def save_inv(inv):
    with open('inventario.json','w') as file:
        json.dump(inv, file, indent=4)

#defino una funcion para crear un diccionario
def crear_dict(product, precio, stock):
    diccionario={"producto":product, "precio":precio, "stock":stock}   
    return diccionario

#main
data=load_inv()

print('---Gestion de Inventario---')
print('1. Crear Producto')
print('2. Mostrar todos los productos')
print('3. Mostrar informacion de un producto')
print('4. Actualizar Producto')
print('5. Eliminar Producto')
print('6. Salir')
print(' ')
user_text=int(input('Elige una opcion: '))

#defino una variable booleana que me ayude a salir del ciclo while a conveniencia
continuar_ejecutando=True

while continuar_ejecutando:
    
    if user_text<1 or user_text>6:
        user_text=int(input('No se encuentra esa opcion, por favor elige una opcion entre las mencionadas: '))
        
    elif user_text==1:
        #creo una lista vacia y un diccionario acorde a esa lista, la lista me servirá para agregar los datos del archivo json
        # y poder modificarlos desde ahí
        data_py=[]
        data_dict={"inventario":data_py}
        for i in data["inventario"]:
            data_py.append(i)
        agregar_nombre=input('ingrese un nombre para el producto: ').lower()
        for productos in data_py:
            while agregar_nombre==productos['producto']:
                print('El producto ya existe!!')
                agregar_nombre=input('Ingrese un nombre que no este en la lista: ').lower()
        while type(agregar_nombre)!=str or agregar_nombre.isnumeric():
            agregar_nombre=input('el nombre del producto debe ser de tipo "str": ').lower()
        agregar_precio=(input('ingrese un precio para el producto: '))
        while not agregar_precio.isnumeric():
            agregar_precio=(input('por favor ingrese un valor numerico: '))
        agregar_precio=int(agregar_precio)
        agregar_stock=(input('ingrese la cantidad del producto a agregar: '))
        while not agregar_stock.isnumeric():
            agregar_stock=(input('por favor ingrese un valor numerico'))
        agregar_stock=int(agregar_stock)
        #creo el diccionario con los datos creados llamando a la funcion
        entrada=crear_dict(agregar_nombre,agregar_precio,agregar_stock)
        #agrego el nuevo diccionario a la lista previamente mencionada
        data_py.append(entrada)
        #llamo a la funcion de guardado con el diccionario asignado a la lista
        save_inv(data_dict)
        print('Producto agregado exitosamente!!')
        break
    elif user_text==2:
        #uso mi variable para detener el bucle para que solo itere sobre el inventario una vez
        continuar_ejecutando=False
        for productos in data["inventario"]:
            print( )
            print("producto: ", productos["producto"])
            print('precio: ', productos["precio"])
            print('stock: ', productos["stock"])
    elif user_text==3:
        continuar_ejecutando=False
        data_py=[]
        #creo una nueva lista donde solo se va a agregar el producto especificado que se va a mostrar
        data_final=[]
        for i in data["inventario"]:
            data_py.append(i)
        producto_especifico=input('Escriba el nombre del producto a buscar: ').lower()
        #creo una variable booleana ya que solo usando el if y else haria que el programa solo evalue el primer dato y si no es el que busco el programa se va a detener
        ejecution=False
        for productos in data_py:
            if productos["producto"]==producto_especifico:
                ejecution=True
                data_final.append(productos)
                print( )
                print('producto: ', productos["producto"])
                print('precio: ', productos["precio"])
                print('stock: ', productos["stock"])
                print( )
                break
        if ejecution==False:
            print('No se encuentra el producto en el inventario')
    elif user_text==4:
        continuar_ejecutando=False
        data_py=[]
        data_final=[]
        data_dict={"inventario":data_final}
        for i in data["inventario"]:
            data_py.append(i)

        actualizo=input('Ingrese el nombre del producto a actualizar: ').lower()
        ejecution=False
        #aqui el produco a actualizar se elimina de la primera lista y se modifica, luego se agrega a la segunda lista.
        #los productos que no coinciden con la busqueda pero estan en el inventario se agregan igualmente a la segunda lista que seria mi lista final
        for productos in data_py:
            if productos["producto"]==actualizo:
                ejecution=True
                data_py.remove(productos)
                nombre=input('Ingrese el nuevo nombre del producto: ').lower()
                while type(nombre)!=str or nombre.isnumeric():
                    nombre=input('Por favor ingrese un nombre de tipo "str": ')
                precio=input('ingrese el nuevo precio del producto: ')
                while not precio.isnumeric():
                    precio=input('Por favor ingrese solo numeros en el precio: ')
                precio=int(precio)
                stock=input('Ingrese la nueva cantidad de productos en stock: ')
                while not precio.isnumeric():
                    stock=input('Por favor ingrese solo numeros en la cantidad en stock: ')
                stock=int(stock)
                producto_actualizado=crear_dict(nombre,precio,stock)
                data_final.append(producto_actualizado)
                print('Producto actualizado exitosamente!!')
                save_inv(data_dict)
                break  
            else:
                data_final.append(productos)
                save_inv(data_dict)    
        if ejecution==False:
            print('el producto no se encuentra en el inventario')
    elif user_text==5:
        continuar_ejecutando=False
        data_py=[]
        data_final=[]
        data_dict={"inventario":data_final}
        for i in data["inventario"]:
            data_py.append(i)
        elimino=input('Ingrese el nombre del producto a eliminar: ').lower()
        ejecution=False
        #aqui los productos que no se eliminaron se agregan a la segunda lista que seria la lista final asociada al diccionario a mostrar
        for productos in data_py:
            if productos["producto"]==elimino:
                ejecution=True
                data_py.remove(productos)
                print('producto eliminado exitosamente!!')
                save_inv(data_dict)
                break  
            else:
                data_final.append(productos) 
                save_inv(data_dict)
        if ejecution==False:
            print('el producto no se encuentra en el inventario')
    elif user_text==6:
        print('Hasta luego!!')
        break

        

        
