# Documentation

**This [document][1] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][2].**

# version [1.0.2][3]

## Introduction:

**HyperSQLOOo** fait partie d'une [Suite][4] d'extensions [LibreOffice][5] et/ou [OpenOffice][6] permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet:
- De surmonter le [dysfonctionnement 139538][7] pour les utilisateurs de **LibreOffice sur Linux**.
- D'utiliser la base de données HyperSQL en mode intégré, rendant la base de donnée portable (un seul fichier odb).
- De profitez des améliorations offertes par l'extension [jdbcDriverOOo][8]:
    - La gestion des utilisateurs et des rôles (groupes).
    - La gestion des nanosecondes et des fuseaux horaires.
    - La gestion de `java.sql.Array`, `java.sql.Blob`, `java.sql.Clob`...
- De remplacer le pilote [HsqlDB 1.8][9] intégré fourni par LibreOffice / OpenOffice, une version qui aura bientôt plus de 20 ans, par une version HsqlDB récente et à votre choix.

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][10].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][11] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

[HsqlDB][12] est une base de données écrite en Java.  
Son utilisation nécessite [l'installation et la configuration][13] dans LibreOffice / OpenOffice d'un **JRE version 11 ou ultérieure**.  
Je vous recommande [Adoptium][14] comme source d'installation de Java.

Cette extension ne peut pas être installée avec l'extension [SQLiteOOo][15]. C'est l'une ou l'autre, mais pour le moment, elles ne peuvent pas fonctionner ensemble.

Si vous utilisez **LibreOffice sous Linux**, alors vous êtes sujet au [dysfonctionnement 139538][7]. Pour contourner le problème, veuillez **désinstaller les paquets** avec les commandes:
- `sudo apt remove libreoffice-sdbc-hsqldb` (pour désinstaller le paquet libreoffice-sdbc-hsqldb)
- `sudo apt remove libhsqldb1.8.0-java` (pour désinstaller le paquet libhsqldb1.8.0-java)

OpenOffice et LibreOffice sous Windows ne sont pas soumis à ce dysfonctionnement.

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![jdbcDriverOOo logo][16]][8] Installer l'extension **[jdbcDriverOOo.oxt][17]** [![Version][18]][17]

    Cette extension est nécessaire pour utiliser HsqlDB version 2.7.2 avec toutes ses fonctionnalités.

- ![HyperSQLOOo logo][19] Installer l'extension **[HyperSQLOOo.oxt][20]** version [![Version][21]][20]

Redémarrez LibreOffice / OpenOffice après l'installation.

___

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![HyperSQLOOo screenshot 1][22]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote HsqlDB intégré
- cliquer sur le bouton: Suivant

![HyperSQLOOo screenshot 2][23]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![HyperSQLOOo screenshot 3][24]

Maintenant à vous d'en profiter...

### Comment migrer une base de données intégrée:

Si vous souhaitez migrer une base de données intégrée (HsqlDB version 1.8.0) vers une version plus récente (par exemple 2.7.2), procédez comme suit:
1. Faite une copie (sauvegarde) de votre base de données (fichier odb).
2. Si elles ne sont pas déjà installées, installez cette extension et l'extension [jdbcDriverOOo][8].
3. Changez l'archive du pilote HsqlDB dans: **Outils -> Options -> Pilotes Base -> Pilote JDBC -> Options des pilotes JDBC -> Archive -> Changer**, par une version [1.8.1.10][9].
4. Redémarrer LibreOffice / OpenOffice aprés le changement du pilote (hsqldb.jar).
5. Ouvrir le fichier odb dans Base (double clique sur le fichier odb).
6. Dans Base allez à: **Outils -> SQL** et tapez la commande SQL: `SHUTDOWN COMPACT` ou `SHUTDOWN SCRIPT`.

- Recommencez cette procédure à l'étape 3 en utilisant une version [2.4.0][25] ou [2.4.1][26] ou [2.5.0][27].
- Recommencez cette procédure à l'étape 3 en utilisant la version [2.7.2][28].

___

## Comment ça marche:

