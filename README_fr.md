<!--
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020 https://prrvchr.github.io                                     ║
║                                                                                    ║
║   Permission is hereby granted, free of charge, to any person obtaining            ║
║   a copy of this software and associated documentation files (the "Software"),     ║
║   to deal in the Software without restriction, including without limitation        ║
║   the rights to use, copy, modify, merge, publish, distribute, sublicense,         ║
║   and/or sell copies of the Software, and to permit persons to whom the Software   ║
║   is furnished to do so, subject to the following conditions:                      ║
║                                                                                    ║
║   The above copyright notice and this permission notice shall be included in       ║
║   all copies or substantial portions of the Software.                              ║
║                                                                                    ║
║   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                  ║
║   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES                  ║
║   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.        ║
║   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY             ║
║   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,             ║
║   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE       ║
║   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                    ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
-->
# [![HyperSQLOOo logo][1]][2] Documentation

**This [document][3] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][4].**

# version [1.1.3][5]

## Introduction:

**HyperSQLOOo** fait partie d'une [Suite][6] d'extensions [LibreOffice][7] ~~et/ou [OpenOffice][8]~~ permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet:
- De surmonter le [dysfonctionnement 139538][9] pour les utilisateurs de **LibreOffice sur Linux**.
- D'utiliser la base de données HyperSQL en mode intégré, rendant la base de donnée portable (un seul fichier odb).
- De profitez des améliorations offertes par l'extension [jdbcDriverOOo][10]:
    - La gestion des utilisateurs et des rôles (groupes).
    - La gestion des nanosecondes et des fuseaux horaires.
    - La gestion de `java.sql.Array`, `java.sql.Blob`, `java.sql.Clob`...
- De remplacer le pilote [HsqlDB 1.8][11] intégré fourni par LibreOffice / OpenOffice, une version qui aura bientôt plus de 20 ans, par une version HsqlDB récente et à votre choix.
- **De supporter les propriétés [ACID][12] de la base de données [HsqlDB][13] sous jancente.**

**Attention : Si vous souhaitez migrer des fichiers odb créés avec LibreOffice ou OpenOffice et HsqlDB version 1.8, il est impératif d'utiliser la version 1.1.2 ou supérieure de HyperSQLOOo sinon il y a un grand risque de perte de données. La procédure de migration est donnée dans la section [Comment migrer une base de données intégrée][14]. Quoi qu'il arrive, gardez vos sauvegardes à jour.**

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][15].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][16] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

L'extension HyperSQLOOo utilise l'extension jdbcDriverOOo pour fonctionner.  
Elle doit donc répondre aux [prérequis de l'extension jdbcDriverOOo][17].

Cette extension ne peut pas être installée avec l'extension [SQLiteOOo][18].  
C'est l'une ou l'autre, mais pour le moment, elles ne peuvent pas fonctionner ensemble (voir [dysfonctionnement #156471][19]).

**Sous Linux et macOS les paquets Python** utilisés par l'extension, peuvent s'il sont déja installé provenir du système et donc, **peuvent ne pas être à jour**.  
Afin de s'assurer que vos paquets Python sont à jour il est recommandé d'utiliser l'option **Info système** dans les Options de l'extension accessible par:  
**Outils -> Options -> Pilotes Base -> Pilote HsqlDB intégré -> Voir journal -> Info système**  
Si des paquets obsolètes apparaissent, vous pouvez les mettre à jour avec la commande:  
`pip install --upgrade <package-name>`

Pour plus d'information voir: [Ce qui a été fait pour la version 1.1.0][20].

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![jdbcDriverOOo logo][21]][10] Installer l'extension **[jdbcDriverOOo.oxt][22]** [![Version][23]][22]

  Cette extension est nécessaire pour utiliser HsqlDB version 2.7.2 avec toutes ses fonctionnalités.

- ![HyperSQLOOo logo][24] Installer l'extension **[HyperSQLOOo.oxt][25]** version [![Version][26]][25]

