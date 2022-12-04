DROP TABLE IF EXISTS LesGymnasesTournois;
DROP TABLE IF EXISTS LesMatchs;
DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS LesTournois;
DROP TABLE IF EXISTS LesGymnases;
DROP TABLE IF EXISTS LesJoueurs;
DROP TABLE IF EXISTS LesClubs;





CREATE TABLE IF NOT EXISTS LesGymnases(
    nomGymnase VARCHAR(30),
    ville VARCHAR(30),
    nbTerrains NUMBER(2),
    nbTapis NUMBER(2),
    CONSTRAINT pk_nom PRIMARY KEY (nomGymnase)
);
INSERT INTO LesGymnases VALUES ("Halle Clémenceau","Grenoble",14,0);
INSERT INTO LesGymnases VALUES ("Complexe Sportif Ilot D'Europe","Bourg de Péage",14,5);
INSERT INTO LesGymnases VALUES ("HPP","Valence",18,5);
INSERT INTO LesGymnases VALUES ("Gymnase HP","Eybens",6,0);
INSERT INTO LesGymnases VALUES ("Gymnase Arcade","Voreppe",11,0);
INSERT INTO LesGymnases VALUES ("Gymnase Chorier","Grenoble",9,0);
INSERT INTO LesGymnases VALUES ("Gymnase Lycée Gabriel Faure","Tournon",5,0);
INSERT INTO LesGymnases VALUES ("Gymnase Jeannie Longo","Tournon",9,0);
INSERT INTO LesGymnases VALUES ("Gymnase Carrier","Saint Marcellin",6,0);
INSERT INTO LesGymnases VALUES ("Gymnase Chartreuse","Saint Martin d'Heres",12,0);
INSERT INTO LesGymnases VALUES ("Gymnase croix de verine","Echirolles",7,0);
INSERT INTO LesGymnases VALUES ("Gymnase La Marelle","Crolles",7,0);
INSERT INTO LesGymnases VALUES ("Gymnase La Saulaie","Saint Marcellin",6,0);

CREATE TABLE IF NOT EXISTS LesClubs (
	sigleClub VARCHAR(10),
	nomClub VARCHAR (30) NOT NULL,
	ville VARCHAR(20),
	CONSTRAINT pk_sigle PRIMARY KEY (sigleClub)
);
INSERT INTO LesClubs VALUES ("GAB38","Grenoble Alpes Badminton","Grenoble");
INSERT INTO LesClubs VALUES ("BCG38","Badminton Club Grenoble","Grenoble");
INSERT INTO LesClubs VALUES ("BCBP26","Badminton Club Bourg de Péage","Bourg de Péage");
INSERT INTO LesClubs VALUES ("BACO69","Badminton Club Oullins","Oullins");
INSERT INTO LesClubs VALUES ("BCF13","Badminton Club Fos sur Mer","Fos sur Mer");
INSERT INTO LesClubs VALUES ("BCV26","Badminton Club Valence","Valence");
INSERT INTO LesClubs VALUES ("AUCB13","Aix Université Club Badminton","Aix en Provence");
INSERT INTO LesClubs VALUES ("HP38","Hewlett Packard Badminton","Grenoble");
INSERT INTO LesClubs VALUES ("BCV38","Badminton Club Voreppe","Voreppe");
INSERT INTO LesClubs VALUES ("BCHT07","BC Hermitage et Touronnais","Tournon");
INSERT INTO LesClubs VALUES ("TGV07","Tamis Guillerandais Vivarais","Guillerand-Granges");
INSERT INTO LesClubs VALUES ("BCM38","Badminton Club Meylan","Meylan");
INSERT INTO LesClubs VALUES ("BCC73","Badminton Club Chambéry","Chambéry");
INSERT INTO LesClubs VALUES ("SBC38","Sassenage Badminton Club","Sassenage");
INSERT INTO LesClubs VALUES ("EB38","Echirolles Badminton","Echirolles");
INSERT INTO LesClubs VALUES ("ACB38","Association Crolloise","Crolles");
INSERT INTO LesClubs VALUES ("BCCI26","BC Chateauneuf sur Isère","Chateauneuf sur Isère");
INSERT INTO LesClubs VALUES ("BIM13","Bad In Marseille","Marseille");


