from copy import deepcopy

letrasProposicionales=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

class Tree(object):
    def __init__(self, l, iz, der):
        self.left = iz
        self.right = der
        self.label = l

def reglafilas(condinicial):
    reglas=""
    for i in condinicial:
        if i == "F1":
            if condinicial[i]==[1,1]:
                reglas+="CB~AYY"
            if condinicial[i]==[3]:
                reglas+="CBAYY"
            if condinicial[i]==[2]:
                reglas+="CBA~YYC~BAYYO"
            if condinicial[i]==[1]:
                reglas+="CB~A~YYC~BA~YYC~B~AYYOO"
            if condinicial[i]==[0]:
                reglas+="C~B~A~YY"
        if i == "F2":
            if condinicial[i]==[1,1]:
                reglas+="FE~DYY"
            if condinicial[i]==[3]:
                reglas+="FEDYY"
            if condinicial[i]==[2]:
                reglas+="FED~YYF~EDYYO"
            if condinicial[i]==[1]:
                reglas+="FE~D~YYF~ED~YYF~E~DYYOO"
            if condinicial[i]==[0]:
                reglas+="F~E~D~YY"
        if i == "F3":
            if condinicial[i]==[1,1]:
                reglas+="IH~GYY"
            if condinicial[i]==[3]:
                reglas+="IHGYY"
            if condinicial[i]==[2]:
                reglas+="IHG~YYI~HGYYO"
            if condinicial[i]==[1]:
                reglas+="IH~G~YYI~HG~YYI~H~GYYOO"
            if condinicial[i]==[0]:
                reglas+="I~H~G~YY"
    reglas+="YY"
    return reglas

def reglacolumnas(condinicial):
    reglas=""
    for i in condinicial:
        if i == "C1":
            if condinicial[i]==[1,1]:
                reglas+="GD~AYY"
            if condinicial[i]==[3]:
                reglas+="GDAYY"
            if condinicial[i]==[2]:
                reglas+="GDA~YYG~DAYYO"
            if condinicial[i]==[1]:
                reglas+="GD~A~YYG~DA~YYG~D~AYYOO"
            if condinicial[i]==[0]:
                reglas+="G~D~A~YY"
        if i == "C2":
            if condinicial[i]==[1,1]:
                reglas+="HE~BYY"
            if condinicial[i]==[3]:
                reglas+="HEBYY"
            if condinicial[i]==[2]:
                reglas+="HEB~YYH~EBYYO"
            if condinicial[i]==[1]:
                reglas+="HE~B~YYH~EB~YYH~E~BYYOO"
            if condinicial[i]==[0]:
                reglas+="H~E~B~YY"
        if i == "C3":
            if condinicial[i]==[1,1]:
                reglas+="IF~CYY"
            if condinicial[i]==[3]:
                reglas+="IFCYY"
            if condinicial[i]==[2]:
                reglas+="IFC~YYI~FCYYO"
            if condinicial[i]==[1]:
                reglas+="IF~C~YYI~FC~YYI~F~CYYOO"
            if condinicial[i]==[0]:
                reglas+="I~F~C~YY"
    reglas+="YY"
    return reglas

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c,None, None))
        elif c == "~":
            formaux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formaux)
        elif c in conectivos:
            formaux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formaux)
    return pila[-1]

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
    conectivos = ["O", "Y"]
    if f.right == None:
    	return f.label
    elif f.label == "~":
    	return "~"+Inorder(f.right)
    elif f.label in conectivos:
    	return "("+Inorder(f.left)+f.label+Inorder(f.right)+")"
    else:
    	print("Oops, rotulo incorrecto")


def enFNC(A):
    # Subrutina de Tseitin para encontrar la FNC de
    # la formula en la pila
    # Input: A (cadena) de la forma
    #                   p=-q
    #                   p=(qYr)
    #                   p=(qOr)
    #                   p=(q>r)
    # Output: B (cadena), equivalente en FNC
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "~" in A:
        q = A[-1]
        # print('q', q)
        B = "~"+p+"O~"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O~"+p+"Y"+r+"O~"+p+"Y~"+q+"O~"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y~"+r+"O"+p+"Y"+q+"O"+r+"O~"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y~"+r+"O"+p+"Y~"+q+"O"+r+"O~"+p
    else:
        print(u'Error enFNC(): Fórmula incorrecta!')

    return B

