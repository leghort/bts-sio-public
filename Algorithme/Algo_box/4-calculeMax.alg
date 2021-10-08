<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER &quot;nb2&quot;" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2para="" F2lignes="" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" totalBoucles="5000000" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="nb1 EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb1"/>
        <item algoitem="nb2 EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb2"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="//Cet algo calcule le plus grand de 2 nombres" code="19#Cet algo calcule le plus grand de 2 nombres"/>
        <item algoitem="nb1 PREND_LA_VALEUR 0" code="5#nb1#0#pasliste"/>
        <item algoitem="nb2 PREND_LA_VALEUR 0" code="5#nb2#0#pasliste"/>
        <item algoitem="TANT_QUE (nb1>=0) FAIRE" code="15#nb1>=0">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="AFFICHER &quot;Entrez un 1er nombre &quot;" code="4#Entrez un 1er nombre #0"/>
            <item algoitem="LIRE nb1" code="2#nb1#pasliste"/>
            <item algoitem="AFFICHER &quot;Entrez un 2eme nombre &quot;" code="4#Entrez un 2eme nombre #0"/>
            <item algoitem="LIRE nb2" code="2#nb2#pasliste"/>
            <item algoitem="SI (nb1>nb2) ALORS" code="6#nb1>nb2">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER nb1" code="3#nb1#1#pasliste"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
                <item algoitem="SINON" code="9#sinon">
                    <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                    <item algoitem="SI (nb2>nb1) ALORS" code="6#nb2>nb1">
                        <item algoitem="DEBUT_SI" code="7#debutsi"/>
                        <item algoitem="AFFICHER &quot;nb2&quot;" code="4#nb2#1"/>
                        <item algoitem="FIN_SI" code="8#finsi"/>
                        <item algoitem="SINON" code="9#sinon">
                            <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                            <item algoitem="AFFICHER &quot;Ces 2 nombres sont egaux&quot;" code="4#Ces 2 nombres sont egaux#1"/>
                            <item algoitem="FIN_SINON" code="11#finsinon"/>
                        </item>
                    </item>
                    <item algoitem="FIN_SINON" code="11#finsinon"/>
                </item>
            </item>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
