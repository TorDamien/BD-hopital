import sqlite3
from termcolor import *
import colorama
import os
colorama.init()

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def accueil():
    cprint("┌────────────────────────────────────────────────────────┐","blue")
    cprint("│    UI Haut Niveau ~~ Aucune connaissance SQL requise   │","blue")
    cprint("└────────────────────────────────────────────────────────┘","blue")

def ask():
    response=""
    while not response.lower() in ["c","j","t","q"]:
        cprint("┌──────────────────────────────────────────────────────────────────────────────────┐","white")
        cprint("│    Votre requête concerne-t-elle un club [c] ? Un joueur [j] ? Un tournoi ? [t]  │","white")
        cprint("└──────────────────────────────────────────────────────────────────────────────────┘","white")
        cprint("Pour sortir, tapez 'q'","red")
        cprint(">>>","green",end="")
        response=input("")
        if response.lower()=="q":
            return -1
        if response.lower() in ["c","j","t"]:
            return response.lower()
        
def une_info_connue(j,cur,con):
    clear()
    cprint("Veuillez saisir l'information que vous possédez sur le joueur","white")
    info=""
    while info=="":
        cprint(">>>","green",end="")
        info=input("")
    if j=="l":
        player_screen_licence(info,cur,con)
    if j=="n":
        player_screen_nom(info,cur,con)

