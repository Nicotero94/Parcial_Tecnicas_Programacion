def devolverEquipoMaximoPuntaje(puntajes):

    tablaDePosiciones = puntajes

    puntajeAlto = max(tablaDePosiciones.values())

    for clave, valor in tablaDePosiciones.items():

        if valor == puntajeAlto:

            return clave


def calculadorDelEquipoGanadorDeLaLiga(resultados):

    if len(resultados) == 0:
        return

    EQUIPO_1 = 0
    EQUIPO_2 = 2

    GOLES_1 = 1
    GOLES_2 = 3

    puntajes = {}

    for partido in resultados:


        if (partido[GOLES_1] > partido[GOLES_2]):

            ganador = partido[EQUIPO_1]
            perdedor = partido[EQUIPO_2]

            puntoGanador = 2
            puntoPerdedor = 0

            puntuajeEnLaTabla = 0

            puntajes[ganador] = puntuajeEnLaTabla + puntoGanador
            puntajes[perdedor] = puntuajeEnLaTabla + puntoPerdedor

        elif (partido[GOLES_1] < partido[GOLES_2]):

            ganador = partido[EQUIPO_2]
            perdedor = partido[EQUIPO_1]

            puntoGanador = 2
            puntoPerdedor = 0

            puntuajeEnLaTabla = 0

            puntajes[ganador] = puntuajeEnLaTabla + puntoGanador
            puntajes[perdedor] = puntuajeEnLaTabla + puntoPerdedor

        else:
            puntajes[partido[EQUIPO_1]] = 1
            puntajes[partido[EQUIPO_2]] = 1




    return devolverEquipoMaximoPuntaje(puntajes)


def ejercicio3(var1):
    return calculadorDelEquipoGanadorDeLaLiga(var1)


#assert (ejercicio3([]) == "")
#assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
#assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")