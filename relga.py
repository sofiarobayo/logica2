

def reglacolumna1(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+={value for value in variable}
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(AY-DYG)")
        elif lista==(1):
            regla.append("(AY-DY-G)O(-AYDY-G)O(-AY-DYG)")
        elif lista==(2):
            regla.append("(AYDY-G)O(-AYDYG)")
        elif lista==(3):
            regla.append("(AYDYG)")
        else:
            regla.append("(-AY-DY-G)")
    return regla

def reglacolumna2(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+=s
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(BY-EYH)")
        elif lista==(1):
            regla.append("(BY-EY-H)O(-BYEY-H)O(-BY-EYH)")
        elif lista==(2):
            regla.append("(BYEY-H)O(-BYEYH)")
        elif lista==(3):
            regla.append("(BYEYH)")
        else:
            regla.append("(-BY-EY-H)")
    return regla

def reglacolumna3(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+=s
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(CY-FYI)")
        elif lista==(1):
            regla.append("(CY-FY-I)O(-CYFY-I)O(-CY-FYI)")
        elif lista==(2):
            regla.append("(CYFY-I)O(-CYFYI)")
        elif lista==(3):
            regla.append("(CYFYI)")
        else:
            regla.append("(-CY-FY-I)")
    return regla

def reglafila1(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+=s
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(AY-BYC)")
        elif lista==(1):
            regla.append("(AY-BY-C)O(-AYBY-C)O(-AY-BYC)")
        elif lista==(2):
            regla.append("(AYBY-C)O(-AYBYC)")
        elif lista==(3):
            regla.append("(AYBYC)")
        else:
            regla.append("(-AY-BY-C)")
    return regla

def reglafila2(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+=s
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(DY-EYF)")
        elif lista==(1):
            regla.append("(DY-EY-F)O(-DYEY-F)O(-DY-EYF)")
        elif lista==(2):
            regla.append("(DYEY-F)O(-DYEYF)")
        elif lista==(3):
            regla.append("(DYEYF)")
        else:
            regla.append("(-DY-EY-F)")
    return regla

def reglafila3(lista):
    sum=0
    regla=[]
    for s in lista:
        sum+=s
    if sum >3:
        print("errror")
    else:
        if lista==(1,1):
            regla.append("(GY-HYI)")
        elif lista==(1):
            regla.append("(GY-HY-I)O(-GYHY-I)O(-GY-HYI)")
        elif lista==(2):
            regla.append("(GYHY-I)O(-GYHYI)")
        elif lista==(3):
            regla.append("(GYHYI)")
        else:
            regla.append("-GY-HY-I")
    return regla

def polacainversa(listaconreglas):
