from pomegranate import *

# pip install pomegranate
# Si no funciona hay q instalar Microsoft Visual C++ 14 o mayor

# Nodo vientos, no tiene padres
vientos = Node(DiscreteDistribution({
    "si": 0.4,
    "no": 0.6
}), name="vientos")

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
cabeza = Node(DiscreteDistribution({
    "gorro": 0.2,
    "gorra": 0.3,
    "sombrero": 0.2,
    "nada": 0.3
}), name="cabeza")

# Nodo torso esta condicionada por la lluvia
torso = Node(DiscreteDistribution({
    "camisa": 0.5,
    "sueter": 0.3,
    "chaqueta": 0.2
}), name="torso")

# Nodo piernas esta condicionada por la lluvia
piernas = Node(DiscreteDistribution({
    "pantalon": 0.4,
    "sudadera": 0.2,
    "pantaloneta": 0.2,
    "bermuda": 0.4
}), name="piernas")

# Nodo pies esta condicionada por la lluvia
pies = Node(DiscreteDistribution({
    "clasicos": 0.4,
    "chanclas": 0.2,
    "tenis": 0.4
}), name="torso")

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
    ["si","si","si","si", 0.9],
    ["si","si","si","no", 0.1],
    ["si","si","no","si", 0.3],
    ["si","si","no","no", 0.7],
    ["si","no","si","si", 0.2],
    ["si","no","si","no", 0.8],
    ["si","no","no","si", 0.1],
    ["si","no","no","no", 0.9],
    ["no","si","si","si", 0.6],
    ["no","si","si","no", 0.4],
    ["no","si","no","si", 0.3],
    ["no","si","no","no", 0.7],
    ["no","no","si","si", 0.8],
    ["no","no","si","no", 0.2],
    ["no","no","no","si", 0.2],
    ["no","no","no","no", 0.8]
    
],[lluvia.distribution, cta.distribution, ppa.distribution]),name="pinta")

# Creamos una Red Bayesiana y añadimos estados
modelo = BayesianNetwork()
modelo.add_state(vientos) 
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
modelo.add_edge(vientos, nubosidad)
modelo.add_edge(nubosidad, lluvia)
modelo.add_edge(cabeza, cta)
modelo.add_edge(torso, cta)
modelo.add_edge(piernas, ppa)
modelo.add_edge(pies, ppa)
modelo.add_edge(cta, pinta)
modelo.add_edge(ppa, pinta)
modelo.add_edge(lluvia, pinta)

#Modelo Final
modelo.bake()
