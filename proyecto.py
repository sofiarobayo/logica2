# -*- coding: utf-8 -*-
class Tree(object):
    def __init__(self, l, iz, der):
        self.left = iz
        self.right = der
        self.label = l

def letrasproposicionales(listafilas,listacolumna):
    cosito=[]
    for s in listafilas:
        for c in listacolumna:
            cosito.append(s+c)
    return cosito

def reglafilas (letrasproposicionales,listafilas,diccionario):
    reglam=""
    for h in listafilas:
        aux=[x for x in letrasproposicionales if x[1]==h]
        for r in aux:
            if diccionario[h]==[1,1]:
                reglam=aux[2]+aux[1]+"~"+aux[1]+"YY"
            if diccionario[h]==[3]:
                reglam=aux[2]+aux[1]+aux[0]+"YY"
            if diccionario[h]==[0]:
                reglam=aux[2]+"~"+aux[1]+"~"+aux[0]+"~YY"
            if diccionario[h]==[1]:
                reglam=aux[2]+aux[1]+"~"+aux[0]+"~"+"YY"+aux[2]+"~"+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+"~"+aux[0]+"YYOO"
            if diccionario[h]==[2]:
                reglam=aux[2]+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+aux[0]+"YYO"
    return reglam

def reglascolumnas(letrasproposicionales,listacolumnas,diccionario):
    reglam=""
    for k in listacolumnas:
        aux2=[y for y in letrasproposicionales if y[1]==k]
        for d in aux2:
            if diccionario[k]==[1,1]:
                reglam=aux[2]+aux[1]+"~"+aux[1]+"YY"
            if diccionario[k]==[3]:
                reglam=aux[2]+aux[1]+aux[0]+"YY"
            if diccionario[k]==[0]:
                reglam=aux[2]+"~"+aux[1]+"~"+aux[0]+"~YY"
            if diccionario[k]==[1]:
                reglam=aux[2]+aux[1]+"~"+aux[0]+"~"+"YY"+aux[2]+"~"+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+"~"+aux[0]+"YYOO"
            if diccionario[k]==[2]:
                reglam=aux[2]+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+aux[0]+"YYO"
    return reglam

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y']
    pila = []
    for c in A:
        if c in letras:
            pila.append(Tree(c,None, None))
        elif c == "~":
            formaux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formaux)
        elif c in conectivos:
            formaux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-2]
            pila.append(formaux)
    return stack[-1]


def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '~':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def Tseitin(A, letras):
    # Algoritmo de transformacion de Tseitin
    # Input: A (cadena) en notacion inorder
    # Output: B (cadena), Tseitin
    letrasProposicionalesB = [chr(x) for x in range(256, 300)]
    assert(not bool(set(letras) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    l = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if s in letras and pila[-1] == '-':
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(atomo + '=-' + s)
            A = A[1:]
            s = A[0]
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
        elif s=="-":
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

def compllit(literal):
    if literal[0]=="~":
        return literal[1]
    else:
        literal="~"+literal
        return literal

def DPLL(lista,interpretaciones):
    lista=unitPropagate(lista,interpretaciones)
    interpretaciones=unitPropagate(lista,interpretaciones)
    if(len(lista)==0):
        last=lista
        ifinal=interpretaciones
        return(lista,interpretaciones)
    elif("" in lista):
        last=lista
        ifinal=interpretaciones
        return(lista,{})
    else:
        temporaria=[x for x in lista]
        for l in temporaria[0]:
            if(len(temporaria)==0):
                return(temporaria, interpretaciones)
            if(l not in interpretaciones.keys() and l!= '~'):
                break
        temporaria.insert(0,1)
        lista2= DPLL(temporaria,interpretaciones)
        interpretaciones2=DPLL(temporaria,interpretaciones)
        if interpretaciones2=={}:
            temporaria=[x for x in lista]
            a=compllit(l)
            temporaria.insert(0,a)
            lista2=DPLL(temporaria,interpretaciones)
            interpretaciones2= DPLL(temporaria,interpretaciones)
        return (lista2,interpretaciones2)

    return 0
def clausUnit(lista):
    for v in lista:
        if (len(v)==1):
            return i
        elif ((len(i)==2) and i=="~"):
            return i
    return None

def clausvacia(lista):
    for q in lista:
        if (q==''):
            return True
    return False

def unitPropagate(lista, interpretaciones):
    x=clausUnit(lista)
    while(x!= None and clausvacia(lista)!=True):
        if(len(x)==1):
            interpretaciones[str(x)]=1
            e=0
            for d in range(0,len(lista)):
                lista[d]=re.sub('~'+x,'',lista[d])
            for d in range(0,len(lista)):
                if(x in lista [d-e]):
                    e+=1
        else:
            interpretaciones[str(x[1])]=0
            e=0
            for d in range(0,len(lista)):
                if(x in lista[d-e]):
                    lista.remove(lista[d-e])
                    e+=1
            for d in range(0,len(lista)):
                lista[d]=re.sub(x[1],'',lista[d])
        x=clausUnit(lista)
    return (lista,interpretaciones)


listafilas=['A','B','C']
#print(listafilas)
listacolumnas=['1','2','3']
#print(listacolumnas)
diccionario={"A":[1,1],"B":[3],"C":[0],"1":[2],"2":[1],"3":[2]}
letras = letrasproposicionales(listafilas, listacolumnas)
print(letras)
prueba=reglafilas(letras,listafilas,diccionario)
print(prueba)
