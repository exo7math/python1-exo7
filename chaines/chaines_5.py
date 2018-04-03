
##############################
# Chaînes de caractères - Analyse statistique d'un texte
##############################


import random # Uniquement pour créer l'énigme

##############################
# Activité 5 - Analyse statistique d'un texte
##############################

## Question supprmiée ##


def nombre_E(phrase):
    """ Compte le nombre de "E"
    Entrée : une phrase en majuscule
    Sortie : le nombre de "E" """

    nb = 0
    for car in phrase:
        if car == "E":
            nb = nb + 1

    return nb


# Test 
phrase = "ESPRIT ES TU LA"
print("La phrase",phrase,"contient",nombre_E(phrase),"fois la lettre E")



## Question 1 ##


def occurrences_lettre(lettre,phrase):
    """ Compte le nombre d'occurrences d'une lettre donnée dans phrase
    Entrée : une lettre et une phrase en majuscule
    Sortie : le nombre de lettres """

    nb = 0
    for car in phrase:
        if car == lettre:
            nb = nb + 1

    return nb


# Test 
phrase = "ESPRIT ES TU LA"
print("La phrase",phrase,"contient",occurrences_lettre("S",phrase),"fois la lettre S")



## Question 2 ##

def nombre_lettres(phrase):
    """ Compte le nombre total de lettres
    Entrée : une phrase en majuscule
    Sortie : le nombre total de lettres de "A" à "Z" """

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    nb = 0
    for car in phrase:
        if car in alphabet:
            nb = nb + 1

    return nb


# Test 
phrase = "ESPRIT ES TU LA"
print("La phrase",phrase,"contient",nombre_lettres(phrase),"lettres")



## Question 3 ##

def pourcentage_lettre(lettre,phrase):
    """ Calcule le ratio d'une lettre donnée dans phrase
    Entrée : une lettre et une phrase en majuscule
    Sortie : le pourcentage d'apparition de la lettre """

    nb_lettres = occurrences_lettre(lettre,phrase)
    nb_total = nombre_lettres(phrase)
    pourcentage = nb_lettres/nb_total*100
    
    return pourcentage


# Test 
phrase = "ESPRIT ES TU LA"
pourcentage = pourcentage_lettre("S",phrase)
print("La phrase",phrase,"contient",pourcentage,"% de lettre S")
print("Pourcentage arrondi :","{0:.2f}".format(pourcentage))


## Question 4 ##

def affiche_frequences(phrase):
    """ Calcule le ratio de toutes les lettres dans une phrase
    Entrée : uune phrase en majuscule
    Sortie : l'affichage des pourcentage d'apparition des lettres """

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for lettre in alphabet:
        pourcentage = pourcentage_lettre(lettre,phrase)
        print(lettre," : ","{0:.2f}".format(pourcentage))

    return


# SECRET ------------------
# Création de l'énigme

def myshuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

#for mot in phrase.split():
#  print(list(mot))
#  print(myshuffle(list(mot)))

# Le corbeau et le renard - Jean de la Fontaine
phrase1 = "MAITRE CORBEAU SUR UN ARBRE PERCHE TENAIT EN SON BEC UN FROMAGE MAITRE RENARD PAR L ODEUR ALLECHE LUI TINT A PEU PRES CE LANGAGE ET BONJOUR MONSIEUR DU CORBEAU QUE VOUS ETES JOLI QUE VOUS ME SEMBLEZ BEAU SANS MENTIR SI VOTRE RAMAGE SE RAPPORTE A VOTRE PLUMAGE VOUS ETES LE PHENIX DES HOTES DE CES BOIS A CES MOTS LE CORBEAU NE SE SENT PAS DE JOIE ET POUR MONTRER SA BELLE VOIX IL OUVRE UN LARGE BEC LAISSE TOMBER SA PROIE LE RENARD S EN SAISIT ET DIT MON BON MONSIEUR APPRENEZ QUE TOUT FLATTEUR VIT AUX DEPENS DE CELUI QUI L ECOUTE CETTE LECON VAUT BIEN UN FROMAGE SANS DOUTE LE CORBEAU HONTEUX ET CONFUS JURA MAIS UN PEU TARD QU ON NE L Y PRENDRAIT PLUS"

#phrase_mystere1 = ' '.join([''.join(myshuffle(list(mot))) for mot in phrase1.split() ])

# Le roi de aulnes - Goethe
phrase2 = "WER REITET SO SPAT DURCH NACHT UND WIND ES IST DER VATER MIT SEINEM KIND ER HAT DEN KNABEN WOHL IN DEM ARM ER FASST IHN SICHER ER HALT IHN WARM MEIN SOHN WAS BIRGST DU SO BANG DEIN GESICHT SIEHST VATER DU DEN ERLKONIG NICHT DEN ERLENKONIG MIT KRON UND SCHWEIF  MEIN SOHN ES IST EIN NEBELSTREIF DU LIEBES KIND KOMM GEH MIT MIR GAR SCHONE SPIELE SPIEL ICH MIT DIR MANCH BUNTE BLUMEN SIND AN DEM STRAND MEINE MUTTER HAT MANCH GULDEN GEWAND MEIN VATER MEIN VATER UND HOREST DU NICHT WAS ERLENKONIG MIR LEISE VERSPRICHT SEI RUHIG BLEIBE RUHIG MEIN KIND IN DURREN BLATTERN SAUSELT DER WIND" 

#phrase_mystere2 = ' '.join([''.join(myshuffle(list(mot))) for mot in phrase2.split() ])

