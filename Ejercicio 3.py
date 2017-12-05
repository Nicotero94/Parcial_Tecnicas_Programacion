
def devolverEquipoMaximoPuntaje(puntajes):



    tablaDePosiciones = puntajes.items()

    for i in tablaDePosiciones:


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

            puntajes[ganador] = 2
            puntajes[perdedor] = 0
        elif (partido[GOLES_1] < partido[GOLES_2]):

            ganador = partido[EQUIPO_2]
            perdedor = partido[EQUIPO_1]

            puntajes[ganador] = 2
            puntajes[perdedor] = 0

        else:
            puntajes[partido[EQUIPO_1]] = 1
            puntajes[partido[EQUIPO_2]] = 1




    return devolverEquipoMaximoPuntaje(puntajes)


def ejercicio3(var1):
    return calculadorDelEquipoGanadorDeLaLiga(var1)


#assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
#assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
#assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")