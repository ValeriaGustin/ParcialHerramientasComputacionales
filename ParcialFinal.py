"""
Parcial Final- Herramientas computacionales
Punto 1
Valeria Gustín
Sara Tabares
"""
def precioFinal(lis, rol, beca, cedula):
    pF = 0
    codigos = []
    for i in range(len(lis)):
        cod = lis[i][0]
        unidad = lis[i][1]
        precio = lis[i][2]

        pF += precio * unidad
        codigos.append(cod)

    if rol == 2 and beca == 1:
        pF *= 0.5
        print("El estudiante con cedula %d, debe pagar %d por los productos: "%(cedula, pF), end = "")
        print(", ".join(codigos))
    elif rol == 2:
        descuento = pF*0.3
        pF -= descuento
        print("El estudiante con cedula %d, debe pagar %d por los productos: "%(cedula, pF), end = "")
        print(", ".join(codigos))
    else:
        descuento = pF*0.2
        pF -= descuento
        print("El profesor con cedula %d, debe pagar %d por los productos: "%(cedula, pF), end = "")
        print(", ".join(codigos))



def cafeteria2():
    cedula = int(input("Ingrese cédula: "))
    print("Seleccione rol")
    print("(1) Profesor")
    print("(2) Estudiante")
    rol = int(input())
    
    if rol == 2:
        print("¿Pertenece al programa de becas?")
        print("(1)Si")
        print("(2)No")
        beca = int(input())
    else:
        beca = 0
        
    print("Número de productos a cancelar: ")
    numProductos = int(input())

    i = 1
    lista = []
    while i <= numProductos:
        lista.append([])
        Codigo = input("Código producto %d: " %i)
        lista[-1].append(Codigo)
        
        Unidades = int(input("Unidades: "))
        lista[-1].append(Unidades)
        
        Precio= int(input("Precio: "))
        lista[-1].append(Precio)
        
        print()
        i+=1
    
    precioFinal(lista, rol, beca, cedula)
    
cafeteria2()
