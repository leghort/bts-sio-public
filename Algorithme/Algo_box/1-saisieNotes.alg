<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER moyenne" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2para="" F2lignes="" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="nbNotes EST_DU_TYPE NOMBRE" code="1#NOMBRE#nbNotes"/>
        <item algoitem="note EST_DU_TYPE NOMBRE" code="1#NOMBRE#note"/>
        <item algoitem="somme EST_DU_TYPE NOMBRE" code="1#NOMBRE#somme"/>
        <item algoitem="moyenne EST_DU_TYPE NOMBRE" code="1#NOMBRE#moyenne"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="nbNotes PREND_LA_VALEUR 0" code="5#nbNotes#0#pasliste"/>
        <item algoitem="somme PREND_LA_VALEUR 0" code="5#somme#0#pasliste"/>
        <item algoitem="note PREND_LA_VALEUR 0" code="5#note#0#pasliste"/>
        <item algoitem="TANT_QUE (note >=0) FAIRE" code="15#note >=0">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="somme PREND_LA_VALEUR somme+note" code="5#somme#somme+note#pasliste"/>
            <item algoitem="LIRE note" code="2#note#pasliste"/>
            <item algoitem="nbNotes PREND_LA_VALEUR nbNotes+1" code="5#nbNotes#nbNotes+1#pasliste"/>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
        <item algoitem="moyenne PREND_LA_VALEUR somme/(nbNotes-1)" code="5#moyenne#somme/(nbNotes-1)#pasliste"/>
        <item algoitem="AFFICHER &quot;La moyenne vaut: &quot;" code="4#La moyenne vaut: #0"/>
        <item algoitem="AFFICHER moyenne" code="3#moyenne#1#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
