from modelo2 import modelo

def probability(viento, nubosidad, lluvia, pinta):
    
    for x,y in viento.items():
        vie = x
        vie2 = y
    for a,b in nubosidad.items():
        nub = a
        nub2 = b
    for c,d in lluvia.items():
        ll = c
        ll2 = d

    predicciones = modelo.predict_proba({
    vie: vie2,
    nub: nub2,
    ll: ll2,
    "cabeza": pinta[0],
    "torso": pinta[1],
    "piernas": pinta[2],
    "pies": pinta[3]
    })

    # Visualizemos las predicciones para cada nodo
    for nodo, prediccion in zip(modelo.states, predicciones):
        if isinstance(prediccion, str):
            print(f"{nodo.name}: {prediccion}")
        else:
            print(f"{nodo.name}")
            for valor, probabilidad in prediccion.parameters[0].items(): 
                print(f"       {valor}: {probabilidad:.2f}")

vient = {"vientos": "si"}
humed = {"humedad": "si"}
nubos = {"": ""}
lluv = {"": ""}
pint = ["gorro", "sueter", "bermuda", "tenis"]

probability(vient, nubos, lluv, pint)