<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER &quot;  &quot;" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="actif" fctcode=""/>
    <F2 F2etat="inactif" F2para="" F2lignes="" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="nb EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb"/>
        <item algoitem="tabNb EST_DU_TYPE LISTE" code="1#LISTE#tabNb"/>
        <item algoitem="indiceTab EST_DU_TYPE NOMBRE" code="1#NOMBRE#indiceTab"/>
        <item algoitem="i EST_DU_TYPE NOMBRE" code="1#NOMBRE#i"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="indiceTab PREND_LA_VALEUR 0" code="5#indiceTab#0#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez un nombre: &quot;" code="4#Entrez un nombre: #0"/>
        <item algoitem="LIRE nb" code="2#nb#pasliste"/>
        <item algoitem="TANT_QUE (nb >=0) FAIRE" code="15#nb >=0">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="SI (nb%2==0) ALORS" code="6#nb%2==0">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="tabNb[indiceTab] PREND_LA_VALEUR nb*nb" code="5#tabNb#nb*nb#indiceTab"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
                <item algoitem="SINON" code="9#sinon">
                    <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                    <item algoitem="tabNb[indiceTab] PREND_LA_VALEUR nb-1" code="5#tabNb#nb-1#indiceTab"/>
                    <item algoitem="FIN_SINON" code="11#finsinon"/>
                </item>
            </item>
            <item algoitem="indiceTab PREND_LA_VALEUR indiceTab+1" code="5#indiceTab#indiceTab+1#pasliste"/>
            <item algoitem="AFFICHER &quot;Saisir un nouveau nombre:&quot;" code="4#Saisir un nouveau nombre:#0"/>
            <item algoitem="LIRE nb" code="2#nb#pasliste"/>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
        <item algoitem="POUR i ALLANT_DE 0 A indiceTab-1" code="12#i#0#indiceTab-1">
            <item algoitem="DEBUT_POUR" code="13#debutpour"/>
            <item algoitem="AFFICHER tabNb[i]" code="3#tabNb#0#i"/>
            <item algoitem="AFFICHER &quot;  &quot;" code="4#  #0"/>
            <item algoitem="FIN_POUR" code="14#finpour"/>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