Redémarrez LibreOffice après l'installation.  
**Attention, redémarrer LibreOffice peut ne pas suffire.**
- **Sous Windows** pour vous assurer que LibreOffice redémarre correctement, utilisez le Gestionnaire de tâche de Windows pour vérifier qu'aucun service LibreOffice n'est visible après l'arrêt de LibreOffice (et tuez-le si ç'est le cas).
- **Sous Linux ou macOS** vous pouvez également vous assurer que LibreOffice redémarre correctement, en le lançant depuis un terminal avec la commande `soffice` et en utilisant la combinaison de touches `Ctrl + C` si après l'arrêt de LibreOffice, le terminal n'est pas actif (pas d'invité de commande).

___

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![HyperSQLOOo screenshot 1][27]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote HsqlDB intégré
- cliquer sur le bouton: Suivant

![HyperSQLOOo screenshot 2][28]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![HyperSQLOOo screenshot 3][29]

Maintenant à vous d'en profiter...

### Comment migrer une base de données intégrée:

Si vous souhaitez migrer une base de données intégrée (HsqlDB version 1.8.0) vers une version plus récente (par exemple 2.7.2), procédez comme suit:
1. Faite une copie (sauvegarde) de votre base de données (fichier odb).
2. Si elles ne sont pas déjà installées, installez cette extension et l'extension [jdbcDriverOOo][10].
3. Changez l'archive du pilote HsqlDB dans: **Outils -> Options -> Pilotes Base -> Pilote JDBC -> Options des pilotes JDBC -> Archive -> Changer**, par une version [1.8.1.10][11].
4. Redémarrer LibreOffice / OpenOffice aprés le changement du pilote (hsqldb.jar).
5. Ouvrir le fichier odb dans Base (double clique sur le fichier odb).
6. Dans Base allez à: **Outils -> SQL** et tapez la commande SQL: `SHUTDOWN COMPACT` ou `SHUTDOWN SCRIPT`.

- Recommencez cette procédure à l'étape 3 en utilisant une version [2.4.0][30] ou [2.4.1][31] ou [2.5.0][32].
- Recommencez cette procédure à l'étape 3 en utilisant la version [2.7.2][33].

___

## Comment ça marche:

HyperSQLOOo est un service [com.sun.star.sdbc.Driver][34] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][10] permettant de stocker la base de données HsqlDB dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, plusieurs choses sont faites:
  - S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers HsqlDB sont extraits du répertoire **database** du fichier odb (décompression).
  - L'extension [jdbcDriverOOo][10] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][35] à partir du chemin du **sous-répertoire** + `/hsqldb`.
  - Si la connexion réussi, un [DocumentHandler][36] est ajouté en tant que [com.sun.star.util.XCloseListener][37] et [com.sun.star.document.XStorageChangeListener][38] au fichier odb.
  - Si la connexion échoue et que les fichiers ont été extraits lors de la phase 1, le **sous-répertoire** est supprimé.
- Lors de la fermeture ou du changement de nom (Enregistrer sous) du fichier odb, si la connexion a réussi, le [DocumentHandler][36] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (zip), puis supprime le **sous-répertoire**.

Le but principal de ce mode de fonctionnement est de profiter des caractéristiques ACID de la base de données sous-jacente en cas de fermeture anormale de LibreOffice.
En contre partie, la fonction: **fichier -> Sauvegarder** n'a **aucun effet sur la base de données sous jacente**. Seul la fermeture du fichier odb ou son enregistrement sous un nom different (Fichier -> Enregistrer sous) effectura la sauvegarde de la base de donnée dans le fichier odb.

___

## A été testé avec:

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

* LibreOffice 24.2.1.2 - Ubuntu 22.04

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][16]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 0.0.1:

- La rédaction de ce pilote a été facilitée par une [discussion avec Villeroy][39], sur le forum OpenOffice, que je tiens à remercier, car la connaissance ne vaut que si elle est partagée...

- Utilisation de l'ancienne version de HsqlDB 1.8.0 (peut être facilement mise à jour).

- Ajout d'une boîte de dialogue permettant de mettre à jour le pilote (hsqldb.jar) dans: Outils -> Options -> Pilotes Base -> Pilote HsqlDB intégré

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.2:

- Maintenant, le pilote divise automatiquement un odb lorsqu'il est ouvert... Cela permet la conversion des fichiers odb produits par le pilote LibreOffice / OpenOffice HsqlDB intégré :wink:

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