def exec(cmd):
    con = sqlite3.connect("projetfinal.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    res=cur.execute(cmd)
    l=[]
    if res.fetchone==None:
        return l
    for row in res:
        for col in row:
            l.append(col)
    return l

def print_player(l,lt,club,matchs):
    clear()
    cprint("┌──────────────────────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                      FICHE JOUEUR DE {l[2]} {l[1]}","white",end="")
    cprint(" "*(43-len(list(l[2]+l[1])))+"│","white")
    cprint("└──────────────────────────────────────────────────────────────────────────────────┘","white")
    cprint(f"NUMERO DE LICENCE:","blue",end=" ")
    cprint(f"{l[0]}","white")
    cprint(f"AGE:","blue",end=" ")
    cprint(f"{l[3]}","white")
    cprint(f"CLUB:","blue",end=" ")
    cprint(f"{club[0]}","white")
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                            TOURNOIS                            │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(lt)-1:
        cprint(f"{lt[t]}"+" "*(30-len(lt[t]))+f"=> {lt[t+1]}","white")   
        t=t+2
    t=0
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                        MATCHS DISPUTES                         │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    m=[0,0]
    while t<len(matchs)-1:
        if int(matchs[t+2])==int(l[0]):
            cmd=f"SELECT nom,prenom FROM LesJoueurs WHERE numLicence={matchs[t+3]}"
            adv=exec(cmd)
            cprint(f"Victoire en {matchs[t+4]} sets face à {adv[1]} {adv[0]} ({matchs[t+6]})","white")
            m[0]+=1
        else:
            cmd=f"SELECT nom,prenom FROM LesJoueurs WHERE numLicence={matchs[t+2]}"
            adv=exec(cmd)
            cprint(f"Défaite en {matchs[t+4]} sets face à {adv[1]} {adv[0]} ({matchs[t+6]})","white")
        t=t+10
        m[1]+=1
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                             STATS                              │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    cprint(f"NOMBRES DE MATCHS DISPUTES:","blue",end=" ")
    cprint(f"{m[1]}","white")
    cprint(f"NOMBRES DE MATCHS REMPORTES:","blue",end=" ")
    cprint(f"{m[0]}","white")
    cprint(f"POURCENTAGE DE VICTOIRE:","blue",end=" ")
    if m[1]==0:
        cprint(f"0 %","white")
    else:
        cprint(f"{round(m[0]/m[1]*100)}%","white")
    print("\n\n\n\n")
    
def player_screen_licence(info,cur,con):
    cmd=f"SELECT * FROM LesJoueurs WHERE numLicence={info}"
    l=exec(cmd)
    if l==[]:
        cprint(f"Vous avez surement du commettre une erreur dans la saisie des informations... Aucun joueur n'a été trouvé avec la licence {info}...","red")
        return
    cmd=f"SELECT DISTINCT nomTournoi,date FROM LesInscriptions JOIN LesTournois USING (idTournoi) WHERE numLicence={info}"
    l2=exec(cmd)
    cmd=f"SELECT DISTINCT nomClub FROM LesClubs WHERE sigleClub='{l[4]}'"
    club=exec(cmd)
    cmd=f"SELECT DISTINCT * FROM LesMatchs JOIN LesTournois USING (idTournoi) WHERE (licenceVainqueur={info} OR licencePerdant={info})"
    matchs=exec(cmd)
    print_player(l,l2,club,matchs)
    
def player_screen_nom(info,cur,con):
    info="".join([list(info)[0].upper(),"".join(list(info)[1:])])
    cmd=f"SELECT * FROM LesJoueurs WHERE nom='{info}'"
    l=exec(cmd)
    if l==[]:
        cprint(f"Vous avez surement du commettre une erreur dans la saisie des informations... Aucun joueur n'a été trouvé avec le nom {info}...","red")
        return
    cmd=f"SELECT DISTINCT nomTournoi,date FROM LesInscriptions JOIN LesTournois USING (idTournoi) WHERE numLicence={l[0]}"
    l2=exec(cmd)
    cmd=f"SELECT DISTINCT nomClub FROM LesClubs WHERE sigleClub='{l[4]}'"
    club=exec(cmd)
    cmd=f"SELECT DISTINCT * FROM LesMatchs JOIN LesTournois USING (idTournoi) WHERE (licenceVainqueur={l[0]} OR licencePerdant={l[0]})"
    matchs=exec(cmd)
    print_player(l,l2,club,matchs)

def get_joueur(cur,con):   
    cprint("Connaissez vous le numéro de licence [l] ou le nom [n] du joueur ? [0] si aucune information connue","white")
    j="1"   
    while j.lower() not in ["l","n","0"]:
        cprint(">>>","green",end="")
        j=input("")
        if j.lower() not in ["l","n","0"]:
            cprint("Erreur entrée: [l/n/0]","red")
    if j.lower()!="0":
        une_info_connue(j,cur,con)
    else:
        cprint("Pour retrouver un joueur, il est nécessaire d'avoir soit:\n\t-son numéro de licence\n\t-son nom de famille","white")
    
def print_club(j):
    cmd=f"SELECT * FROM LesClubs WHERE sigleClub='{j}'"
    l=exec(cmd)
    if l==[]:
        cprint("Erreur dans la saisie du sigle du club","red")
        return
    cmd=f"SELECT nomTournoi,date FROM LesTournois WHERE sigleClub='{j}'"
    to=exec(cmd)
    cmd=f"SELECT COUNT(nom) FROM LesJoueurs WHERE sigleClub='{j}'"
    nb=exec(cmd)
    cmd=f"SELECT prenom,nom FROM LesJoueurs WHERE sigleClub='{j}'"
    jo=exec(cmd)
    clear()
    cprint("┌──────────────────────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                      FICHE CLUB DE {l[1]}","white",end="")
    cprint(" "*(46-len(list(l[1])))+"│","white")
    cprint("└──────────────────────────────────────────────────────────────────────────────────┘","white")
    cprint(f"SIGLE:","blue",end=" ")
    cprint(f"{l[0]}","white")
    cprint(f"VILLE:","blue",end=" ")
    cprint(f"{l[2]}","white")
    cprint(f"NOMBRE DE JOUEURS DANS LA BASE:","blue",end=" ")
    cprint(f"{nb[0]}","white")
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                       TOURNOIS ORGANISES                       │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(to)-1:
        cprint(f"{to[t]}"+" "*(30-len(to[t]))+f"=> {to[t+1]}","white")   
        t=t+2
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                        JOUEURS DU CLUB                         │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(jo)-1:
        cprint(f"{jo[t]} {jo[t+1]}","white")   
        t=t+2
    print("\n\n\n\n")

def club():
    cprint("Veuillez indiquer le sigle du club que vous souhaitez voir","white")
    j=""   
    while j.lower()=="":
        cprint(">>>","green",end="")
        j=input("")
        if j.lower()=="":
            cprint("Erreur entrée","red")
        if j.lower()!="":
            print_club(j.upper())

def print_tournoi(t):
    cmd=f"SELECT * FROM LesTournois WHERE nomTournoi='{t}'"
    infot=exec(cmd)
    cmd=f"SELECT * FROM LesGymnasesTournois JOIN LesGymnases USING(nomGymnase) WHERE idTournoi={infot[0]}"
    gym=exec(cmd)
    cmd=f"SELECT nom,prenom,sigleClub,paiement FROM LesInscriptions JOIN LesJoueurs USING(numLicence) WHERE idTournoi={infot[0]}"
    jo=exec(cmd)  
    cmd=f"SELECT COUNT(numLicence) FROM LesInscriptions WHERE idTournoi={infot[0]}"
    nb=exec(cmd)  
    clear()  
    cprint("┌──────────────────────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                      FICHE TOURNOI DE {t}","white",end="")
    cprint(" "*(43-len(list(t)))+"│","white")
    cprint("└──────────────────────────────────────────────────────────────────────────────────┘","white")
    cprint(f"ORGANSIE PAR:","blue",end=" ")
    cprint(f"{infot[3]}","white")
    cprint(f"DATE:","blue",end=" ")
    cprint(f"{infot[1]}","white")
    cprint(f"PRIX:","blue",end=" ")
    cprint(f"{infot[5]} €","white")
    cprint(f"NOMBRE DE JOUEURS:","blue",end=" ")
    cprint(f"{nb[0]}/{infot[4]}","white")
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                      GYMNASE(S) UTILISE(S)                     │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(gym)-1:
        cprint(f"{gym[t+1]} ({gym[t+3]} terrains et {gym[t+4]} tapis)","white")   
        t=t+5
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                        JOUEURS INSCRITS                        │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(jo)-1:
        cprint(f"{jo[t+1]} {jo[t]} (joueur du {jo[t+2]}, a déjà réglé {jo[t+3]} €)","white")   
        t=t+4
    cmd=f"SELECT DISTINCT * FROM LesMatchs JOIN LesTournois USING (idTournoi) WHERE idTournoi={infot[0]}"
    matchs=exec(cmd)
    cprint("┌────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                        MATCHS DISPUTES                         │","white")
    cprint("└────────────────────────────────────────────────────────────────┘","white")
    t=0
    while t<len(matchs)-1:
        cmd=f"SELECT nom,prenom FROM LesJoueurs WHERE numLicence={matchs[t+3]}"
        loser=exec(cmd)
        cmd=f"SELECT nom,prenom FROM LesJoueurs WHERE numLicence={matchs[t+2]}"
        winner=exec(cmd)
        cprint(f"Victoire de {winner[1]} {winner[0]} en {matchs[t+4]} sets face à {loser[1]} {loser[0]}","white")
        t=t+10    
    print("\n\n\n\n")

def tournoi():
    cmd="SELECT nomTournoi FROM LesTournois"
    l=exec(cmd)
    cprint("┌──────────────────────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                                LISTE DES TOURNOIS                                │","white")
    cprint("└──────────────────────────────────────────────────────────────────────────────────┘","white")
    i=1
    for t in l:
        cprint(f"|{i}| {t}","blue")
        i=i+1
    choix=0
    while int(choix)<1 or int(choix)>i+1:
        cprint("Quel tournoi souhaitez vous voir en détails ? [numéro du tournoi]","white")
        cprint(">>>","green",end="")
        choix=input("")
    tournoi=l[int(choix)-1]
    print_tournoi(tournoi)

def main(cur,con,stats): #stats[1]=compteur requetes
    accueil()
    r=0
    while r!=-1:
        r=ask()
        clear()
        if r=="j":
            get_joueur(cur,con) #terminé
            stats[1]+=8 #nombre de requetes utilisés dans la fonction get_joueur
        if r=="c": 
            club()   #terminé
            stats[1]+=4
        if r=="t":
            tournoi() #terminé
            stats[1]+=8
    sortie=False

