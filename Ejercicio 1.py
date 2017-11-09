def rotacionDeUnaPalabra(palabra):

    palabrasRotadas = []

    if len(palabra) == 0:
        return palabrasRotadas

    elif len(palabra) == 1:

        palabrasRotadas.append(palabra)
        return palabrasRotadas

    palabrasRotadas.append(palabra)

    for letra in range(len(palabra)-1):

        rotar = palabra[letra + 1]

        if len(palabra) == 2:
            rotar = rotar + palabra[0]
            palabrasRotadas.append(rotar)

        elif len(palabra) == 3:
            if rotar[0] == palabra[1]:
                rotar = rotar + palabra[2] + palabra[0]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[2]:
                rotar = rotar + palabra[0] + palabra[1]
                palabrasRotadas.append(rotar)

        elif len(palabra) == 4:
            if rotar[0] == palabra[1]:
                rotar = rotar + palabra[2] + palabra[3] + palabra[0]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[2]:
                rotar = rotar + palabra[3] + palabra[0] + palabra[1]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[3]:
                rotar = rotar + palabra[0] + palabra[1] + palabra[2]
                palabrasRotadas.append(rotar)

        elif len(palabra) == 5:
            if rotar[0] == palabra[1]:
                rotar = rotar + palabra[2] + palabra[3] + palabra[4] + palabra[0]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[2]:
                rotar = rotar + palabra[3] + palabra[4] + palabra[0] + palabra[1]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[3]:
                rotar = rotar + palabra[4] + palabra[0] + palabra[1] + palabra[2]
                palabrasRotadas.append(rotar)
            elif rotar[0] == palabra[4]:
                rotar = rotar + palabra[0] + palabra[1] + palabra[2] + palabra[3]
                palabrasRotadas.append(rotar)

    return palabrasRotadas

def ejercicio1(var1):
    return rotacionDeUnaPalabra(var1)


assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])

