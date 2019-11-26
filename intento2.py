

def reglacolumna1(lista):
    regla=""
    if lista==[1,1]:
        regla.append("GD~AYY")
    elif lista==[1]:
        regla.append("GD~A~YYG~DA~YYG~D~AYYOO")
    elif lista==[2]:
        regla.append("GDA~YYG~DAYYO")
    elif lista==[3]:
        regla.append("(AYDYG)")
    elif lista==[0]
        regla.append("(-AY-DY-G)")
    return regla

def reglacolumna2(lista):
    regla=""
    if lista==[1,1]:
        regla.append("HE~BYY")
    elif lista==[1]:
        regla.append("HE~B~YYH~EB~YYH~E~BYYOO")
    elif lista==[2]:
        regla.append("HEB~YYH~EBYYO")
    elif lista==[3]:
        regla.append("(HYEYB)")
    elif lista==[0]:
        regla.append("(H~YE~YB~)")
    return regla

def reglacolumna3(lista):
    regla=""
    if lista==[1,1]:
        regla.append("IF~CYY")
    elif lista==[1]:
        regla.append("IF~C~YYI~FC~YYI~F~CYYOO")
    elif lista==[2]:
        regla.append("IFC~YYI~FCYYO")
    elif lista==[3]:
        regla.append("IYFYC")
    elif lista==[0]:
        regla.append("I~YF~YC~")
    return regla

def reglafila1(lista):
    regla=""
    if lista==[1,1]:
        regla.append("CB~AYY")
    elif lista==[1]:
        regla.append("CB~A~YYC~BA~YYC~B~AYYOO")
    elif lista==[2]:
        regla.append("CBA~YYC~BAYYO")
    elif lista==[3]:
        regla.append("CBAYY")
    elif lista==[0]:
        regla.append("C~B~A~YY")
    return regla

def reglafila2(lista):
    regla=""
    if lista==[1,1]:
        regla.append("FE~DYY)")
    elif lista==[1]:
        regla.append("FE~D~YYF~ED~YYF~E~DYYOO")
    elif lista==[2]:
        regla.append("FED~YYF~EDYYO")
    elif lista==[3]:
        regla.append("FEDYY")
    else:
        regla.append("F~E~D~YY")
    return regla

def reglafila3(lista):
    regla=""
    if lista==(1,1):
        regla.append("IH~GYY")
    elif lista==[1]:
        regla.append("IH~G~YYI~HG~YYI~H~GYYOO")
    elif lista==[2]:
        regla.append("IHG~YYI~HGYYO")
    elif lista==[3]:
        regla.append("IHGYY")
    else:
        regla.append("I~H~G~YY")
    return regla
