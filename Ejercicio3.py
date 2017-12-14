def iniciarTablaDePosicionesConCeros(resultados):

    tablaConEquipos = {}

    for partido in resultados:

        equipos = {partido}

        for equipo in equipos:

           tablaConEquipos[equipo[0]] = 0
           tablaConEquipos[equipo[2]] = 0

    return tablaConEquipos

def devolverEquipoMaximoPuntaje(tablaDePosiciones):

    equipoConPuntajeAlto = max(tablaDePosiciones.values())
    equipoConPuntajeBajo = min(tablaDePosiciones.values())
    equiposOrdenadosAlfabeticamente = sorted(tablaDePosiciones.keys())
    equipoGanadorAlfabeticamente = equiposOrdenadosAlfabeticamente[0]

    for equipo, puntos in tablaDePosiciones.items():

        if equipoConPuntajeAlto == equipoConPuntajeBajo:
            return equipoGanadorAlfabeticamente

        elif puntos == equipoConPuntajeAlto:
            return equipo

def calculadorDelEquipoGanadorDeLaLiga(resultados):

    if len(resultados) == 0:
        return ''

    tablaDePosiciones = iniciarTablaDePosicionesConCeros(resultados)

    EQUIPO_1 = 0
    EQUIPO_2 = 2

    GOLES_1 = 1
    GOLES_2 = 3

    for partido in resultados:

        if partido[GOLES_1] > partido[GOLES_2]:

            ganador = partido[EQUIPO_1]
            perdedor = partido[EQUIPO_2]

            puntoGanador = 2
            puntoPerdedor = 0

            puntajeDelEquipoGanador = tablaDePosiciones.get(ganador)
            puntajeDelEquipoPerdedor = tablaDePosiciones.get(perdedor)

            tablaDePosiciones[ganador] = puntajeDelEquipoGanador + puntoGanador
            tablaDePosiciones[perdedor] = puntajeDelEquipoPerdedor + puntoPerdedor

        elif partido[GOLES_1] < partido[GOLES_2]:
            ganador = partido[EQUIPO_2]
            perdedor = partido[EQUIPO_1]

            puntoGanador = 2
            puntoPerdedor = 0

            puntajeDelEquipoGanador = tablaDePosiciones.get(ganador)
            puntajeDelEquipoPerdedor = tablaDePosiciones.get(perdedor)

            tablaDePosiciones[ganador] = puntajeDelEquipoGanador + puntoGanador
            tablaDePosiciones[perdedor] = puntajeDelEquipoPerdedor + puntoPerdedor

        else:
            equipo1 = partido[EQUIPO_1]
            equipo2 = partido[EQUIPO_2]

            tablaDePosiciones[equipo1] += 1
            tablaDePosiciones[equipo2] += 1

    return devolverEquipoMaximoPuntaje(tablaDePosiciones)