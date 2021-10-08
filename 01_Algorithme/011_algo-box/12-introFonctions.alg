<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="APPELER_FONCTION calculCarre()" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2para="" F2lignes="" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions">
        <item algoitem="FONCTION calculCarre( )" code="201#calculCarre# ">
            <item algoitem="VARIABLES_FONCTION" code="202#declarationsvariablesfonction">
                <item algoitem="nb EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb"/>
            </item>
            <item algoitem="DEBUT_FONCTION" code="203#debutfonction"/>
            <item algoitem="AFFICHER &quot;entrez un nombre&quot;" code="4#entrez un nombre#0"/>
            <item algoitem="LIRE nb" code="2#nb#pasliste"/>
            <item algoitem="AFFICHERCALCUL nb*nb" code="20#nb*nb#0"/>
            <item algoitem="FIN_FONCTION" code="204#finfonction"/>
        </item>
    </item>
    <item algoitem="VARIABLES" code="100#declarationsvariables"/>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="//Appel de la fonction calculCarre" code="19#Appel de la fonction calculCarre"/>
        <item algoitem="APPELER_FONCTION calculCarre()" code="206#calculCarre()"/>
        <item algoitem="APPELER_FONCTION calculCarre()" code="206#calculCarre()"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