# Cent ans de solitude - Gabriel Garcia Marquez
phrase3 = "FASCINADO POR UNA REALIDAD INMEDIATA QUE ENTONCES LE RESULTO MAS FANTASTICA QUE EL VASTO UNIVERSO DE SU IMAGINACION PERDIO TODO INTERES POR EL LABORATORIO DE ALQUIMIA PUSO A DESCANSAR LA MATERIA EXTENUADA POR LARGOS MESES DE MANIPULACION Y VOLVIO A SER EL HOMBRE EMPRENDEDOR DE LOS PRIMEROS TIEMPOS QUE DECIDIA EL TRAZADO DE LAS CALLES Y LA POSICION DE LAS NUEVAS CASAS Y SE DETERMINO QUE FUERA EL QUIEN DIRIGIERA LA REPARTICION DE LA TIERRA"

phrase_mystere3 = ' '.join([''.join(myshuffle(list(mot))) for mot in phrase3.split() ])

# Sumertimes - Elle Fitzgerald
phrase4 = "SUMMERTIME AND THE LIVING IS EASY FISH ARE JUMPING AND THE COTTON IS HIGH OH YOUR DADDY IS RICH AND YOUR MA IS GOOD LOOKING SO HUSH LITTLE BABY DONT YOU CRY ONE OF THESE MORNINGS YOU RE GONNA RISE UP SINGING AND YOULL SPREAD YOUR WINGS AND YOULL TAKE TO THE SKY BUT TILL THAT MORNING THERE AINT NOTHING CAN HARM YOU WITH DADDY AND MAMMY STANDING BY"

phrase_mystere4 = ' '.join([''.join(myshuffle(list(mot))) for mot in phrase4.split() ])


# FIN SECRET ------------------

# Choix des phrases mystères

phrase_mystere1 = "TMAIER BERACUO RSU NU REBRA PRCEEH EIANTT NE ONS EBC NU GAOFREM EIMATR RERNAD APR L RDUOE LAHECLE UIL TTNI A EUP SREP EC LGNGAEA TE RBONUJO ERMNOUSI DU UBRACEO QUE OVSU EEST LIJO UQE OUVS EM MSZELBE BAEU ASNS MIERNT IS RVETO AGRAME ES PRARPTOE A OEVTR AMGUPLE VUOS SEET EL PNIHXE DSE OSHET ED CSE BIOS A ESC MSOT LE OUBRCEA NE ES ESTN ASP DE IEJO TE OUPR ERRNOTM AS BELEL XOVI IL OREVU NU RGLEA ECB ILESSA EBOMTR AS PIOER EL NRDAER S EN ISIAST TE ITD MNO NOB EUSRMNOI NRPEEAZP QEU UTOT EUTLRFTA IVT XUA SPNEDE DE UECIL UQI L TECEOU TECET NEOCL VATU BNEI UN GMAEORF SNAS TUOED LE EOABURC OHENTXU TE NSCOFU UJRA SMIA UN EPU TRDA UQ NO EN L Y ARRPEIDNT ULSP"

print(phrase_mystere1)

affiche_frequences(phrase_mystere1)

phrase_mystere2 = "WRE TREITE SO TSPA CUDHR AHNCT UND WIND SE STI RED AEVRT MTI ESEIMN IDNK RE ATH END NEABNK WLOH IN EMD AMR ER AFTSS HIN IHSERC RE AHTL HIN MRWA EINM SHNO SAW SRTIBG UD SO NGBA DNEI EIHSGTC ESISTH RAETV UD DEN LERNIOKG NITHC NDE LOENINKGRE TIM OKRN UDN CHWFSEI NEIM NSOH ES STI IEN BIFTRLSEEEN DU BILESE IKDN OMKM EHG MIT MIR RAG ECHNOS EPELSI EIPSL IHC ITM RDI HNCMA BEUTN MBLUNE DINS NA DEM TNDRAS NMIEE UTETMR AHT CAMHN UDNGEL GDAWEN MIEN EATRV MENI VEART DUN OSTHER DU CINTH SAW KNNOEIREGL RIM ILEES PRSTVRCIEH ISE IHGRU BEEILB RIGUH MNEI KNDI NI RDNEUR NATBRLET STAESUL EDR WNID"

print(phrase_mystere2)

affiche_frequences(phrase_mystere2)

phrase_mystere3 = "DSNOACAIF ORP ANU DAEDALRI DNAAEIMTI EQU NNCOSETE EL RSTEOUL SMA AACTFAITNS UQE EL TSVAO OINSRVUE DE US ANIGIICANOM EIORDP TOOD RTEIENS RPO LE ITOABOLRROA ED QIUAMALI USOP A NSSRCAEAD LA TMREAAI NXTADAUEE ROP GOARLS EMESS DE NNAMICLUIAPO Y LOVOIV A RES LE RHMEOB EOMDNEERPRD DE LOS RSOPMRIE OMTSIPE UEQ CIIDADE LE RTDAAOZ ED LSA CELSAL Y LA NICOIOPS ED LAS UESVNA SSACA Y ES ITRMNEEOD QEU AERFU EL UEQIN IIIRDEGAR LA NAIORTREICP DE AL RRTEIA"

print(phrase_mystere3)

affiche_frequences(phrase_mystere3)

phrase_mystere4 = "IMTRUESMME DNA TEH LNGIIV SI EYAS SIFH REA GJPNUIM DNA HET TTNOCO IS GHIH OH OUYR DDADY SI IRHC DAN ROUY MA SI DOGO GKOILON OS USHH LTLIET BBYA NDOT OUY CYR NEO OF HESET GNSRONIM YUO RE NANGO SIER PU SNIGING NAD OULLY EPADRS YUOR GINSW DAN LYOLU KATE OT HET KSY TUB ITLL TATH MGNIRNO EREHT NATI INTGOHN ACN AHMR OYU TWIH DADYD NDA MYMMA NSTIDGAN YB"

print(phrase_mystere4)

affiche_frequences(phrase_mystere4)