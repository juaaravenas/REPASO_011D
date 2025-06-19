def mostrar_menu(titulo, lista_opciones ):
    print(titulo)
    for opcion  in  lista_opciones:
        print(opcion)

def validar_opcion(canti_opcion):
    ingreso_ok = False
    while ingreso_ok == False:
        try:
            opcion = int(input("Ingrese opcion seleccionada "))
            if opcion <= 0  or opcion > canti_opcion:
                print("Error:  Opçion no validad")
            else:
                ingreso_ok = True
        except:        
            print("ERROR:  El valor debe ser numerico ")
    return opcion

def  validar_stock(stock_total):
     if  stock_total > 0:
         return True
     else:
         return False

def validar_nombre(dicc_reserva,nombre):
    if nombre in dicc_reserva:
       return True
    else:
         return False

def validar_clave(clave_ingreso, clave_validar):
    if  clave_ingreso == clave_validar:
       return True
    else:
         return False

def reserva(dicc_reserva, stock):
    if validar_stock(stock):
       nombre = input("Ingrese nombre de Cliente ") 
       if validar_nombre(dicc_reserva,nombre):
           print("ERROR: Cliente ya realizó reserva ")
       else:
           clave = input("Ingrese la clave para reserva ")
           clave_validar = "EstoyEnListaDeReserva"
           if validar_clave(clave, clave_validar):
               dicc_reserva[nombre]= 1
               stock -= 1
           else:
               print("ERROR:  Clave incorrecta ")

    else:
        print("Stock insuficiente ")     
    return   dicc_reserva, stock


def buscar(dicc_reserva, stock):
       nombre = input("Ingrese nombre de Cliente ") 
       if validar_nombre(dicc_reserva,nombre):
          print(f"Le damos la bienvenida al cliente {nombre}")  
          if validar_stock(stock):
             opcion =  input("Desea pagar para ser cliente VIP (s/n) ")
             if opcion == "s":
                dicc_reserva[nombre] += 1
                stock -= 1
          else:
              print("ERROR:  Stock insuficiente ")
       else:
          print("ERROR: Cliente no existe.  Debe realizar reserva  ")
       return   dicc_reserva, stock
 



dicc_reserva = {}
lista_opciones = []
stock_zapatilla = 20

titulo_menu = "TOTEM AUTOATENCIÓN RESERVA STRIKE"
lista_opciones.append("1.- Reservar zapatillas ")
lista_opciones.append("2.- Buscar zapatillas reservadas.")
lista_opciones.append("3.- Ver stock de reservas. ")
lista_opciones.append("4.- Salir. ")

opcion = 0
while opcion != len(lista_opciones):
    mostrar_menu(titulo_menu, lista_opciones ) 
    opcion =  validar_opcion(len(lista_opciones))   

    match opcion:
        case 1:
            print(dicc_reserva, stock_zapatilla)
            dicc_reserva, stock_zapatilla = reserva(dicc_reserva, stock_zapatilla)
            print(dicc_reserva, stock_zapatilla)
        case 2:
            print(dicc_reserva, stock_zapatilla)
            dicc_reserva, stock_zapatilla = buscar(dicc_reserva, stock_zapatilla)
            print(dicc_reserva, stock_zapatilla)
        case 4:
            print("Programa terminado... ")