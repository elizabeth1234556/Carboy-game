f = open('datos.txt', 'r')
mensaje = f.read()
f.close
numerolinea = 0
listaUno = mensaje.split("\n")
print(listaUno)

sentencia_0 = "Inicio:"
sentencia_1 = ("Tanque = lleno", "Tanque = medio", "Tanque = cuarto")
sentencias = ("Velocidad = rapido", "Velocidad = lento", "Velocidad = normal", "Acelerar",
              "Si Trafico : Derecha", "Si Trafico : izquierda",
              "Si Trafico : fin :", "Si Trafico : rebasar", "Si Trafico : velocidad = rapido",
              "Si Trafico : velocidad = lento", "Si Trafico : velocidad = normal")

sentencias_ErrorSintaxis = (
    "Tanque = rapido", "Tanque = lento", "Tanque = normal", "Tanque = Derecha", "Tanque = Izquierda",
    "Tanque = Acelerar",
    "Tanque = Trafico", "Tanque = Tanque", "Tanque = Rebasar")

for i in listaUno:
    if i == listaUno[0]:
        if listaUno[0] == sentencia_0:
            print("LINEA 0 VALIDO")
        else:
            print("LINEA 0 NO VALIDO")

    if i == listaUno[1]:
        if listaUno[1] == sentencia_1:
            print("LINEA 1 VALIDO")
        else:
            print("LINEA 1 NO VALIDO  " )

    if i == listaUno[2]:
        if listaUno[2] == sentencias:
            print("LINEA 2 VALIDO")
        else:
            print("LINEA 2 NO VALIDO")

    if i == listaUno[3]:
        if listaUno[3] == sentencias:
            print("LINEA 3 VALIDO")
        else:
            print("LINEA 3 NO VALIDO")