HyperSQLOOo est un service [com.sun.star.sdbc.Driver][29] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][8] permettant de stocker la base de données HyperSQL dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, trois choses sont faites:
    1. S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers HyperSQL sont extraits du répertoire **database** du fichier odb (décompression).
    2. Un [DocumentHandler][30] est ajouté en tant que [com.sun.star.util.XCloseListener][31] et [com.sun.star.document.XStorageChangeListener][32] au fichier odb.
    3. L'extension [jdbcDriverOOo][8] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][33] à partir du chemin du **sous-répertoire** + `nom_du_fichier_odb`.

- Lors de la fermeture ou du renommage (Enregistrer sous) d'un fichier odb, le [DocumentHandler][30] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (compression) puis supprime le **sous-répertoire**.

___

## A été testé avec:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][11]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 0.0.1:

- La rédaction de ce pilote a été facilitée par une [discussion avec Villeroy][34], sur le forum OpenOffice, que je tiens à remercier, car la connaissance ne vaut que si elle est partagée...

- Utilisation de l'ancienne version de HsqlDB 1.8.0 (peut être facilement mise à jour).

- Ajout d'une boîte de dialogue permettant de mettre à jour le pilote (hsqldb.jar) dans: Outils -> Options -> Pilotes Base -> Pilote HsqlDB intégré

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.2:

- Maintenant, le pilote divise automatiquement un odb lorsqu'il est ouvert... Cela permet la conversion des fichiers odb produits par le pilote LibreOffice / OpenOffice HsqlDB intégré :wink:

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.3:

- Je tiens particulièrement à remercier fredt à [hsqldb.org][12] pour:

    - Son accueil pour ce projet et sa permission d'utiliser le logo HsqlDB dans l'extension.

    - La qualité de sa base de données HsqlDB.

- Fonctionne désormais avec OpenOffice sous Windows.

- Lors de la décompression, un conflit de nom de fichier affiche désormais une erreur précise.

- Gère désormais correctement les espaces dans les noms de fichiers et les chemins.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.4:

- Modification de [Driver.py][35] afin de rendre possible l'utilisation du service Uno: `com.sun.star.sdb.RowSet`.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.5:

- Ecriture d'un [DocumentHandler][30] responsable:
    - De l'extraction des fichiers de base de données contenus dans le fichier **odb** à la connexion.
    - De la sauvegarde des fichiers de base de données dans le fichier **odb** lors de sa fermeture.

- Réécriture de [Driver.py][35] afin de permettre:
    - Son fonctionnement avec le nouveau pilote JDBC fourni par l'extension [jdbcDriverOOo][8] version 0.0.4.
    - La prise en charge du nouveau [DocumentHandler][30] afin de rendre les fichiers **odb** portables tels qu'ils étaient dans LibreOffice / OpenOffice avec la version 1.8 de HsqlDB.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 1.0.0:

- Renommage de l'extension de HsqlDBembeddedOOo en HsqlDriverOOo.

- Integration de HyperSQL version 2.7.2.

### Ce qui a été fait pour la version 1.0.1:

- Renommage de l'extension de HsqlDriverOOo en HyperSQLOOo.

- Résolution du [dysfonctionnement 156511][36] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][37] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **HyperSQLOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Que reste-t-il à faire pour la version 1.0.2:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: <https://prrvchr.github.io/HyperSQLOOo/>
[2]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_fr>
[3]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#historique>
[4]: <https://prrvchr.github.io/README_fr>
[5]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[6]: <https://www.openoffice.org/fr/Telecharger/>
[7]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[8]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[9]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[10]: <https://github.com/prrvchr/HyperSQLOOo/>
[11]: <https://github.com/prrvchr/HyperSQLOOo/issues/new>
[12]: <http://hsqldb.org/>
[13]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10/fr>
[14]: <https://adoptium.net/releases.html?variant=openjdk11>
[15]: <https://github.com/prrvchr/SQLiteOOo/README_fr>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[17]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[18]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[19]: <img/HyperSQLOOo.svg#middle>
[20]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[21]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.0.2#right>
[22]: <img/HyperSQLOOo-1_fr.png>
[23]: <img/HyperSQLOOo-2_fr.png>
[24]: <img/HyperSQLOOo-3_fr.png>
[25]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[26]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[27]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[28]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.7.2/hsqldb-2.7.2.jar>
[29]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[30]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/documenthandler.py>
[31]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[32]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[33]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[34]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[35]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/driver.py>
[36]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[37]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
