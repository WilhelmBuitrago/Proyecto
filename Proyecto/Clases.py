from logic import *
from logica import *
class Node():
    def __init__(self, prenda, padre):
        self.prenda = prenda
        self.padre = padre
        self.accion = prenda.tipo

class Prenda():
    def __init__(self, tipo, estilo, color, nombre):
        self.color = color
        self.estilo = estilo
        self.tipo = tipo
        self.nombre = nombre

class Pintas():
    def __init__(self):
        self.pintas = []

    def add_pinta(self, pinta):
        self.pintas.append(pinta)
    
    def mostar(self):
        for contador, pinta in enumerate(self.pintas):
            lista = []
            for j in pinta:
                lista.append(j.nombre)
            print(f"Pinta numero {contador+1}.\n{lista[3]}, {lista[2]}, {lista[1]}, {lista[0]}\n")

class Pinta():
    def __init__(self):
        self.prendas = []
        self.tipos = []
    
    def add_prenda(self, prenda):
        self.prendas.append(prenda)
        self.tipos.append(prenda.tipo)

    def mostrar(self, estilo):
        print(f"Tu pinta con estilo {estilo}, tiene: ")
        for prenda in self.prendas:
            print(prenda.nombre)

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

    def __init__(self, estilo):
        # formato: tipo, estilo, color, nombre 
        with open('C:\\Users\\wilhe\\OneDrive\\Escritorio\\Nueva carpeta (4)\\Prendas.txt') as file:
            contenido = file.read()
        contenido = contenido.splitlines()  
        
        self.clothes = []
        self.estilo_deseado = estilo
        
        
        
        
        #print(formal)
        for i in contenido:
            tipo, estilo, color, nombre = i.split(", ")
            self.clothes.append(Prenda(tipo, estilo, color, nombre))

        self.clothes = logica_ropa(self.clothes,self.estilo_deseado)
        
        """
        conocimiento = And(estilo_actual,estil)
        
        for j in self.clothes:
            estilo_actual = Symbol(j.estilo)
            if model_check(conocimiento,estilo_actual):
                print(j.nombre)
        """    
            
                
            
    
    def modelo_trans(self, tipo):
        
        acciones = {
            None : "cabeza",
            "cabeza":"torso",
            "torso":"piernas",
            "piernas":"pies"
        }
        
        tipo_sig = acciones[tipo]
        prendas_posibles = []

        for prenda in self.clothes:
            if prenda.estilo == self.estilo_deseado and prenda.tipo == tipo_sig:
                prendas_posibles.append(prenda)

        #for i in prendas_posibles:
        #    print(i.nombre)

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

            # Si el tipo es diferente de pies se hallan las prendas disponibles y se introducen a la frontera
            if tipo_prenda_actual != "pies":
                prendas_posibles = self.modelo_trans(tipo_prenda_actual)
                for i in prendas_posibles:
                    frontera.add(Node(i, nodo))
                    #print(f"añadio {i.nombre}")

            # En caso de que no significa que llegó a los pies, con esto se guarda la combinacion actual como una lista en pintas
            else:
                nodo2 = nodo
                lista = []
                for i in range(4):
                    lista.append(nodo2.prenda)                    
                    nodo2 = nodo2.padre
                pintas.add_pinta(lista)

            #if not pinta.tipo_en_pinta(nodo.prenda.tipo):
            #    pinta.add_prenda(nodo.prenda)
        pintas.mostar()

            
        #pinta.mostrar(self.estilo_deseado) 

comb = Combination2("formal")
comb.solve()