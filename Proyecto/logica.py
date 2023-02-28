from logic import *

def logica_ropa(prendas,estilo):
    estil = Symbol(estilo)
    estilo_actual = Symbol("estilo_actual")
    conocimiento = And(estilo_actual,estil)
    prendas_logic = []
    for j in prendas:
        estilo_actual = Symbol(j.estilo)
        if model_check(conocimiento,estilo_actual):
            prendas_logic.append(j)
    for elem in prendas_logic:
        print(elem.nombre)
    return prendas_logic