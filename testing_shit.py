from typing import Generator, Iterable
from utilidades import (Usuarios, Ordenes, OrdenesItems, 
                       Productos, Proveedor, ProveedoresProductos)

def cargar_productos(path: str) -> Generator:
    with open(path, encoding = 'utf-8') as file:
        primera_linea = True
        for linea in file:
            if primera_linea:
                #esta es la primera linea, descartala
                primera_linea = False
            else:
                producto = linea.strip("\n").split(";")
                producto[2], producto[3] = float(producto[2]), \
                                           int(producto[3])
                yield Productos(*producto)

def productos_desde_fecha(generador_productos: Generator,
                            fecha: str, inverso: bool) -> Generator:
    return map(lambda producto: ("hola" if int(producto.fecha_modificacion[:4]) >= int(fecha[:4]) 
                                  else "chao") if inverso  else False, generador_productos)

productos = cargar_productos("productos.csv")
productos = productos_desde_fecha(productos, "2023-12-03", True)
for producto in productos:
    print(producto)