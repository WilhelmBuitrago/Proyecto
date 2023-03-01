from pomegranate import *

# pip install pomegranate
# Si no funciona hay q instalar Microsoft Visual C++ 14 o mayor

# Nodo vientos, no tiene padres
vientos = Node(DiscreteDistribution({
    "si": 0.4,
    "no": 0.6
}), name="vientos")

# Nodo de humedad esta condicionado por los vientos
"""humedad = Node(ConditionalProbabilityTable([
    ["si","si",0.6],
    ["si","no",0.4],
    ["no","si",0.3],
    ["no","no",0.7]
],[vientos.distribution]), name="humedad")"""

# nodo nubosidad esta condicionado por la humedad
nubosidad = Node(ConditionalProbabilityTable([
    ["si","si", 0.7],
    ["si","no", 0.3],
    ["no","si", 0.2],
    ["no","no", 0.8]
],[vientos.distribution]), name="nubosidad")

# Nodo lluvia esta condicionada por la nubosidad
lluvia = Node(ConditionalProbabilityTable([
    ["si","si", 0.7],
    ["si","no", 0.3],
    ["no","si", 0.2],
    ["no","no", 0.8],
    
],[nubosidad.distribution]),name="lluvia")

#############################################################

# Nodo cabeza esta condicionado por la lluvia
cabeza = Node(ConditionalProbabilityTable([
    ["si","sombrero", 0.6],
    ["si","gorra", 0.3],
    ["si","gorro", 0.05],
    ["si","nada", 0.05],
    ["no","sombrero", 0.2],
    ["no","gorra", 0.3],
    ["no","gorro", 0.2],
    ["no","nada", 0.3],
    
],[lluvia.distribution]),name="cabeza")

# Nodo torso esta condicionada por la lluvia
torso = Node(ConditionalProbabilityTable([
    ["si","camisa", 0.1],
    ["si","sueter", 0.1],
    ["si","chaqueta", 0.8],
    ["no","camisa", 0.4],
    ["no","sueter", 0.4],
    ["no","chaqueta", 0.2],
    
],[lluvia.distribution]),name="torso")

# Nodo piernas esta condicionada por la lluvia
piernas = Node(ConditionalProbabilityTable([
    ["si","pantalon", 0.7],
    ["si","sudadera", 0.2],
    ["si","pantaloneta", 0.05],
    ["si","bermuda", 0.05],
    ["no","pantalon", 0.3],
    ["no","sudadera", 0.3],
    ["no","pantaloneta", 0.2],
    ["no","bermuda", 0.2],
    
],[lluvia.distribution]),name="piernas")

# Nodo pies esta condicionada por la lluvia
pies = Node(ConditionalProbabilityTable([
    ["si","clasicos", 0.4],
    ["si","chanclas", 0.05],
    ["si","tenis", 0.55],
    ["no","clasicos", 0.33],
    ["no","chanclas", 0.33],
    ["no","tenis", 0.34]
    
],[lluvia.distribution]),name="pies")

# Nodo de cabeza y torso adecuados esta condicionada por cabeza y torso
cta = Node(ConditionalProbabilityTable([
    ["gorro","camisa","si", 0.2],
    ["gorro","camisa","no", 0.8],
    ["gorro","sueter","si", 0.8],
    ["gorro","sueter","no", 0.2],
    ["gorro","chaqueta","si", 0.7],
    ["gorro","chaqueta","no", 0.3],
    ["gorra","camisa","si", 0.5],
    ["gorra","camisa","no", 0.5],
    ["gorra","sueter","si", 0.9],
    ["gorra","sueter","no", 0.1],
    ["gorra","chaqueta","si", 0.6],
    ["gorra","chaqueta","no", 0.4],
    ["sombrero","camisa","si", 0.8],
    ["sombrero","camisa","no", 0.2],
    ["sombrero","sueter","si", 0.2],
    ["sombrero","sueter","no", 0.8],
    ["sombrero","chaqueta","si", 0.1],
    ["sombrero","chaqueta","no", 0.9],
    ["nada","camisa","si", 0.7],
    ["nada","camisa","no", 0.3],
    ["nada","sueter","si", 0.7],
    ["nada","sueter","no", 0.3],
    ["nada","chaqueta","si", 0.7],
    ["nada","chaqueta","no", 0.3]
    
],[cabeza.distribution, torso.distribution]),name="cta")

# Nodo de piernas y pies adecuados esta condicionada por piernas y pies
ppa = Node(ConditionalProbabilityTable([
    ["pantalon","clasicos","si", 0.9],
    ["pantalon","clasicos","no", 0.1],
    ["pantalon","chanclas","si", 0.3],
    ["pantalon","chanclas","no", 0.7],
    ["pantalon","tenis","si", 0.4],
    ["pantalon","tenis","no", 0.6],
    ["sudadera","clasicos","si", 0.1],
    ["sudadera","clasicos","no", 0.9],
    ["sudadera","chanclas","si", 0.3],
    ["sudadera","chanclas","no", 0.7],
    ["sudadera","tenis","si", 0.9],
    ["sudadera","tenis","no", 0.1],
    ["pantaloneta","clasicos","si", 0.05],
    ["pantaloneta","clasicos","no", 0.95],
    ["pantaloneta","chanclas","si", 0.9],
    ["pantaloneta","chanclas","no", 0.1],
    ["pantaloneta","tenis","si", 0.6],
    ["pantaloneta","tenis","no", 0.4],
    ["bermuda","clasicos","si", 0.7],
    ["bermuda","clasicos","no", 0.3],
    ["bermuda","chanclas","si", 0.7],
    ["bermuda","chanclas","no", 0.3],
    ["bermuda","tenis","si", 0.8],
    ["bermuda","tenis","no", 0.2]
    
],[piernas.distribution, pies.distribution]),name="ppa")

# Nodo de pinta completa adecuada esta condicionada por cabeza - torso adecuados y piernas - piesadecuados
pinta = Node(ConditionalProbabilityTable([
    ["si","si","si", 0.9],
    ["si","si","no", 0.1],
    ["si","no","si", 0.3],
    ["si","no","no", 0.7],
    ["no","si","si", 0.2],
    ["no","si","no", 0.8],
    ["no","no","si", 0.1],
    ["no","no","no", 0.9]
    
],[cta.distribution, ppa.distribution]),name="pinta")

# Creamos una Red Bayesiana y añadimos estados
modelo = BayesianNetwork()
modelo.add_state(vientos) 
"""modelo.add_state(humedad)"""
modelo.add_state(nubosidad)
modelo.add_state(lluvia)
modelo.add_state(cabeza) 
modelo.add_state(torso)
modelo.add_state(piernas)
modelo.add_state(pies)

modelo.add_state(cta) 
modelo.add_state(ppa)
modelo.add_state(pinta)

# Añadimos bordes que conecten nodos
"""modelo.add_edge(vientos, humedad)
modelo.add_edge(humedad, nubosidad)"""
modelo.add_edge(vientos, nubosidad)
modelo.add_edge(nubosidad, lluvia)
modelo.add_edge(lluvia, cabeza)
modelo.add_edge(lluvia, torso)
modelo.add_edge(lluvia, piernas)
modelo.add_edge(lluvia, pies)
modelo.add_edge(cabeza, cta)
modelo.add_edge(torso, cta)
modelo.add_edge(piernas, ppa)
modelo.add_edge(pies, ppa)
modelo.add_edge(cta, pinta)
modelo.add_edge(ppa, pinta)

#Modelo Final
modelo.bake()