CREATE TABLE IF NOT EXISTS LesJoueurs(
    numLicence NUMBER(8),
    nom VARCHAR(20) NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    age NUMBER(2) NOT NULL,
    sigleClub VARCHAR(10),
    CONSTRAINT  pk_licence PRIMARY KEY (numLicence),
    CONSTRAINT fk_club FOREIGN KEY (sigleClub) REFERENCES LesClubs(sigleClub),
    CONSTRAINT fk_age CHECK (age>0)
);
--GAB38
INSERT INTO LesJoueurs VALUES (07227979,"Barneaud","Esteban",19,"GAB38");
INSERT INTO LesJoueurs VALUES (00213045,"Leroux","Maxime",34,"GAB38");
INSERT INTO LesJoueurs VALUES (07007409,"Lacour","Timeo",14,"GAB38");
INSERT INTO LesJoueurs VALUES (06927961,"Werst","Marlene",35,"GAB38");
INSERT INTO LesJoueurs VALUES (07040459,"Duverne","Guillaume",21,"GAB38");
--BCG38
INSERT INTO LesJoueurs VALUES (07088205,"Swarts","Tristan",21,"BCG38");
INSERT INTO LesJoueurs VALUES (06766104,"Troussel","Erwan",23,"BCG38");
INSERT INTO LesJoueurs VALUES (00405777,"Chenal","Martin",28,"BCG38");
INSERT INTO LesJoueurs VALUES (06866537,"Ceccaldi","Adrien",33,"BCG38");
INSERT INTO LesJoueurs VALUES (07208376,"Cao","Michael",33,"BCG38");
INSERT INTO LesJoueurs VALUES (06791878,"Chan","Edmond",25,"BCG38");
--BCBP26
INSERT INTO LesJoueurs VALUES (06841924,"Bariol","Salome",18,"BCBP26");
INSERT INTO LesJoueurs VALUES (00469674,"Bariol","Raphael",44,"BCBP26");
INSERT INTO LesJoueurs VALUES (07006169,"Laurent","Tom",15,"BCBP26");
INSERT INTO LesJoueurs VALUES (07329904,"Bied","Lucien",20,"BCBP26");
--BACO69
INSERT INTO LesJoueurs VALUES (0664cmd=f"SELECT * FROM LesClubs WHERE sigleClub='{j}'"62710,"Lansac","Delphine",26,"BACO69");
INSERT INTO LesJoueurs VALUES (00536224,"Mattenet","Damien",28,"BACO69");
--BCF13
INSERT INTO LesJoueurs VALUES (06562597,"Popov","Christo",19,"BCF13");
INSERT INTO LesJoueurs VALUES (00486992,"Popov","Toma junior",23,"BCF13");
INSERT INTO LesJoueurs VALUES (06567081,"Speranza","Thierry",52,"BCF13");
INSERT INTO LesJoueurs VALUES (06584934,"Alary","Anaîs",27,"BCF13");
--BCV26
INSERT INTO LesJoueurs VALUES (07107045,"Laurent","Adrien",18,"BCV26");
INSERT INTO LesJoueurs VALUES (06611468,"Risson","Charlélie",20,"BCV26");
INSERT INTO LesJoueurs VALUES (06969581,"Lesage","Anais",16,"BCV26");
INSERT INTO LesJoueurs VALUES (07082987,"Michel","Florian",17,"BCV26");
--AUCB13
INSERT INTO LesJoueurs VALUES (00233556,"Labar","Ronan",32,"AUCB13");
INSERT INTO LesJoueurs VALUES (06698043,"Barbieri","Yohan",17,"AUCB13");
INSERT INTO LesJoueurs VALUES (00200838,"Françoise","Alexandre",31,"AUCB13");
INSERT INTO LesJoueurs VALUES (07327744,"Magee","Chloe",33,"AUCB13");
--HP38
INSERT INTO LesJoueurs VALUES (07084732,"Popova","Olga",37,"HP38");
--BCHT07
INSERT INTO LesJoueurs VALUES (06828769,"Duhoo","Enzo",24,"BCHT07");
--SBC38
INSERT INTO LesJoueurs VALUES (00554748,"Martinez","Mathieu",51,"SBC38");
--BCC73
INSERT INTO LesJoueurs VALUES (06763558,"Bouzon","Arnaud",19,"BCC73");
--BCM38
INSERT INTO LesJoueurs VALUES (07207496,"Valloire","Hugo",25,"BCM38");
INSERT INTO LesJoueurs VALUES (06898868,"Fremont","Tom",15,"BCM38");
--EB38
INSERT INTO LesJoueurs VALUES (06950955,"Gachet","Fabien",48,"EB38");
--BIM13
INSERT INTO LesJoueurs VALUES (00493716,"Aubert","Alexis",31,"BIM13");


