def generador_turno(area):
    turno_p = 1
    turno_f = 1
    turno_c = 1
    while True:
        if area == "perfumeria":
            yield turno_p
            turno_p +=1

        elif area == "farmacia":
            yield turno_f
            turno_f +=1
            
        else:
            yield turno_c
            turno_c +=1