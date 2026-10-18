def distancia_levenshtein(cadena_origen: str, cadena_destino: str) -> int:
    longitud_origen = len(cadena_origen)
    longitud_destino = len(cadena_destino)

    # matriz[fila][columna] = distancia entre los primeros 'fila' caracteres del origen y los primeros 'columna' caracteres del destino
    matriz = [[0] * (longitud_destino + 1) for _ in range(longitud_origen + 1)]

    # Primera columna: borrar todos los caracteres del origen
    for fila in range(longitud_origen + 1):
        matriz[fila][0] = fila

    # Primera fila: insertar todos los caracteres del destino
    for columna in range(longitud_destino + 1):
        matriz[0][columna] = columna

    # Llenado de la matriz
    for fila in range(1, longitud_origen + 1):
        for columna in range(1, longitud_destino + 1):
            if cadena_origen[fila - 1] == cadena_destino[columna - 1]:
                costo_sustitucion = 0
            else:
                costo_sustitucion = 1

            costo_eliminacion = matriz[fila - 1][columna] + 1
            costo_insercion = matriz[fila][columna - 1] + 1
            costo_cambio = matriz[fila - 1][columna - 1] + costo_sustitucion

            matriz[fila][columna] = min(costo_eliminacion, costo_insercion, costo_cambio)

    return matriz[longitud_origen][longitud_destino]


print(distancia_levenshtein("kitten", "sitting"))  # 3
print(distancia_levenshtein("gato", "pato"))       # 1