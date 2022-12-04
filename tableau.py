from termcolor import *
import colorama

"│   ┌  ─ ┐  └────────────────────────────────────────────┘ ┴ ┬"
colorama.init()

def chapeau_haut(col):
    cprint("┌──────────────────────────────","white",end="")
    for i in range(0,col-1):
        cprint("┬──────────────────────────────","white",end="")
    cprint("┐","white")

def chapeau_bas(col):
    cprint("├──────────────────────────────","white",end="")
    for i in range(0,col-1):
        cprint("┼──────────────────────────────","white",end="")
    cprint("┤","white")

def valeurs_tableau(l):
    for i in range(len(l)):
        cprint("│","white",end="")
        cprint(l[i],"white",end="")
        cprint(" "*(30-len(str(l[i]))),end="")
    cprint("│","white")
    
def tableau(l):
    chapeau_haut(len(l))
    valeurs_tableau(l)
    chapeau_bas(len(l))

def get_col(cmd):
    cmd=cmd.split(",")
    res=[]
    for t in cmd:
        r=t.split(' ')
        for f in r:
            if not(f.lower()=="select" or f.lower()=="from"):
                f2=list(f)[0].upper()
                f3="".join(list(f)[1::])
                f=f2+f3
                res.append(f)
            if f.lower()=="from": 
                res=get_all(cmd,res)
                return res
    res=get_all(cmd,res)
    return res

def get_all(cmd,res):
    if res[0]!="*":
        return res
    for t in cmd:
        r=t.split(' ')
        trouvé=0
        for f in r:
            if trouvé==1:
                tableau=f
                trouvé=2
            if f.lower()=="from":
                trouvé=1
    if tableau=="LesJoueurs":
        return ["numLicence","Nom","Prenom","Age","Club"]
    elif tableau=="LesClubs":
        return ["Sigle","Nom","Ville"]
    elif tableau=="LesTournois":
        return ["idTournoi","date","nomTournoi","Club","nbPlaces","Prix"]
    elif tableau=="LesGymnases":
        return ["nomGymnase","Ville","nbTerrains","nbTapis"]
    elif tableau=="LesMatchs":
        return ["idTournoi","date","numeroMatch","numeroLicenceVainqueur","numeroLicencePerdant","nbSets"]
    elif tableau=="LesInscriptions":
        return ["idTournoi","numeroLicence","paiement"]
    elif tableau=="LesGymnasesTournois":
        return ["idTournoi","nomGymnase"]
    return res

def get_atrbs(tableau):
    if tableau=="LesJoueurs":
        return ["numLicence","Nom","Prenom","Age","sigleClub"]
    elif tableau=="LesClubs":
        return ["SigleClub","NomClub","Ville"]
    elif tableau=="LesTournois":
        return ["idTournoi","date","nomTournoi","Club","nbPlaces","Prix"]
    elif tableau=="LesGymnases":
        return ["nomGymnase","Ville","nbTerrains","nbTapis"]
    elif tableau=="LesMatchs":
        return ["idTournoi","date","numeroMatch","numeroLicenceVainqueur","numeroLicencePerdant","nbSets"]
    elif tableau=="LesInscriptions":
        return ["idTournoi","numeroLicence","paiement"]
    elif tableau=="LesGymnasesTournois":
        return ["idTournoi","nomGymnase"]
    else:
        cprint("ERREUR FICHIER NON CONNU")
        return []




