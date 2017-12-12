def devolverEquipoMaximoPuntaje(puntajes):

    equipoConPuntajeAlto = max(puntajes.values())
    equipoGanadorAlfabeticamente = sorted(puntajes.keys())

    for equipo, puntos in puntajes.items():

        if puntos >= equipoConPuntajeAlto:
                return equipo

def calculadorDelEquipoGanadorDeLaLiga(resultados):

    if len(resultados) == 0:
        return ''

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

            if len(puntajes) == 0:
                puntajes[ganador] = puntoGanador
                puntajes[perdedor] = puntoPerdedor

            elif len(puntajes) > 0:

                if ganador not in puntajes:
                    puntajeDelEquipoGanador = 0
                else:
                    puntajeDelEquipoGanador = puntajes.get(ganador)

                if perdedor not in puntajes:
                    puntajeDelEquipoPerdedor = 0
                else:
                    puntajeDelEquipoPerdedor = puntajes.get(perdedor)

                puntajes[ganador] = puntajeDelEquipoGanador + puntoGanador
                puntajes[perdedor] = puntajeDelEquipoPerdedor + puntoPerdedor


        elif (partido[GOLES_1] < partido[GOLES_2]):
            ganador = partido[EQUIPO_2]
            perdedor = partido[EQUIPO_1]

            puntoGanador = 2
            puntoPerdedor = 0

            if len(puntajes) == 0:
                puntajes[ganador] = puntoGanador
                puntajes[perdedor] = puntoPerdedor

            elif len(puntajes) > 0:

                if ganador not in puntajes:
                    puntajeDelEquipoGanador = 0
                else:
                    puntajeDelEquipoGanador = puntajes.get(ganador)

                if perdedor not in puntajes:
                    puntajeDelEquipoPerdedor = 0
                else:
                    puntajeDelEquipoPerdedor = puntajes.get(perdedor)

                puntajes[ganador] = puntajeDelEquipoGanador + puntoGanador
                puntajes[perdedor] = puntajeDelEquipoPerdedor + puntoPerdedor

        else:
            if len(puntajes) == 0:
                puntajes[partido[EQUIPO_1]] = 1
                puntajes[partido[EQUIPO_2]] = 1

            elif len(puntajes) > 0:

                if EQUIPO_1 not in puntajes:
                    puntajeDelEquipo1 = 0
                else:
                    puntajeDelEquipo1 = puntajes.get(EQUIPO_1)

                if EQUIPO_2 not in puntajes:
                    puntajeDelEquipo2 = 0
                else:
                    puntajeDelEquipo2 = puntajes.get(EQUIPO_2)

                puntajes[partido[EQUIPO_1]] = puntajeDelEquipo1 + 1
                puntajes[partido[EQUIPO_2]] = puntajeDelEquipo2 + 1

    return devolverEquipoMaximoPuntaje(puntajes)

def ejercicio3(var1):
    return calculadorDelEquipoGanadorDeLaLiga(var1)

#assert (ejercicio3([]) == "")
#assert (ejercicio3([("a", 1, "b", 0)]) == "a")
#assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")