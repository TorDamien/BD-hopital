import sqlite3
from termcolor import *
import colorama
import os
colorama.init()
import tableau #Fonction de récup tables
import time
from datetime import datetime
import sys
import webbrowser
import random
import interface_haut_niveau
c=0
stats=[time.time(),0]#heure d'entrée,requetes éxécutées
connected=False
cmdlist=["exit()","save()","?tables","?attributs"]

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def proc_sortie():
    t2=time.time()-stats[0]
    cprint("Avant que vous ne partiez, voici quelques données sur votre utilisation:","white")
    cprint("┌────────────────────────────────────────────┐ ┌────────────────────────────────────────────┐ ┌────────────────────────────────────────────┐","blue")
    cprint(f"│    Secondes sur le programme: {round(t2)} secondes","blue",end="")
    print(" "*(4-len(str(round(t2)))),end="")
    cprint(f"├─┤          {stats[1]} requete(s) éxécutée(s)","blue",end="")
    print(" "*(4-len(str(stats[1]))),end="")
    cprint("       ├─┤              Projet INF403                 │","blue")
    cprint("└────────────────────────────────────────────┘ └────────────────────────────────────────────┘ └────────────────────────────────────────────┘","blue")
    sys.exit(0)

def proc_projet():
    global choix
    global cur
    global connected
    global projet_file
    global con
    global stats
    choix="Reqs"
    f="projetfinal.db"
    projet_file=True
    cprint("Commandes disponibles dans l'interface bas niveau:\n-?attributs [nomTable] pour obtenir les attributs de la table renseignée\n-?tables pour obtenir les noms de table du projet","green")
    con = sqlite3.connect(f)
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    connected=True
    cprint("┌────────────────────────────────────────────┐\n│     Connecté au fichier 'projetfinal.db'   │\n└────────────────────────────────────────────┘","green" )
    cprint("~~Un peu de contexte~~\nVous avez été connecté à la base de données 'projetfinal.db'.\nDans cette base de données, on trouve d'ores et déjà toutes les tables de mon projet","white")
    cprint("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐","white")
    cprint(f"│                      Souhaitez vous utiliser une interface haut niveau ? (Aucune connaissance sql demandée) [y/n]                     │","white")
    cprint("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘","white")
    cprint("(Recommandé [y])>>>","green",end="")
    rep=input("")
    sortie=False
    if rep.lower()=="y":
        cprint("Appuyez sur un touche pour rentrer dans l'interface haut niveau. En sortie, vous serez dans l'interface bas niveau.","white")
        a=input()
        clear()
        sortie=interface_haut_niveau.main(cur,con,stats)
    if sortie==False:
        cprint("Souhaitez vous pouvoir éxécuter quelques commandes tests pré-rentrées sur la base de données ? Si non, vous allez pouvoir rentrer vos propres commandes. [y/n] ","white")
        cprint(">>>","green",end="")
        tests=input("")
        if tests.lower()=='n':
            return
        while JeVeuxTesterDesCommandes()!=1:
            continue

def verif_insert_match(cmd):
    global con
    global projet_file
    if projet_file==False:
        return True
    if "INSERT" not in cmd:
        return True
    lcmd=cmd.split(" ")
    if lcmd[2]!="LesMatchs":
        return True
    values=lcmd[4].split(",")
    idT=list(values[0])[1]
    numlicence1=values[2]
    numlicence2=values[3]
    res=con.execute(f"SELECT * FROM LesInscriptions WHERE numLicence={numlicence1} AND idTournoi={idT}")
    c=0
    for row in res:
        c=c+1
    if c!=0:
        res=con.execute(f"SELECT * FROM LesInscriptions WHERE numLicence={numlicence2} AND idTournoi={idT}")
        c=0
        for row in res:
            c=c+1
        if c!=0:
            return True
    cprint("┌─────────────────────────────────────────────────────────────────────┐\n│         Un des joueurs renseignés n'est pas inscrit au tournoi      │\n└─────────────────────────────────────────────────────────────────────┘","red" )
    return False
        