CREATE TABLE IF NOT EXISTS LesTournois (
    idTournoi NUMBER(4),
    date DATE NOT NULL,
    nomTournoi VARCHAR(30) NOT NULL,
    sigleClub VARCHAR(10) NOT NULL,
    nbPlaces NUMBER(3) NOT NULL,
    prix NUMBER(2) NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY (idTournoi),
    CONSTRAINT fk_club FOREIGN KEY (sigleClub) REFERENCES LesClubs(sigleClub),
    CONSTRAINT ck_prix CHECK (prix>=0),
    CONSTRAINT ck_places CHECK (nbPlaces>=0)
);
INSERT INTO LesTournois VALUES (1,'26-03-2022 08:00:00',"Tournoi International du BCBP","BCBP26",300,19);
INSERT INTO LesTournois VALUES (2,'04-06-2022 08:00:00',"Trophée des Alpes","GAB38",500,22);
INSERT INTO LesTournois VALUES (3,'14-05-2022 08:00:00',"Tournoi International Valence","BCV26",380,18);
INSERT INTO LesTournois VALUES (4,'09-04-2022 08:00:00',"Tournoi Hewlett Packard","HP38",60,15);
INSERT INTO LesTournois VALUES (5,'11-06-2022 08:00:00',"TRV 2022","BCV38",400,20);
INSERT INTO LesTournois VALUES (6,'18-12-2022 08:00:00',"Tournoi de Noel du BCHT","BCHT07",200,15);
INSERT INTO LesTournois VALUEs (7,'01-11-2021 08:00:00',"8eme Plume Crolloise","ACB38",150,20);

CREATE TABLE LesInscriptions (
    idTournoi NUMBER(4),
    numLicence NUMBER(8),
    paiement NUMBER(2),
    CONSTRAINT pk_idlicence PRIMARY KEY(idTournoi,numLicence),
    CONSTRAINT fk_id FOREIGN KEY (idTournoi) REFERENCES LesTournois(idTournoi),
    CONSTRAINT fk_numlicence FOREIGN KEY (numLicence) REFERENCES LesJoueurs(numLicence),
    CONSTRAINT ck_paiement CHECK (paiement>=0)
);
--TOURNOI BCBP--
INSERT INTO LesInscriptions VALUES (1,07227979,19);
INSERT INTO LesInscriptions VALUES (1,00469674,0);
INSERT INTO LesInscriptions VALUES (1,07329904,19);
INSERT INTO LesInscriptions VALUES (1,06828769,19);
INSERT INTO LesInscriptions VALUES (1,07082987,19);
INSERT INTO LesInscriptions VALUES (1,06763558,19);
INSERT INTO LesInscriptions VALUES (1,06791878,19);
INSERT INTO LesInscriptions VALUES (1,00493716,19);
INSERT INTO LesInscriptions VALUES (1,07040459,19);
--TOURNOI TROPHEE DES ALPES--
INSERT INTO LesInscriptions VALUES (2,07227979,22);
INSERT INTO LesInscriptions VALUES (2,00405777,22);
INSERT INTO LesInscriptions VALUES (2,06766104,22);
INSERT INTO LesInscriptions VALUES (2,07088205,22);
--TOURNOI INTERNATIONAL VALENTINOIS--
INSERT INTO LesInscriptions VALUES (3,07227979,18);
INSERT INTO LesInscriptions VALUES (3,06611468,18);
INSERT INTO LesInscriptions VALUES (3,07082987,0);
INSERT INTO LesInscriptions VALUES (3,06969581,0);
INSERT INTO LesInscriptions VALUES (3,07107045,0);
--TOURNOI HP--
INSERT INTO LesInscriptions VALUES (4,07088205,15);
INSERT INTO LesInscriptions VALUES (4,06766104,15);
INSERT INTO LesInscriptions VALUES (4,00405777,15);
INSERT INTO LesInscriptions VALUES (4,07227979,15);
INSERT INTO LesInscriptions VALUES (4,06866537,15);
INSERT INTO LesInscriptions VALUES (4,00554748,15);
INSERT INTO LesInscriptions VALUES (4,07040459,15);
INSERT INTO LesInscriptions VALUES (4,07208376,15);
--TOURNOI BCV--
INSERT INTO LesInscriptions VALUES (5,07227979,20);
INSERT INTO LesInscriptions VALUES (5,07088205,20);
--TOURNOI BCHT--
INSERT INTO LesInscriptions VALUES (6,07227979,15);
INSERT INTO LesInscriptions VALUES (6,00405777,15);
INSERT INTO LesInscriptions VALUES (6,06611468,15);
INSERT INTO LesInscriptions VALUES (6,06763558,15);
INSERT INTO LesInscriptions VALUES (6,07006169,15);
--TOURNOI CROLLES--
INSERT INTO LesInscriptions VALUES (7,06950955,20);
INSERT INTO LesInscriptions VALUES (7,07227979,20);
INSERT INTO LesInscriptions VALUES (7,06766104,20);
INSERT INTO LesInscriptions VALUES (7,07207496,20);
INSERT INTO LesInscriptions VALUES (7,06866537,20);
INSERT INTO LesInscriptions VALUES (7,06898868,20);