- Modification de [Driver.py][40] afin de rendre possible l'utilisation du service Uno: `com.sun.star.sdb.RowSet`.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.5:

- Ecriture d'un [DocumentHandler][36] responsable:
    - De l'extraction des fichiers de base de données contenus dans le fichier **odb** à la connexion.
    - De la sauvegarde des fichiers de base de données dans le fichier **odb** lors de sa fermeture.

- Réécriture de [Driver.py][40] afin de permettre:
    - Son fonctionnement avec le nouveau pilote JDBC fourni par l'extension [jdbcDriverOOo][10] version 0.0.4.
    - La prise en charge du nouveau [DocumentHandler][36] afin de rendre les fichiers **odb** portables tels qu'ils étaient dans LibreOffice / OpenOffice avec la version 1.8 de HsqlDB.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 1.0.0:

- Renommage de l'extension de HsqlDBembeddedOOo en HsqlDriverOOo.

- Integration de HyperSQL version 2.7.2.

### Ce qui a été fait pour la version 1.0.1:

- Renommage de l'extension de HsqlDriverOOo en HyperSQLOOo.

- Résolution du [dysfonctionnement 156511][41] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][42] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **HyperSQLOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Ce qui a été fait pour la version 1.1.0:

- Tous les paquets Python nécessaires à l'extension sont désormais enregistrés dans un fichier [requirements.txt][43] suivant la [PEP 508][44].
- Désormais si vous n'êtes pas sous Windows alors les paquets Python nécessaires à l'extension peuvent être facilement installés avec la commande:  
  `pip install requirements.txt`
- Modification de la section [Prérequis][45].

### Ce qui a été fait pour la version 1.1.1:

- Prise en charge des [nouvelles fonctionnalités][46] de **jdbcDriverOOo 1.1.2**.

### Ce qui a été fait pour la version 1.1.2:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.3.1**.
- Lors de l'enregistrement sous un nom différent, la base de données si ouverte sera fermée correctement.
- Lors de l'ouverture d'un fichier odb, si la connexion échoue, pour éviter la destruction des données, la recompression des fichiers de la base de données n'aura pas lieu. Merci à Robert d'avoir su détecter ce [dysfonctionnement][47].

### Ce qui a été fait pour la version 1.1.3:

- Utilisation du nouveau format de données implémenté dans la version 1.1.2. Par conséquent, si vous devez ouvrir des fichiers odb créés avec une version inférieure à 1.1.2, vous devez d'abord les ouvrir avec la version 1.1.2, sinon une erreur sera générée.

### Que reste-t-il à faire pour la version 1.1.3:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: </img/hypersql.svg#collapse>
[2]: <https://prrvchr.github.io/HyperSQLOOo/>
[3]: <https://prrvchr.github.io/HyperSQLOOo/>
[4]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_fr>
[5]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-113>
[6]: <https://prrvchr.github.io/README_fr>
[7]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[8]: <https://www.openoffice.org/fr/Telecharger/>
[9]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[10]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[11]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[12]: <https://fr.wikipedia.org/wiki/Propri%C3%A9t%C3%A9s_ACID>
[13]: <http://hsqldb.org/>
[14]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#comment-migrer-une-base-de-donn%C3%A9es-int%C3%A9gr%C3%A9e>
[15]: <https://github.com/prrvchr/HyperSQLOOo/>
[16]: <https://github.com/prrvchr/HyperSQLOOo/issues/new>
[17]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#pr%C3%A9requis>
[18]: <https://prrvchr.github.io/SQLiteOOo/README_fr#prérequis>
[19]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[20]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-110>
[21]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[22]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[23]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[24]: <img/HyperSQLOOo.svg#middle>
[25]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[26]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.1.3#right>
[27]: <img/HyperSQLOOo-1_fr.png>
[28]: <img/HyperSQLOOo-2_fr.png>
[29]: <img/HyperSQLOOo-3_fr.png>
[30]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[31]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[32]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[33]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.7.2/hsqldb-2.7.2.jar>
[34]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[35]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[36]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/documenthandler.py>
[37]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[38]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[39]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[40]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/driver.py>
[41]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[42]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[43]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/requirements.txt>
[44]: <https://peps.python.org/pep-0508/>
[45]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#pr%C3%A9requis>
[46]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-112>
[47]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471#c54>
