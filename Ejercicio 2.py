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

    posicionesDeBotes = []
    posicionesDeDisparo = []

    if len(mapa) == 0:
        return botesNoHundidos

    largoDelMapa = len(mapa)-1

    for lasFilasDelMapaSonIguales in range(largoDelMapa):

        if len(mapa[lasFilasDelMapaSonIguales]) != len(mapa[lasFilasDelMapaSonIguales + 1]):
            return botesNoHundidos

    for caracter in range(len(mapa)):

        if mapa[caracter] != " ":
            soloTieneEspacios = True
        elif mapa[caracter] != ".":
            return botesNoHundidos
        elif mapa[caracter] != "b":
            return botesNoHundidos

    if soloTieneEspacios == False:
        return botesNoHundidos

    mapaDeBooleanos = convertirMapaAMapaBooleano(mapa)

    for fila in range(len(mapaDeBooleanos)):

        noHayBotes = []

        for bote in range(len(mapaDeBooleanos[fila])):

            if mapaDeBooleanos[fila][bote] == True:
                boteEnLaFila = fila
                boteEnLaColumna = bote

                posicionDeBote = (boteEnLaFila,boteEnLaColumna)
                posicionesDeBotes.append(posicionDeBote)

            elif bote == False:
                noHayBotes.append(posicionDeBote)

    for disparo in disparos:
        fila, columna = disparo
        menos = (fila - 1, columna - 1)
        posicionesDeDisparo.append(menos)

    hundidos = []

    for item in posicionesDeBotes:
        if item not in posicionesDeDisparo:
            botesNoHundidos.append(item)
        else:
            hundidos.append(hundidos)

    posicionesDeBotesCorregidos = []

    for sumarUno in botesNoHundidos:
        fila, columna = sumarUno
        posicionesCorregidas = (fila + 1, columna + 1)
        posicionesDeBotesCorregidos.append(posicionesCorregidas)

    return posicionesDeBotesCorregidos



def ejercicio2(var1,var2):
    return batallaDeBotes(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])