CREATE TABLE IF NOT EXISTS LesGymnasesTournois (
    idTournoi NUMBER(4),
    nomGymnase NUMBER(8),
    CONSTRAINT pk_id_gymnase PRIMARY KEY (idTournoi,nomGymnase),
    CONSTRAINT fk_id FOREIGN KEY (idTournoi) REFERENCES LesTournois(idTournoi),
    CONSTRAINT fk_nomgymnase FOREIGN KEY (nomGymnase) REFERENCES LesGymnases(nomGymnase)
);

INSERT INTO LesGymnasesTournois VALUES (1,"Complexe Sportif Ilot D'Europe");
INSERT INTO LesGymnasesTournois VALUES (2,"Halle Clémenceau");
INSERT INTO LesGymnasesTournois VALUES (3,"HPP");
INSERT INTO LesGymnasesTournois VALUES (4,"Gymnase HP");
INSERT INTO LesGymnasesTournois VALUES (5,"Gymnase Arcade");
INSERT INTO LesGymnasesTournois VALUES (6,"Gymnase Jeannie Longo");
INSERT INTO LesGymnasesTournois VALUES (6,"Gymnase Lycée Gabriel Faure");
INSERT INTO LesGymnasesTournois VALUES (7,"Gymnase La Marelle");

CREATE TABLE LesMatchs (
    idTournoi NUMBER(4) NOT NULL,
    numMatch NUMBER(3),
    licenceVainqueur NUMBER(8) NOT NULL,
    licencePerdant NUMBER(8) NOT NULL,
    nbSets NUMBER(1) NOT NULL,
    CONSTRAINT pk_date_num PRIMARY KEY (idTournoi,numMatch),
    CONSTRAINT fk_id FOREIGN KEY (idTournoi) REFERENCES LesTournois(idTournoi),
    CONSTRAINT fk_numlicence FOREIGN KEY (licenceVainqueur) REFERENCES LesJoueurs(numLicence),
    CONSTRAINT fk_numlicence FOREIGN KEY (licencePerdant) REFERENCES LesJoueurs(numLicence),
    CONSTRAINT ck_sets CHECK (nbSets>0 AND nbSets<=3),
    CONSTRAINT ck_num_match CHECK (numMatch>0)
);

INSERT INTO LesMatchs VALUES (6,1,00405777,07227979,2);
INSERT INTO LesMatchs VALUES (1,100,06828769,07082987,2);
INSERT INTO LesMatchs VALUES (4,142,00554748,07088205,3);
INSERT INTO LesMatchs VALUES (4,137,00554748,07040459,2);
INSERT INTO LesMatchs VALUES (1,42,06763558,07040459,2);
INSERT INTO LesMatchs VALUES (6,65,06611468,06763558,3);
INSERT INTO LesMatchs VALUES (6,51,07006169,00405777,3);
INSERT INTO LesMatchs VALUES (7,4,06766104,06950955,3);
INSERT INTO LesMatchs VALUES (7,6,06766104,07227979,2);
INSERT INTO LesMatchs VALUES (7,8,06950955,07207496,2);
INSERT INTO LesMatchs VALUES (7,14,07207496,06866537,2);
INSERT INTO LesMatchs VALUES (4,37,07208376,07227979,3);
INSERT INTO LesMatchs VALUES (1,101,06791878,07227979,3);
INSERT INTO LesMatchs VALUES (1,14,00493716,07227979,2);

