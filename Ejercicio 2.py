def convertirMapaAMapaBooleano(mapa):

    mapaBooleano = []

    for linea in mapa:

        filaBooleana = []

        for letra in linea:
            if letra == "b":
                filaBooleana.append(True)
            elif letra == '.':
                filaBooleana.append(False)
            else:
                return []

        mapaBooleano.append(filaBooleana)

    return mapaBooleano

def batallaDeBotes(mapa,disparos):

    botesNoHundidos = []
    soloTieneEspacios = False

    if len(mapa) == 0:
        return botesNoHundidos

    for i in range(len(mapa)):
        if mapa[i] != " ":
            soloTieneEspacios = True
        elif mapa[i] != ".":
            return botesNoHundidos
        elif mapa[i] != "b":
            return botesNoHundidos

    if soloTieneEspacios == False:
        return botesNoHundidos

    mapaDeBooleanos = convertirMapaAMapaBooleano(mapa)

    for fila in mapaDeBooleanos:

        if fila == mapaDeBooleanos[0]:

            filaNumero0 = mapaDeBooleanos[0]

        elif fila == mapaDeBooleanos[1]:
            filaNumero1 = mapaDeBooleanos[1]

        elif fila == mapaDeBooleanos[2]:
            filaNumero2 = mapaDeBooleanos[2]

        elif fila == mapaDeBooleanos[3]:
            filaNumero3 = mapaDeBooleanos[3]

    for disparo in disparos:

        botesHundidos = []

        if disparo[0] == 1:
            if disparo[1] == 1:
                tiro = True
                if filaNumero0[0] == tiro:
                    botesHundidos.append(disparo)



    return botesNoHundidos

def ejercicio2(var1,var2):
    return batallaDeBotes(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

#assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])
