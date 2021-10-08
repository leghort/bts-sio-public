<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="tabCarres[i] PREND_LA_VALEUR tabCarres[i]*tabCarres[i]" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2para="" F2lignes="" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="tabCarres EST_DU_TYPE LISTE" code="1#LISTE#tabCarres"/>
        <item algoitem="i EST_DU_TYPE NOMBRE" code="1#NOMBRE#i"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="POUR i ALLANT_DE 0 A 4" code="12#i#0#4">
            <item algoitem="DEBUT_POUR" code="13#debutpour"/>
            <item algoitem="//Saisir un nombre" code="19#Saisir un nombre"/>
            <item algoitem="AFFICHER &quot;Saisir un ebtier &quot;" code="4#Saisir un ebtier #0"/>
            <item algoitem="LIRE tabCarres[i]" code="2#tabCarres#i"/>
            <item algoitem="tabCarres[i] PREND_LA_VALEUR tabCarres[i]*tabCarres[i]" code="5#tabCarres#tabCarres[i]*tabCarres[i]#i"/>
            <item algoitem="FIN_POUR" code="14#finpour"/>
        </item>
        <item algoitem="POUR i ALLANT_DE 0 A 4" code="12#i#0#4">
            <item algoitem="DEBUT_POUR" code="13#debutpour"/>
            <item algoitem="AFFICHER tabCarres[i]" code="3#tabCarres#0#i"/>
            <item algoitem="AFFICHER &quot;  &quot;" code="4#  #0"/>
            <item algoitem="FIN_POUR" code="14#finpour"/>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
