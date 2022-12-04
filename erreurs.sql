--Club inexistant;
INSERT INTO LesJoueurs VALUES (08789852,"Dupont","Guillaume",45,"RDT74");
-- Joueur non inscrit au tournoi;
INSERT INTO LesMatchs VALUES (5,47,07208376,07227979,2);
--Tournoi invalide;
INSERT INTO LesMatchs VALUES (85,47,07208376,07227979,2);
--Joueur age inférieur à 0;
INSERT INTO LesJoueurs VALUES (08789852,"Dupont","Guillaume",-1,"GAB38");
--ID Tournoi déjà utilisé;
INSERT INTO LesTournois VALUES (1,'26-05-2022 08:00:00',"Tournoi Test","BCBP26",300,19);
--Inscription d'un joueur inconnu;
INSERT INTO LesInscriptions VALUES (1,08888889,19);
--Inscription à un tournoi inconnu;
INSERT INTO LesInscriptions VALUES (41,07227979,19);
--Lien entre un gymnase inconnu et un tournoi;
INSERT INTO LesGymnasesTournois VALUES (2,"Gymnase du centre");
--Lien entre un gymnase et un tournoi inconnu;
INSERT INTO LesGymnasesTournois VALUES (41,"Gymnase Lycée Gabriel Faure");
--Match en 4 sets => impossible;
INSERT INTO LesMatchs VALUES (6,1,00405777,07227979,4);
--Match en -1 sets => impossible;
INSERT INTO LesMatchs VALUES (6,1,00405777,07227979,-1);
--Numéro de match <0;
INSERT INTO LesMatchs VALUES (6,-42,00405777,07227979,2);





