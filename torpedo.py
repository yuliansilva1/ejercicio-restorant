#----------------hotel--------------------
#muestra el menu de opciones
def mostrar_menu():
    print("""MENÚ
    1. Ver edificio
    2. Comprar departamento
    3. Buscar dueño
    4. Total ganancias
    5. Salir""")
    
#valida las opciones
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")
            
#crear variables necesarias:
import numpy
edificio = numpy.zeros((10,4), int)
lista_ruts = []
lista_nombres = []
lista_filas = []
lista_columnas = []

#variables auxiliares:
lista_letras = ['A','B','C','D']
lista_pisos = [10,9,8,7,6,5,4,3,2,1]

#valida el rut
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
#valida el nombre
def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

#vista del edificio
def ver_edificio():
    print("        A B C D")
    for x in range(10):
        print("Piso",lista_pisos[x], end="\t")
        for y in range(4):
            print(edificio[x][y], end=" ")
        print()
        
#valida los pisos
def validar_piso():
    while True:
        try:
            piso = int(input("Ingrese piso(1-10): "))
            if piso in lista_pisos:
                return piso
            else:
                print("ERROR! PISO INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#valida los departamentos            
def validar_depto():
    while True:
        depto = input("Ingrese depto(A,B,C,D): ")
        if depto.upper() in lista_letras:
            return depto
        else:
            print("ERROR! DEPARTAMENTO INCORRECTO!")
            
#proceso para comprar departamento
def comprar():
    if 0 not in edificio:
        print("NO EXISTEN DEPARTAMENTOS DISPONIBLES!")
        return
    rut = validar_rut()
    nombre = validar_nombre()
    while True:
        ver_edificio()
        piso = validar_piso()
        departamento = validar_depto()
        piso_comprar = lista_pisos.index(piso)
        depto_comprar = lista_letras.index(departamento.upper())
        if edificio[piso_comprar][depto_comprar] == 0:
            #antes de registrarlo, hay que pagar:
            if piso_comprar in(0,1,2):
                valor = 200000000
            else:
                valor = 150000000
            dinero = int(input("Ingrese dinero: "))
            if dinero == valor:
                edificio[piso_comprar][depto_comprar] = 1
                lista_ruts.append(rut)
                lista_nombres.append(nombre)
                lista_filas.append(piso_comprar)
                lista_columnas.append(depto_comprar)
                print("DEPARTAMENTO COMPRADO CON ÉXITO!")
                break
            else:
                print("DINERO INSUFICIENTE, GUARDIAS! ATTACK!")
                return
        else:
            print("DEPARTAMENTO NO DISPONIBLE")
            
#muestra las ganancias de la venta de departamentos
def ganancias():
    acum = 0
    for x in range(10):
        for y in range(4):
            if x in (0,1,2) and edificio[x][y] == 1:
                acum += 200000000
            elif edificio[x][y] == 1:
                acum += 150000000
    return

#----------------restaurante--------------------
#los import ocupados
import os
import time
import numpy

#arreglo
restaurant = numpy.zeros((3,3),int)

#listas
lista_ruts = []
lista_nombres = []
lista_correos = []
lista_filas = []
lista_columnas = []
lista_totales = []

#muestra el menu de opciones
def mostrar_menu():
    os.system('clear')
    print("""MENÚ
    1. Ver restaurant
    2. Reservar
    3. Ver carta
    4. Pagar
    5. Cancelar reserva
    6. Salir""")
 
#valida las opciones   
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,5,6):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
    
#vista del restaurante
def ver_restaurant():
    os.system('clear')
    print("\tVER RESTAURANT\n")
    contador = 1
    for x in range(3):
        print(f"Mesas para {(x+1)*2} personas: ",end=" ")
        for y in range(3):
            print(f"Mesa {contador}: {restaurant[x][y]} ", end=" ")
            contador += 1
        print("\n")
    time.sleep(3)
    
#valida el rut
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#valida el nombre
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

#valida el correo
def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")

#valida la cantidad de personas max 6 min 1
def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas(1-6): "))
            if cantidad >= 1 and cantidad <= 6:
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DEBE ESTAR ENTRE 1 Y 6!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#valida las mesas disponibles
def mesas_disponibles(p_cantidad):
    contador = 1
    lista_mesas = []
    for x in range(3):
        for y in range(3):
            if restaurant[x][y] == 0:
                if p_cantidad <= 2:
                    lista_mesas.append(contador)
                elif p_cantidad >=3 and p_cantidad <= 4 and x in(1,2):
                    lista_mesas.append(contador)
                elif p_cantidad >= 5 and p_cantidad <=6 and x == 2:
                    lista_mesas.append(contador)
            contador += 1
    return lista_mesas

