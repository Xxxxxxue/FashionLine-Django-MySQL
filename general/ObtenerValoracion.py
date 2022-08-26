def SacarValoracion(valoraciones):
    media = 0
    excelente = 0
    muybien = 0
    correcto = 0
    mal = 0
    muymal = 0
    print(valoraciones.count())
    for v in valoraciones:
        media += v.idvaloracion.valoracion
        if (v.idvaloracion.valoracion == 5):
            excelente += 1
        if (v.idvaloracion.valoracion == 4):
            muybien += 1
        if (v.idvaloracion.valoracion == 3):
            correcto += 1
        if (v.idvaloracion.valoracion == 2):
            mal += 1
        if (v.idvaloracion.valoracion == 1):
            muymal += 1

    media = media / valoraciones.count()
    media = round(media, 2)
    # para cada valor de valoracion, calcula su porcentaje
    listValora = {
        'excelente': round(excelente / valoraciones.count() * 100, 0),
        'muy bien': round(muybien / valoraciones.count() * 100, 0),
        'correcto': round(correcto / valoraciones.count() * 100, 0),
        'mal': round(mal / valoraciones.count() * 100, 0),
        'muy mal': round(muymal / valoraciones.count() * 100, 0),
        'media': media
    }
    return listValora