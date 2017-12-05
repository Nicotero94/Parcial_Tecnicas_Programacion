def calculadorDelEquipoGanadorDeLaLiga(equipos):

    equipoGanador = []

    if len(equipos) == 0:
        return ""




    for partidos in range(len(equipos)):

        ganador = []

        for resultado in range(len(equipos[partidos])):

            if equipos[partidos][resultado] != int:
                equipo = resultado
            elif equipos[partidos][resultado] == int:
                goles = resultado



            print(equiposs)













def ejercicio3(var1):
    return calculadorDelEquipoGanadorDeLaLiga(var1)


#assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
#assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
#assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")