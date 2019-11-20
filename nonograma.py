
def letrasproposicionales(listafilas,listacolumna):
    cosito=[]
    for s in listafilas:
        for c in listacolumna:
            cosito.append(s+c)
    return cosito



def reglafilas (letrasproposicionales,listafilas,diccionario):
    reglam=""
    for h in listafilas:
        aux=[x for x in letrasproposicionales if x[1]=='1']
        if diccionario[h]==[1,1]:
            reglam=aux[2]+aux[1]+"~"+aux[1]+"YY"
        elif diccionario[h]==[3]:
            reglam=aux[2]+aux[1]+aux[0]+"YY"
        elif diccionario[h]==[0]:
            reglam=aux[2]+"~"+aux[1]+"~"+aux[0]+"~YY"
        elif diccionario[h]==[1]:
            reglam=aux[2]+aux[1]+"~"+aux[0]+"~"+"YY"+aux[2]+"~"+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+"~"+aux[0]+"YYOO"
        elif diccionario[h]==[2]:
            reglam=aux[2]+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+aux[0]+"YYO"
    return reglam

def reglascolumnas(letrasproposicionales,listacolumnas,diccionario):
    reglam=""
    for k in listacolumnas:
        aux2=[y for y in letras porposicionales if y[1]=='1']
        if diccionario[k]==[1,1]:
            reglam=aux[2]+aux[1]+"~"+aux[1]+"YY"
        elif diccionario[k]==[3]:
            reglam=aux[2]+aux[1]+aux[0]+"YY"
        elif diccionario[k]==[0]:
            reglam=aux[2]+"~"+aux[1]+"~"+aux[0]+"~YY"
        elif diccionario[k]==[1]:
            reglam=aux[2]+aux[1]+"~"+aux[0]+"~"+"YY"+aux[2]+"~"+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+"~"+aux[0]+"YYOO"
        elif diccionario[k]==[2]:
            reglam=aux[2]+aux[1]+aux[0]+"~YY"+aux[2]+"~"+aux[1]+aux[0]+"YYO"    
    return reglam
        
def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    delimeter = ','
    conectivos = ['~', 'O', 'Y']
    pila = []
    letra = ""
    for c in A:
        if c not in conectivos and c != delimeter:
            letra += c
        elif c == delimeter:
            if letra in letrasProposicionales:
                pila.append(Tree(letra, None, None))
            letra = ""
        else :
            if c == '~':
                formulaAux = Tree(c, None, pila[-1])
                del pila[-1]
                pila.append(formulaAux)
            elif c in conectivos and c != '~':
                formulaAux = Tree(c, pila[-1], pila[-2])
                del pila[-1]
                del pila[-1]
                pila.append(formulaAux)
    return pila[-1]
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
    
def tseiting(parametro):
    return 0

def formaclausal(parametro):
    return 0

def DPLL(parametro):
    return 0

def unitPropagate(parametro):
    return 0


listafilas=['A','B','C']
listacolumnas=['1','2','3']
diccionario={"A":[1,1],"B":[3],"C":[0],"1":[2],"2":[1],"3":[2]}
letras = letrasproposicionales(listafilas, listacolumna)
#print(letras)
prueba=reglafilas(letras,listafilas,diccionario)
#print(prueba)
