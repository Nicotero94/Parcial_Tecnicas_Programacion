def iniciarTablaDePosicionesConCeros(resultados):

    tablaConEquipos = {}

    for partido in resultados:

        diccionario = {partido}

        for equipos in diccionario:

           tablaConEquipos[equipos[0]] = 0
           tablaConEquipos[equipos[2]] = 0

    return tablaConEquipos

def devolverEquipoMaximoPuntaje(tablaDePosiciones):

    equipoConPuntajeAlto = max(tablaDePosiciones.values())
    puntosDeLosEquipos = sorted(tablaDePosiciones.values())
    equipoGanadorAlfabeticamente = sorted(tablaDePosiciones.keys())

    for equipo, puntos in tablaDePosiciones.items():

        lisa = []

        if puntos == equipoConPuntajeAlto:
            lisa.append(puntos)



        print(lisa)

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

def ejercicio3(var1):
    return calculadorDelEquipoGanadorDeLaLiga(var1)

#assert (ejercicio3([]) == "")
#assert (ejercicio3([("a", 1, "b", 0)]) == "a")
#assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")