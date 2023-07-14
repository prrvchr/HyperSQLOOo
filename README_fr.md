# Documentation

**This [document][2] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][3].**

# version [1.0.0][4]

## Introduction:

**HsqlDriverOOo** fait partie d'une [Suite][5] d'extensions [LibreOffice][6] et/ou [OpenOffice][7] permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet:
- De surmonter le [dysfonctionnement 139538][8] pour les utilisateurs de **LibreOffice sur Linux**.
- D'utiliser HsqlDB en mode intégré, rendant la base de donnée portable (un seul fichier odb), avec la version du pilote HsqlDB de votre choix.
- De profitez des améliorations offertes par l'extension [jdbcDriverOOo][9] avec la gestion des utilisateurs et des rôles (groupes).
- De remplacer le pilote [HsqlDB 1.8][10] intégré fourni par LibreOffice / OpenOffice, une version qui aura bientôt plus de 20 ans, par une version HsqlDB récente et à votre choix.

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][11].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][12] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

## Prérequis:

[HsqlDB][13] est une base de données écrite en Java.  
Son utilisation nécessite [l'installation et la configuration][14] dans LibreOffice / OpenOffice d'un **JRE version 11 ou ultérieure**.  
Je vous recommande [Adoptium][15] comme source d'installation de Java.

Si vous utilisez **LibreOffice sous Linux**, alors vous êtes sujet au [dysfonctionnement 139538][8]. Pour contourner le problème, veuillez **désinstaller les paquets** avec les commandes:
- `sudo apt remove libreoffice-sdbc-hsqldb` (pour désinstaller le paquet libreoffice-sdbc-hsqldb)
- `sudo apt remove libhsqldb1.8.0-java` (pour désinstaller le paquet libhsqldb1.8.0-java)

OpenOffice et LibreOffice sous Windows ne sont pas soumis à ce dysfonctionnement.

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- Installer l'extension ![jdbcDriverOOo logo][16] **[jdbcDriverOOo.oxt][17]** version 0.0.4.  
Cette extension est nécessaire pour utiliser HsqlDB version 2.5.1 avec toutes ses fonctionnalités.

- Installer l'extension ![HsqlDriverOOo logo][1] **[HsqlDriverOOo.oxt][18]** version 1.0.0.

Redémarrez LibreOffice / OpenOffice après l'installation.

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![HsqlDriverOOo screenshot 1][19]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote HsqlDB intégré
- cliquer sur le bouton: Suivant

![HsqlDriverOOo screenshot 2][20]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![HsqlDriverOOo screenshot 3][21]

Maintenant à vous d'en profiter...

### Comment migrer une base de données intégrée:

Si vous souhaitez migrer une base de données intégrée (HsqlDB version 1.8.0) vers une version plus récente (par exemple 2.5.1), procédez comme suit:
- 1 - Faite une copie (sauvegarde) de votre base de données (fichier odb).
- 2 - Si elles ne sont pas déjà installées, installez cette extension et l'extension [jdbcDriverOOo][9].
- 3 - Changez l'archive du pilote HsqlDB dans: **Outils -> Options -> Pilotes Base -> Pilote JDBC -> Options des pilotes JDBC**, par une version [1.8.1.10][10].
- 4 - Redémarrer LibreOffice / OpenOffice aprés le changement du pilote (hsqldb.jar).
- 5 - Ouvrir le fichier odb dans Base (double clique sur le fichier odb).
- 6 - Dans Base allez à: **Outils -> SQL** et tapez la commande SQL: `SHUTDOWN COMPACT` ou `SHUTDOWN SCRIPT`.
- 7 - Changez l'archive du pilote HsqlDB dans: **Outils -> Options -> Pilotes Base -> Pilote JDBC -> Options des pilotes JDBC**, par une version [2.4.0][22] ou [2.4.1][23] ou [2.5.0][24].
- 8 - Redémarrer LibreOffice / OpenOffice aprés le changement du pilote (hsqldb.jar).
- Recommencez cette procédure à l'étape 5 en utilisant la version [2.5.1][25].
- Pour finir, répétez l'étape 5 puis 6.

## A été testé avec:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

Je vous encourage en cas de problème :-(  
de créer un [dysfonctionnement][12]  
J'essaierai de le résoudre ;-)

## Historique:

### Ce qui a été fait pour la version 0.0.1:

- La rédaction de ce pilote a été facilitée par une [discussion avec Villeroy][26], sur le forum OpenOffice, que je tiens à remercier, car la connaissance ne vaut que si elle est partagée...

- Utilisation de l'ancienne version de HsqlDB 1.8.0 (peut être facilement mise à jour).

- Ajout d'une boîte de dialogue permettant de mettre à jour le pilote (hsqldb.jar) dans: Outils -> Options -> Pilotes Base -> Pilote HsqlDB intégré

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.2:

- Maintenant, le pilote divise automatiquement un odb lorsqu'il est ouvert... Cela permet la conversion des fichiers odb produits par le pilote LibreOffice / OpenOffice HsqlDB intégré ;-)

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.3:

- Je tiens particulièrement à remercier fredt à [hsqldb.org][13] pour:

    - Son accueil pour ce projet et sa permission d'utiliser le logo HsqlDB dans l'extension.

    - La qualité de sa base de données HsqlDB.

- Fonctionne désormais avec OpenOffice sous Windows.

- Lors de la décompression, un conflit de nom de fichier affiche désormais une erreur précise.

- Gère désormais correctement les espaces dans les noms de fichiers et les chemins.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.4:

- Modification de [Driver.py][27] afin de rendre possible l'utilisation du service Uno: `com.sun.star.sdb.RowSet`.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.5:

- Ecriture d'un [DocumentHandler][28] responsable:
  - De l'extraction des fichiers de base de données contenus dans le fichier **odb** à la connexion.
  - De la sauvegarde des fichiers de base de données dans le fichier **odb** lors de sa fermeture.

- Réécriture de [Driver.py][27] afin de permettre:
  - Son fonctionnement avec le nouveau pilote JDBC fourni par l'extension [jdbcDriverOOo][9] version 0.0.4.
  - La prise en charge du nouveau [DocumentHandler][28] afin de rendre les fichiers **odb** portables tels qu'ils étaient dans LibreOffice / OpenOffce avec la version 1.8 de HsqlDB.

- Beaucoup d'autres correctifs...

### Que reste-t-il à faire pour la version 0.0.5:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: <img/HsqlDriverOOo.svg>
[2]: <https://prrvchr.github.io/HsqlDriverOOo/>
[3]: <https://prrvchr.github.io/HsqlDriverOOo/source/HsqlDriverOOo/registration/TermsOfUse_fr>
[4]: <https://prrvchr.github.io/HsqlDriverOOo/README_fr#historique>
[5]: <https://prrvchr.github.io/README_fr>
[6]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[7]: <https://www.openoffice.org/fr/Telecharger/>
[8]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[9]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[10]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[11]: <https://github.com/prrvchr/HsqlDriverOOo/>
[12]: <https://github.com/prrvchr/HsqlDriverOOo/issues/new>
[13]: <http://hsqldb.org/>
[14]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10/fr>
[15]: <https://adoptium.net/releases.html?variant=openjdk11>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg>
[17]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/jdbcDriverOOo.oxt>
[18]: <https://github.com/prrvchr/HsqlDriverOOo/raw/master/HsqlDriverOOo.oxt>
[19]: <img/HsqlDriverOOo-1_fr.png>
[20]: <img/HsqlDriverOOo-2_fr.png>
[21]: <img/HsqlDriverOOo-3_fr.png>
[22]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[23]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[24]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[25]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.1/hsqldb-2.5.1.jar>
[26]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[27]: <https://github.com/prrvchr/HsqlDriverOOo/blob/master/source/HsqlDriverOOo/service/Driver.py>
[28]: <https://github.com/prrvchr/HsqlDriverOOo/blob/master/uno/lib/uno/database/documenthandler.py>