def Tseitin(A, letras):
    # Algoritmo de transformacion de Tseitin
    # Input: A (cadena) en notacion inorder
    # Output: B (cadena), Tseitin
    letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
    assert(not bool(set(letras) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    atomos = letras + letrasProposicionalesB
    l = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if s in letras and pila[-1] == '~':
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(atomo + '=~' + s)
            A = A[1:]
            #s = A[0]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            W = pila[-1]
            O = pila[-2]
            V = pila[-3]
            pila = pila[:len(pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            l.append(atomo + "=(" + V + O + W+")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    b = ''
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in l:

        y = enFNC(x)
        b += 'Y' + y
    b = atomo + b

    return b

def Clausula(C):
    # Subrutina Clausula para obtener lista de literales
    # Input: C (cadena) una clausula
    # Output: L (lista), lista de literales
    L=[]
    while len(C)>0:
        s=C[0]
        if s == "O":
            C=C[1:]
        elif s=="~":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

def formaClausal(A):
    # Algoritmo para obtencion de forma clausal
    # Input: A (cadena) en notacion inorder en FNC
    # Output: L (lista), lista de listas de literales
    l = []
    i = 0
    while len(A) > 0:
        if i == len(A) - 1:
            l.append(Clausula(A))
            A = ''
        else:
            if A[i] == 'Y':
                l.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i += 1
    return l

def clausulaUnitaria(lista):#Retorna true si hay una cláusula unitaria.
#Retorna true si hay una cláusula unitaria.
	for n in lista:
		if len(n) == 1:
			return True
	return False

def complemento(literal):
    x=literal
    if x[0]=="~":
        return x[1]
    else:
        return "~"+x

def unitPropagate(clausula, I):#Función que realiza la propagación de la unidad.
	clausulavacia = []
	aux = clausulaUnitaria(clausula)
	while(clausulavacia not in clausula and aux):
		for n in clausula:
			if len(n) == 1:
				l = n[0]
		clausula = [y for y in clausula if l not in y]
		for w in clausula:
			if complemento(l) in w:
				w.remove(complemento(l))
		if l[0] == '~':
			I[l[1]] = 0
		else:
			I[l] = 1
		aux = clausulaUnitaria(clausula)
	return clausula, I

def DPLL(clausula,I):

    clausula=unitPropagate(clausula,I)
    I=unitPropagate(clausula,I)
    clausulavacia=[]
    
    if clausulavacia in clausula:
       return "Insatisfacible",{}
       
    elif len(clausula)==0:
        return "Satisfacible",{}
    
    literal=""
    for i in clausula:
        for x in i:
            if x not in I.keys():
                literal=x
                
    literalc=complemento(literal)
    if literal=="":
        print("error")
        return None
    sp= deepcopy(clausula)
    sp=[n for n in sp if literal not in n]
    
    for m in sp:
        if literalc in m:
            m.remove(literalc)
    ip= deepcopy(I)
    if literal[0]=='~':
        ip[literal[1]]=0
    else:
        ip[literal]=1
        
    clausula1=DPLL(sp,ip)
    I1=DPLL(sp,ip)
    if clausula1=="Satisfacible":
        return clausula1,I1
    else:
        spp=deepcopy(clausula)
        for z in spp:
            if complemento(literal) in z:
                spp.remove(z)
        
        for b in spp:
            if literal in b:
                b.remove(literal)
                
        ipp=deepcopy(I)
        if literal[0]=='~':
            ipp[literal[1]]=0
        else:
            ipp[literal]=1
        
        return DPLL(spp,ipp)
        
    
        
    
       
#------------------------------------------------------------------------------
condinicialesfilas={"F1":[1,1], "F2":[3], "F3":[0]}
condincialescolumnas={"C1":[2],"C2":[1],"C3":[2]}
filas=reglafilas(condinicialesfilas)
columnas=reglacolumnas(condincialescolumnas)
regla_total=filas+columnas+"Y"
prueba_inorder = Inorder(StringtoTree(regla_total))

print("Inorer regla total: ")
print(prueba_inorder)

prueba_tseitin=Tseitin(prueba_inorder, letrasProposicionales)
print("Tseitin regla total: ")
print(prueba_tseitin)

print("\n")

print("Forma Clausal regla total: ")
prueba_clausal=formaClausal(prueba_tseitin)
print(prueba_clausal)

print("\n")

prueba_DPLL=DPLL(prueba_clausal,{})
print(prueba_DPLL)
