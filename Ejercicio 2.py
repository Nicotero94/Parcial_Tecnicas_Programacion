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

        posicionesDeBotes = []
        noBotes = []

        for bote in fila:

            if bote == True:

                boteEnLaFila = mapaDeBooleanos.index(fila)
                boteEnLaColumna = fila.index(bote)

                bote = (boteEnLaFila,boteEnLaColumna)

                posicionesDeBotes.append(bote)

            elif bote == False:
                noBotes.append(bote)

        print(posicionesDeBotes)


    for disparo in disparos:

        posicionesDeDisparo = []

        fila, columna = disparo
        menos = (fila - 1, columna - 1)
        posicionesDeDisparo.append(menos)



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
