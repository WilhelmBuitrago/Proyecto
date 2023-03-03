from logica import *
from probability import *

class Node():
    def __init__(self, prenda, padre):
        self.prenda = prenda
        self.padre = padre

class Prenda():
    def __init__(self, tipo, estilo, color, sub_tipo, nombre):
        self.color = color
        self.estilo = estilo
        self.tipo = tipo
        self.nombre = nombre
        self.sub_tipo = sub_tipo

class Pintas():
    def __init__(self):
        self.pintas = []

    def add_pinta(self, pinta):
        self.pintas.append(pinta)
    
    def mostar(self):
        for contador, pinta in enumerate(self.pintas):
            lista = []
            for prenda in pinta.prendas:
                lista.append(prenda.nombre)
            print(f"Pinta numero {contador+1}.\n{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}\n")

    def get_first(self):
        for i in self.pintas:
            return i

class Pinta():
    def __init__(self):
        self.prendas = []
        self.tipos = []
        self.prob = 0
    
    def add_prenda(self, prenda):
        self.prendas.append(prenda)
        self.tipos.append(prenda.tipo)
    
    def add_prob(self, prob):
        self.prob = prob

    def mostrar(self):
        for prenda in self.prendas:
            print(prenda.nombre)

    def ordenar(self):
        self.prendas.reverse()
        
    def tipo_en_pinta(self, tipo):
        x = False
        if tipo in self.tipos:
            x |= True
        else:
            x |= False
        return x

class Frontera():
    def __init__(self):
        self.frontera =[]
    
    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, prenda):
        self.frontera.append(prenda)

    def mostrar(self):
        print("Tu frontera tiene: ")
        for i in self.frontera:
            print(i.nombre)
            
    def primer_elemento(self):
        return self.frontera[0]
    
    def eliminar(self):
        pass

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class Pila(Frontera):
    def eliminar(self):
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            nodo = self.frontera[-1]
            self.frontera = self.frontera[:-1]
            return nodo
    
class Cola(Frontera):
    def eliminar(self):
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            nodo = self.frontera[0]
            self.frontera = self.frontera[1:]
            return nodo

class Combination2():

    def __init__(self, estilo, viento, nubosidad, lluvia):
        # formato: tipo, estilo, color, nombre 
        with open('Prendas.txt') as file:
            contenido = file.read()
        contenido = contenido.splitlines()  
        
        self.clothes = []
        self.estilo_deseado = estilo
        self.viento = viento
        self.nubosidad = nubosidad
        self.lluvia = lluvia       
        
        for i in contenido:
            tipo, estilo, color, sub_tipo, nombre = i.split(", ")
            self.clothes.append(Prenda(tipo, estilo, color, sub_tipo, nombre))

        #self.clothes = logica_ropa_estilo(self.clothes, self.estilo_deseado)

    def modelo_trans(self, tipo):
        
        acciones = {
            None : "cabeza",
            "cabeza":"torso",
            "torso":"piernas",
            "piernas":"zapatos"
        }
        
        tipo_sig = acciones[tipo]
        prendas_posibles = []

        for prenda in self.clothes:
            if prenda.estilo == self.estilo_deseado and prenda.tipo == tipo_sig:
                prendas_posibles.append(prenda)

        return prendas_posibles
    
    def solve(self):

        frontera = Pila()
        #pinta = Pinta()
        pintas = Pintas()
        
        # Usar el modelo de transicion para hallar las cabezas que cumplan con el tipo deseado
        prendas_posibles = self.modelo_trans(None)

        # Añadir las cabezas a la frontera sin padres
        for i in prendas_posibles:
            frontera.add(Node(i,None))
            #print(f"añadio: {i.nombre}")

        while not frontera.empty():

            # Extraer un nodo de la frontera                        
            nodo = frontera.eliminar()

            #print(f"extrajo: {nodo.prenda.nombre}")
            tipo_prenda_actual = nodo.prenda.tipo

            # Si el tipo es diferente de zapatos se hallan las prendas disponibles y se introducen a la frontera
            if tipo_prenda_actual != "zapatos":
                prendas_posibles = self.modelo_trans(tipo_prenda_actual)
                for i in prendas_posibles:
                    frontera.add(Node(i, nodo))
                    #print(f"añadio: {i.nombre}")

            # En caso de que no significa que llegó a los zapatos, con esto se guarda la combinacion actual como una lista en pintas
            else:
                nodo2 = nodo
                pint = Pinta()
                for i in range(4):
                    pint.add_prenda(nodo2.prenda)                    
                    nodo2 = nodo2.padre
                pint.ordenar()
                pintas.add_pinta(pint)

            #if not pinta.tipo_en_pinta(nodo.prenda.tipo):
            #    pinta.add_prenda(nodo.prenda)
        
        #pintas.mostar()
        """
        conjun = []
        
        for combinacion in pintas.pintas:
            zapato = combinacion.prendas[3].color
            piernas = combinacion.prendas[2].color
            torso = combinacion.prendas[1].color
            cabeza = combinacion.prendas[0].color
            #print(zapato, piernas, torso, cabeza)
        
            a = logica_colores(cabeza,torso,piernas,zapato,combinacion)
            if a != None:
                conjun.append(a)
                
        for i,prenda in enumerate(conjun):
            print("prenda No {}".format(i + 1))
            print("cabeza:", prenda.cabeza.nombre, "Color: ", prenda.cabeza.color)
            print("torso:", prenda.torso.nombre, "Color: ", prenda.torso.color)
            print("piernas:", prenda.piernas.nombre, "Color: ", prenda.piernas.color)
            print("pies:", prenda.zapatos.nombre, "Color: ", prenda.zapatos.color)
            print()"""
        best = pintas.get_first()

        for contador, pinta in enumerate(pintas.pintas):
            lista = []
            for prenda in pinta.prendas:
                lista.append(prenda.sub_tipo)
            prob = probability(self.viento, self.nubosidad, self.lluvia, lista)
            #print(f"probabilidad de la pinta {contador+1}: {prob*100:.0f}")
            pinta.add_prob(prob)
            
            if pinta.prob > best.prob:
                best = pinta
        
        print(f"la mejor pinta, con un {best.prob*100:.0f}% tiene:")
        best.mostrar()


        
            
        #pinta.mostrar(self.estilo_deseado) 

#viento, nubosidad, lluvia, pinta):

estilo_deseado = "casual"
viento = {"vientos": "si"}
nubosidad = {"nubosidad": "si"}
lluvia = {"lluvia": "no"}

comb = Combination2(estilo_deseado, viento, nubosidad, lluvia)
comb.solve()