#valida que la mesa no este reservada
def validar_mesa(p_mesas):
    while True:
        try:
            mesa = int(input("Ingrese número de mesa: "))
            if mesa in(p_mesas):
                return mesa
            else:
                print("ERROR! NÚMERO DE MESA NO DISPONIBLE!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#hace el proseso de validacion para reservar la mesa y lo guarda
def reservar():
    os.system('clear')
    print("RESERVAR MESA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        print("YA TIENE UNA RESERVA!")
        return

    nombre = validar_nombre()
    correo = validar_correo()
    ver_restaurant()
    cant_personas = validar_cantidad()
    lista_mesas = mesas_disponibles(cant_personas)
    if len(lista_mesas)==0:
        print("NO EXISTEN MESAS DISPONIBLES")
        time.sleep(3)
        return
    
    print("MESAS DISPONIBLES:",lista_mesas)
    mesa = validar_mesa(lista_mesas)
    contador = 1
    for x in range(3):
        for y in range(3):
            if contador == mesa:
                restaurant[x][y] = 1
                lista_ruts.append(rut)
                lista_nombres.append(nombre)
                lista_correos.append(correo)
                lista_filas.append(x)
                lista_columnas.append(y)
                lista_totales.append(0)
                print("MESA RESERVADA CON ÉXITO")
                time.sleep(3)
            contador+=1

#valida el menu de productos del local
def ver_carta():
    os.system('clear')
    rut = validar_rut()
    if rut not in lista_ruts:
        print("NO EXISTE RESERVA PARA EL RUT INDICADO!")
        time.sleep(3)
        return

    posicion = lista_ruts.index(rut)
    acumulador = 0
    while True:
        os.system('clear')
        print("""CARTA
        1. BEBESTIBLES
        2. PLATO FONDO
        3. POSTRES
        4. PEDIR
        5. CANCELAR""")
        opcion = validar_opcion_menu()
        if opcion == 1:
            print("""\nBEBESTIBLES
            1. LIMONADA $2.500
            2. BEBIDA $1.500
            3. JUGO $2.000""")
            opcion_bebestible = validar_opciones_carta()
            cantidad = validar_cantidad_prod()
            if opcion_bebestible == 1:
                acumulador = acumulador + 2500*cantidad
            elif opcion_bebestible == 2:
                acumulador = acumulador + 1500*cantidad
            else:
                acumulador = acumulador + 2000*cantidad
        elif opcion == 2:
            print("""\nPLATO FONDO
            1. CONSOME $3.000
            2. POLLO CON PAPAS FRITAS $4.500
            3. ENSALADA $2.000""")
            opcion_plato = validar_opciones_carta()
            cantidad = validar_cantidad_prod()
            if opcion_plato == 1:
                acumulador = acumulador + 3000*cantidad
            elif opcion_plato == 2:
                acumulador = acumulador + 4500*cantidad
            else:
                acumulador = acumulador + 2000*cantidad
        elif opcion == 3:
            print("""\nPOSTRES
            1. HELADO $2.000
            2. TIRAMISU $2.500
            3. JALEA $1.000""")
            opcion_plato = validar_opciones_carta()
            cantidad = validar_cantidad_prod()
            if opcion_plato == 1:
                acumulador = acumulador + 2000*cantidad
            elif opcion_plato == 2:
                acumulador = acumulador + 2500*cantidad
            else:
                acumulador = acumulador + 1000*cantidad
        elif opcion == 4:
            lista_totales[posicion] = lista_totales[posicion] + acumulador
            print("PEDIDO REALIZADO!")
            break
        else:
            print("PEDIDO CANCELADO DE LA CARTA")
            break
    time.sleep(3)

#valida las opciones del menu de productos
def validar_opcion_menu():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
#valida las opciones de los productor por opcion
def validar_opciones_carta():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
#valida la cantidad de productos
def validar_cantidad_prod():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#valida el descuento
def validar_descuento():
    while True:
        try:
            desc = int(input("Ingrese descuento: "))
            if desc >= 0:
                return desc
            else:
                print("ERROR! DESCUENTO DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#valida la opcion de pago
def pagar():
    os.system('clear')
    print("PAGAR CUENTA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        posicion = lista_ruts.index(rut)
        descuento = validar_descuento()
        print(f"""BOLETA
        SUBTOTAL   {lista_totales[posicion]}
        IVA        {round(19/100 * lista_totales[posicion])}
        TOTAL      {round(119/100 * lista_totales[posicion])}
        DESCUENTO  {descuento}
        TOTAL      {round(119/100 * lista_totales[posicion]) - descuento}""")

        fila = lista_filas[posicion]
        columna = lista_columnas[posicion]
        restaurant[fila][columna] = 0
        
        lista_ruts.pop(posicion)
        lista_nombres.pop(posicion)
        lista_correos.pop(posicion)
        lista_filas.pop(posicion)
        lista_columnas.pop(posicion)
        lista_totales.pop(posicion)
        print("\nPAGO REALIZADO CON ÉXITO!")
    else:
        print("EL RUT INDICADO NO TIENE RESERVA!")
    time.sleep(5)

#validacion de la cancelacion de la reserva
def cancelar_reserva():
    os.system('clear')
    print("CANCELAR RESERVA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        posicion = lista_ruts.index(rut)
        fila = lista_filas[posicion]
        columna = lista_columnas[posicion]
        restaurant[fila][columna] = 0
        
        lista_ruts.pop(posicion)
        lista_nombres.pop(posicion)
        lista_correos.pop(posicion)
        lista_filas.pop(posicion)
        lista_columnas.pop(posicion)
        lista_totales.pop(posicion)
        print("\nRESERVA CANCELADA CON ÉXITO!")
    else:
        print("EL RUT INDICADO NO TIENE RESERVA!")
    time.sleep(5)


    