from logic import *
class pintaf():
    def __init__(self,cabeza,torso,piernas,zapatos):
        self.cabeza = cabeza
        self.torso = torso
        self.piernas = piernas
        self.zapatos = zapatos
        self.prob = 0
    def add_prob2(self, prob):
        self.prob = prob
    def mostrar2(self):

        print()
        print("cabeza:", self.cabeza.nombre, "Color: ", self.cabeza.color)
        print("torso:", self.torso.nombre, "Color: ", self.torso.color)
        print("piernas:", self.piernas.nombre, "Color: ", self.piernas.color)
        print("pies:", self.zapatos.nombre, "Color: ", self.zapatos.color)
        print()
        
        
def logica_ropa_estilo(prendas,estilo):
    estil = Symbol(estilo)
    estilo_actual = Symbol("estilo_actual")
    conocimiento = And(estilo_actual,estil)
    prendas_logic = []
    for j in prendas:
        estilo_actual = Symbol(j.estilo)
        if model_check(conocimiento,estilo_actual):
            prendas_logic.append(j)
    #for elem in prendas_logic:
        #print(elem.nombre)
    return prendas_logic
def logica_colores(cabeza,torso,piernas,zapatos,prenda):
    ves = []



    #Colores
    
    marron = Symbol("marron")
    negro = Symbol("negro")
    gris = Symbol("gris")
    azul = Symbol("azul")
    rojo = Symbol("rojo")
    verde = Symbol("verde")
    rosa = Symbol("rosa")
    naranja = Symbol("naranja")
    violeta = Symbol("violeta")
    amarillo = Symbol("amarillo")
    morado = Symbol("morado")   
    colores = ["azul","verde","rosa","naranja","violeta","amarillo","morado"]
    tor = Symbol("amarillo")
    pie = Symbol("morado")
    conocimiento1 = Or(     
                      And(And(tor,amarillo),And(pie,morado)))
    tor = Symbol(torso)
    a = model_check(conocimiento1,tor)
    tor = Symbol("morado")
    pie = Symbol("amarillo")
    conocimiento2 = Or(     
                      And(And(tor,morado),And(pie,amarillo)))
    pie = Symbol(piernas)
    b = model_check(conocimiento2,pie)
    tor = Symbol("verde")
    pie = Symbol("rojo")
    conocimiento3 = Or(     
                      And(And(tor,verde),And(pie,rojo)))
    tor = Symbol(torso)
    c = model_check(conocimiento3,tor)
    tor = Symbol("rojo")
    pie = Symbol("verde")
    conocimiento4 = Or(     
                      And(And(tor,rojo),And(pie,verde)))
    pie = Symbol(piernas)
    d = model_check(conocimiento4,pie)
    tor = Symbol("azul")
    pie = Symbol("naranja")
    conocimiento5 = Or(     
                      And(And(tor,azul),And(pie,naranja)))
    tor = Symbol(torso)
    e = model_check(conocimiento5,tor)
    tor = Symbol("naranja")
    pie = Symbol("azul")
    conocimiento6 = Or(     
                      And(And(tor,naranja),And(pie,azul)))
    pie = Symbol(piernas)
    f = model_check(conocimiento6,pie)
    
    pie = Symbol("gris")
    conocimiento7 = And(pie,gris)
    pie = Symbol(piernas)
    g = model_check(conocimiento7,pie)
    pie = Symbol("negro")
    conocimiento8 = And(pie,negro)
    pie = Symbol(piernas)
    h = model_check(conocimiento8,pie)
    pie = Symbol("marron")
    conocimiento17 = And(pie,marron)
    pie = Symbol(piernas)
    r = model_check(conocimiento17,pie)
    
    tor = Symbol("gris")
    conocimiento9 = And(tor,gris)
    tor = Symbol(torso)
    i = model_check(conocimiento9,tor)
    tor = Symbol("negro")
    conocimiento10 = And(tor,negro)
    tor = Symbol(torso)
    j = model_check(conocimiento10,tor)
    tor = Symbol("marron")
    conocimiento16 = And(tor,marron)
    tor = Symbol(torso)
    p = model_check(conocimiento16,tor)
    
    zap = Symbol("gris")
    conocimiento11 = And(zap,gris)
    zap = Symbol(zapatos)
    k = model_check(conocimiento11,zap)
    zap = Symbol("negro")
    conocimiento12 = And(zap,negro)
    zap = Symbol(zapatos)
    l = model_check(conocimiento12,zap)
    zap = Symbol("marron")
    conocimiento18 = And(zap,marron)
    zap = Symbol(zapatos)
    s = model_check(conocimiento18,zap)
    #print(l)
    
    cab = Symbol("gris")
    conocimiento13 = And(cab,gris)
    cab = Symbol(cabeza)
    m = model_check(conocimiento13,cab)
    cab = Symbol("negro")
    conocimiento14 = And(cab,negro)
    cab = Symbol(cabeza)
    n = model_check(conocimiento14,cab)
    cab = Symbol("marron")
    conocimiento15 = And(cab,marron)
    cab = Symbol(cabeza)
    o = model_check(conocimiento15,cab)
    #print(m)
    #print((k or l), (g or h), (m or n))
    for q in colores:

            if torso == q:
                if (k or l or s):
                    if (m or n or o):
                        if (g or h or r) or (a and b) or (c and d) or (e and f):
                            if not prenda in ves:

                                return pintaf(prenda.prendas[0],prenda.prendas[1],prenda.prendas[2],prenda.prendas[3])

            if piernas ==q: 
                if (k or l or s):
                    if (m or n or o):
                        if (i or j or p) or (a and b) or (c and d) or (e and f):
                            if not prenda in ves:

                                return pintaf(prenda.prendas[0],prenda.prendas[1],prenda.prendas[2],prenda.prendas[3])

    if (k or l or s):
        if (m or n or o):
            if (i or j or p or g or h or r):
                return pintaf(prenda.prendas[0],prenda.prendas[1],prenda.prendas[2],prenda.prendas[3])
                

        

  



    
    