def JeVeuxTesterDesCommandes():
    cprint("─────────────────────────────────────────────────────────────────────────────────────────────","white")
    cprint("[1] Tous les Joueurs      [4] Tous les noms et prénoms de joueurs","white")
    cprint("[2] Tous les Clubs        [5] Tous les tournois qui possèdent plus de 100 places","white")
    cprint("[3] Tous les Tournois     [6] Tous les joueurs qui ont plus de 18 ans","white")
    cprint("( Tapez 'ok' si vous voulez sortir des tests)","red")
    cprint("─────────────────────────────────────────────────────────────────────────────────────────────","white")
    cprint(">>>","green",end="")
    num=input("")
    if num.lower()=="ok":
        return 1
    if num=='1': exec_test("SELECT * FROM LesJoueurs")
    if num=='2': exec_test("SELECT * FROM LesClubs")
    if num=='3': exec_test("SELECT * FROM LesTournois")
    if num=='4': exec_test("SELECT nom,prenom FROM LesJoueurs")
    if num=='5': exec_test("SELECT * FROM LesTournois WHERE nbPlaces>=100")
    if num=='6': exec_test("SELECT * FROM LesJoueurs WHERE age>=18")

def JeVeuxUnTuto():
    cprint("─────────────────────────────────────────────────────────────────────────────────────────────","white")
    cprint("[1] Menu Principal              [4] Comment sauvegarder/back up des modifications ?","white")
    cprint("[2] Sous Menu 'Projet'          [5] Comment faire des requetes fichier/clavier ?","white")
    cprint("[3] Création/Interaction DB     [6] Tout voir","white")
    cprint("( Tapez 'ok' si vous voulez sortir du tutoriel)","red")
    cprint("─────────────────────────────────────────────────────────────────────────────────────────────","white")
    cprint(">>>","green",end="")
    num=input("")
    if num.lower()=="ok":
        return 1
    if num=='1':
        #CAS MENU PRINCIPAL
        clear()
        cprint("Voici donc le menu sur lequel vous étiez il y a quelques secondes:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        clear()
        cprint("Vous aviez donc entré 't' ou 'tuto' pour accéder à ce tutoriel\nDans la même logique, il vous suffira:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue",end="")
        cprint("<= D'entrer 'c' pour vous connecter à un fichier db","green")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue",end="")
        cprint("<= D'entrer 'p' pour découvrir le projet de l'UE INF403","green")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear() 
    if num=='2':
        clear()
        cprint("~~Le sous menu Projet~~\nLe sous menu projet vous amène directement à la partie projet et sa base de données.\nIl vous sera proposé d'accéder à l'interface de haut niveau (aucune connaissance SQL requise pour l'utiliser). Cette interface permet d'obtenir des informations sur les tables à travers des menus simples","white")
        cprint("Ensuite, vous arrivez dans l'interface bas niveau où des connaissances sql sont requises.Il vous demandera si vous souhaitez exécuter des commandes préfaites et vous aurez ensuite la possibilité de réaliser des commandes sur la base de données\nVous n'aurez donc pas besoin de rentrer le nom du fichier de la base de données en procédant comme cela.","white")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
        #CAS SOUS MENU "PROJET"
    if num=='3':
        #CAS CREATION/INTERACTION
        clear()
        cprint("~~Le sous menu Creation de table/Interaction avec les tables~~\nPour utiliser cela, il nous faut rentrer dans le menu de connexion à un fichier:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue",end="")
        cprint("<= 'c' juste ici","green")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        cprint("Il vous sera ensuite demandé de vous connecter à une table.\nSi vous avez une base de données, il vous suffit de rensienger le nom du fichier.\nDans le cas contraire, vous pouvez créer une base de données vierge dont vous précisez le nom.","white")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        cprint("Vous pourrez ensuite effectuer des commandes comme dans n'importe quelle base (SELECT, UPDATE, DELETE) etc.\nVous pourrez donc agir sur votre table ainsi","white")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
    if num=='4':
        #CAS SAUVEGARDE/BACK UP
        clear()
        cprint("~~Sauvegardes et Back up~~\nAprès avoir effectué des commandes, vous aurez soit envie de sauvegarder, soit de faire un back up. Pour cela on dispose de 2 commandes:","white")
        cprint("-save(): commande vous permettant de sauvegarder les modifications. Il vous sera de possible de sauvegarder les modifications au moment de la sortie de fichier","white")
        cprint("-exit(): commande permettant de sortir du fichier. Il vous est ensuite demandé si vous souhaitez faire une sauvegarde des modifications ou non. Si non, un back up sera effectué avec les données avant modifications.","white")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
    if num=='5':
        #REQUETES
        clear()
        webbrowser.open_new_tab("https://moodle.caseine.org/pluginfile.php/141740/mod_resource/content/0/L2_BD_INF403_2021-22_CH3_SQL-DML%28Avec%20Aggregation%29.pdf")
        cprint("Pour éxécuter un fichier, il vous suffit d'indiquer le nom du fichier .sql et il s'écécutera.\nAppuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
    if num=='6':
        #TOUT AFFICHER
        #1
        clear()
        cprint("Voici donc le menu sur lequel vous étiez il y a quelques secondes:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        clear()
        cprint("Vous aviez donc entré 't' ou 'tuto' pour accéder à ce tutoriel\nDans la même logique, il vous suffira:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue",end="")
        cprint("<= D'entrer 'c' pour vous connecter à un fichier db","green")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue",end="")
        cprint("<= D'entrer 'p' pour découvrir le projet de l'UE INF403","green")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour continuer ce tutoriel...","white")
        a=input()
        #2
        clear()
        cprint("~~Le sous menu Projet~~\nLe sous menu projet vous amène directement à la partie projet et sa base de données.\nIl vous demandera si vous souhaitez exécuter des commandes préfaites et vous aurez ensuite la possibilité de réaliser des commandes sur la base de données\nVous n'aurez donc pas besoin de rentrer le nom du fichier en procédant comme cela.","white")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
        clear()
        cprint("~~Le sous menu Creation de table/Interaction avec les tables~~\nPour utiliser cela, il nous faut rentrer dans le menu de connexion à un fichier:","white")
        cprint("┌──────────┐ ┌────────────────────────────────┐","blue")
        cprint("│ Tuto [t] ├─┤   Connexion à un fichier db[c] │","blue",end="")
        cprint("<= 'c' juste ici","green")
        cprint("└──────────┘ └────────────────────────────────┘","blue")
        cprint("          ╲     /","blue")
        cprint("       ┌────────────────────┐","blue")
        cprint("       │ Projet INF403 [p]  │","blue")
        cprint("       └────────────────────┘","blue")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        cprint("Il vous sera ensuite demandé de vous connecter à une table.\nSi vous avez une base de données, il vous suffit de rensienger le nom du fichier.\nDans le cas contraire, vous pouvez créer une base de données vierge dont vous précisez le nom.","white")
        cprint("Appuyez sur n'importe quelle touche pour passer à l'écran suivant...","white")
        a=input("")
        cprint("Vous pourrez ensuite effectuer des commandes comme dans n'importe quelle base (SELECT, UPDATE, DELETE) etc.\nVous pourrez donc agir sur votre table ainsi","white")
        cprint("Appuyez sur n'importe quelle touche pour continuer ce tutoriel...","white")
        a=input()
        clear()
        cprint("~~Sauvegardes et Back up~~\nAprès avoir effectué des commandes, vous aurez soit envie de sauvegarder, soit de faire un back up. Pour cela on dispose de 2 commandes:","white")
        cprint("-save(): commande vous permettant de sauvegarder les modifications. Il vous sera de possible de sauvegarder les modifications au moment de la sortie de fichier","white")
        cprint("-exit(): commande permettant de sortir du fichier. Il vous est ensuite demandé si vous souhaitez faire une sauvegarde des modifications ou non. Si non, un back up sera effectué avec les données avant modifications.","white")
        cprint("Appuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()
        webbrowser.open_new_tab("https://moodle.caseine.org/pluginfile.php/141740/mod_resource/content/0/L2_BD_INF403_2021-22_CH3_SQL-DML%28Avec%20Aggregation%29.pdf")
        cprint("Pour éxécuter un fichier, il vous suffit d'indiquer le nom du fichier .sql et il s'écécutera.\nAppuyez sur n'importe quelle touche pour terminer ce tutoriel...","white")
        a=input()
        clear()

def exec_test(cmd):
    global c
    t1=time.time()
    res=cur.execute(cmd)
    col2=tableau.get_col(cmd)
    tableau.tableau(col2)
    c=0
    for row in res:
        if c!=0:
            cprint("\n│","red",end="")
            cprint("                              │"*(len(col2)-1),"red",end="")
            cprint("                              │","red")
        cprint("│","red",end="")
        for col in row:
            cprint(f"{col}","white",end=" "*(30-len(str(col))))
            cprint("│","red",end="")
        c=c+1
    cprint("\n└──────────────────────────────","red",end="")
    for i in range(0,len(col2)-1):
        cprint("┴──────────────────────────────","red",end="")
    cprint("┘","red")
    t2=time.time()
    t=round(t2-t1,4)
    cprint(f"Terminé en {t} secondes ~~ {c} lignes sélectionnées","yellow")


def proc_tuto():
    global choix
    choix="z"
    while JeVeuxUnTuto()!=1:
        continue
    
def loading_bar():
    clear()
    if random.randint(0,100)%2==0:
        cprint("Optimisation pour votre pc en cours...","white")
        for i in range(101):
            cprint("["+"#"*i+"."*(100-i)+"]","green",end="\r",) #Il ne s'est pas passé grand chose réellement
            t=random.randint(5,10)/100
            time.sleep(t)

def accueil():
    cprint("┌────────────────────────────────────────────┐ ┌────────────────────────────────────────────┐","blue")
    cprint("│                 Tuto [t]                   ├─┤        Connexion à un fichier db[c]        │","blue")
    cprint("└────────────────────────────────────────────┘ └────────────────────────────────────────────┘","blue")
    cprint("                                    ╲                   ╱","blue")
    cprint("                        ┌────────────────────────────────────────────┐","blue")
    cprint("                        │              Projet INF403 [p]             │","blue")
    cprint("                        └────────────────────────────────────────────┘","blue")

def first_screen():
    loading_bar()
    clear()
    cprint(" ┌────────────────────────────────────────────┐","blue")
    cprint("┌","white",end="")
    cprint("┤                 Projet SGBD                ├","blue",end="")
    cprint("┐\n│","white",end="")
    cprint("└────────────────────────────────────────────┘","blue",end="")
    cprint("│\n│","white",end="")
    cprint("┌────────────────────────────────────────────┐","blue",end="")
    cprint("│\n└","white",end="")
    cprint("┤               Esteban INM 3                ├","blue",end="")
    cprint("┘","white")
    cprint(" └────────────────────────────────────────────┘","blue")
    global choix
    choix="z"

def main():
    first_screen()
    cprint(f"Session du: {datetime.now().strftime('%A %d %B %Y à %H:%M:%S')}","white")
    global choix
    global cur
    global con
    while True:
        ########################################################################################################################################################
        ###INTERFACE DE CHOIX DE MENUS: Choisir dans quel menu se rediriger ou pour sortir du programme
        ########################################################################################################################################################  
        while choix.lower() not in ["t","c","p","reqs"]:
            accueil()
            cprint("(Pour quitter, entrez 'q')","red")
            cprint(">>>","green",end="")
            choix=input()
            if choix.lower()=='q':
                proc_sortie()
            if choix.lower()=='t' or choix.lower()=="tuto":
                proc_tuto()
            if choix.lower()=='p':
                proc_projet()
                cprint("Vous pouvez désormais éxécuter vos propres commandes dans la console ou via des fichiers","white")
                cprint("(Pour quitter, entrez 'exit()')","red")

        if choix=="c":
            ########################################################################################################################################################
            ###INTERFACE DE CONNEXION : permet d'ouvrir ou créer une base de donnée et d'ouvrir un terminal relié à cette base de donnée
            ########################################################################################################################################################
            cprint("┌────────────────────────────────────────────┐\n│   Bienvenue sur l'interface de connexion   │\n└────────────────────────────────────────────┘","blue" )
            connected=False
            while not connected:
                cprint("└└>>Veuillez saisir le nom de la base de donnée à ouvrir: ","blue",end="" )
                f=input("")
                if f=="projetfinal.db":
                    projet_file=True
                    cprint("Commandes disponibles:\n-?attributs [nomTable] pour obtenir les attributs de la table renseignée\n-?tables pour obtenir les noms de table du projet","green")
                if f in os.listdir():
                    con = sqlite3.connect(f)
                    con.execute("PRAGMA foreign_keys = 1")
                    cur = con.cursor()
                    connected=True
                else:
                    cprint("┌────────────────────────────────────────────┐\n│         La base indiquée n'existe pas      │\n└────────────────────────────────────────────┘","red" )
                    cprint(f"└└>>Voulez vous créer une base de donnée portant ce nom '{f}' : (y/n) ","blue",end="" )
                    g=input("")
                    if g.lower()=="y":
                        cprint("┌────────────────────────────────────────────┐\n│                  Base créée                │\n└────────────────────────────────────────────┘","green" )
                        con = sqlite3.connect(f)
                        con.execute("PRAGMA foreign_keys = 1")
                        cur = con.cursor()
                        connected=True
            cprint("┌────────────────────────────────────────────┐\n│             Connecté au fichier            │\n└────────────────────────────────────────────┘","green" )
            choix="Reqs"

        if choix=="Reqs":
            True
            ########################################################################################################################################################
            ###BOUCLE : Une fois le terminal ouvert, toutes les commandes seront entrées dans cette boucle
            ########################################################################################################################################################
            while True:
                ###ENTREE CLAVIER
                cprint(">>>","green",end="")
                cmd=input("")
                t1=time.time()
                
                #Vérification que l'entrée clavier n'est pas une commande
                t=False
                if cmd in cmdlist or "?attributs" in cmd.lower():              
                    t=True
                    ###COMMANDE EXIT
                    if cmd.lower()=="exit()":
                        cprint("└└>>Voulez vous sauvegarder les modifications ? (y/n) ","blue",end="" )
                        f=input("")
                        if f.lower()=="y":
                            con.commit()
                            con.close()
                            cprint("┌────────────────────────────────────────────┐\n│            Sauvegarde effectuée            │\n└────────────────────────────────────────────┘","green" )
                            cprint("┌────────────────────────────────────────────┐\n│      Deconnecté de la base de données      │\n└────────────────────────────────────────────┘","green" )
                            choix="deco"
                            break
                        if f.lower()=="n":   
                            choix="deco"
                            cprint("┌────────────────────────────────────────────┐\n│      Deconnecté de la base de données      │\n└────────────────────────────────────────────┘","green" )
                            break
                    ###COMMANDE SAVE
                    if cmd.lower()=="save()":
                        cprint("└└>>Voulez vous sauvegarder les modifications ? (y/n) ","blue",end="" )
                        f=input("")
                        if f.lower()=="y":
                            con.commit()
                            cprint("┌────────────────────────────────────────────┐\n│            Sauvegarde effectuée            │\n└────────────────────────────────────────────┘","green" )
                    ###COMMANDE TABLES
                    if cmd.lower()=="?tables" and projet_file==True:
                        cprint("Les différentes tables sont:","white")
                        l=["LesGymnasesTournois","LesMatchs","LesInscriptions","LesTournois","LesGymnases","LesJoueurs","LesClubs"]
                        for table in l:
                            cprint(f"-{table}","white")
                    ###COMMANDE ATTRIBUTS
                    if "?attributs" in cmd.lower() and projet_file==True:
                        try:
                            table=cmd.split(" ")[1]
                            t=tableau.get_atrbs(table)
                            if t!=[]:
                                cprint(f"Les différentes attributs de la table {table} sont:","white")
                                for table in t:
                                    cprint(f"-{table}","white")
                        except:
                            cprint(f"Il est nécessaire de préciser une table existante du projet. Veuillez vérifier à bien indiquer une table du projet.","white")


                ###COMMANDE SQL FICHIER
                if cmd in os.listdir() and t==False:
                    file = open(cmd)
                    cmds = file.read()
                    cmds=cmds.split(";")
                    for cmd in cmds:
                        if cmd!="" or cmd==" ":
                            if cmd!=""  and "select" not in cmd.lower():
                                cprint(f"COMMANDE FICHIER:","white",end=" ")
                                cprint(f"{cmd}","cyan")   
                                cmd.replace("\n"," ")
                                try:
                                    valeur_temoin=1
                                    if verif_insert_match(cmd)==False:
                                        valeur_temoin=0
                                    if valeur_temoin==1:
                                        for row in cur.execute(cmd):
                                            print(row)
                                            print(f"{len(cmds)} lignes sélectionnées")
                                except:
                                    cprint("┌────────────────────────────────────────────┐\n│        Erreur dans la requête envoyée      │\n└────────────────────────────────────────────┘","red" )
                            if "select" in cmd.lower():
                                try:
                                    if verif_insert_match(cmd)==False:
                                        break
                                    res=cur.execute(cmd)
                                    col2=tableau.get_col(cmd)
                                    tableau.tableau(col2)
                                    for row in res:
                                        if c!=0:
                                            cprint("\n│","red",end="")
                                            cprint("                              │"*(len(col2)-1),"red",end="")
                                            cprint("                              │","red")
                                        cprint("│","red",end="")
                                        for col in row:
                                            cprint(f"{col}","white",end=" "*(30-len(str(col))))
                                            cprint("│","red",end="")
                                        c=c+1
                                    cprint("\n└──────────────────────────────","red",end="")
                                    for i in range(0,len(col2)-1):
                                        cprint("┴──────────────────────────────","red",end="")
                                    cprint("┘","red")
                                    t2=time.time()
                                    t=round(t2-t1,4)
                                    cprint(f"Terminé en {t} secondes ~~ {c} lignes sélectionnées","yellow")
                                except sqlite3.Error as e:
                                    cprint("┌────────────────────────────────────────────┐\n│        Erreur dans la requête envoyée      │\n└────────────────────────────────────────────┘","red" )
                                    cprint(f"┌────────────────────────────────────────────\n│Erreur spécifiée: {e}      \n└────────────────────────────────────────────","red")
                                stats[1]=stats[1]+1
                ###COMMANDE SQL AU CLAVIER
                elif t==False:
                    try:
                        if verif_insert_match(cmd)==False:
                            break
                        res=cur.execute(cmd)
                        if "select" in cmd.lower():
                            col2=tableau.get_col(cmd)
                            tableau.tableau(col2)
                            c=0
                            for row in res:
                                if c!=0:
                                    cprint("\n│","red",end="")
                                    cprint("                              │"*(len(col2)-1),"red",end="")
                                    cprint("                              │","red")
                                cprint("│","red",end="")
                                for col in row:
                                    cprint(f"{col}","white",end=" "*(30-len(str(col))))
                                    cprint("│","red",end="")
                                c=c+1
                            cprint("\n└──────────────────────────────","red",end="")
                            for i in range(0,len(col2)-1):
                                cprint("┴──────────────────────────────","red",end="")
                            cprint("┘","red")
                        t2=time.time()
                        t=round(t2-t1,4)
                        cprint(f"Terminé en {t} secondes ~~ {c} lignes sélectionnées","yellow")
                        stats[1]=stats[1]+1
                    except sqlite3.Error as e:
                        cprint("┌────────────────────────────────────────────┐\n│        Erreur dans la requête envoyée      │\n└────────────────────────────────────────────┘","red" )
                        cprint(f"┌────────────────────────────────────────────\n│Erreur spécifiée: {e}      \n└────────────────────────────────────────────","red")



main()





