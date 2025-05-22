<!--
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020-25 https://prrvchr.github.io                                  ║
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

# version [1.2.0][5]

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

Si vous souhaitez migrer des fichiers odb créés avec LibreOffice ou OpenOffice et HsqlDB version 1.8, il est impératif d'utiliser la dernière version de HyperSQLOOo. La procédure de migration est donnée dans la section [Comment migrer une base de données intégrée][14].

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][15].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][16] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

L'extension HyperSQLOOo utilise l'extension jdbcDriverOOo pour fonctionner.  
Elle doit donc répondre aux [prérequis de l'extension jdbcDriverOOo][20].

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![jdbcDriverOOo logo][21]][10] Installer l'extension **[jdbcDriverOOo.oxt][22]** [![Version][23]][22]

  Cette extension est nécessaire pour utiliser HsqlDB version 2.7.4 avec toutes ses fonctionnalités.

- ![HyperSQLOOo logo][24] Installer l'extension **[HyperSQLOOo.oxt][25]** version [![Version][26]][25]

Redémarrez LibreOffice après l'installation.  
**Attention, redémarrer LibreOffice peut ne pas suffire.**
- **Sous Windows** pour vous assurer que LibreOffice redémarre correctement, utilisez le Gestionnaire de tâche de Windows pour vérifier qu'aucun service LibreOffice n'est visible après l'arrêt de LibreOffice (et tuez-le si ç'est le cas).
- **Sous Linux ou macOS** vous pouvez également vous assurer que LibreOffice redémarre correctement, en le lançant depuis un terminal avec la commande `soffice` et en utilisant la combinaison de touches `Ctrl + C` si après l'arrêt de LibreOffice, le terminal n'est pas actif (pas d'invité de commande).

Après avoir redémarré LibreOffice, vous pouvez vous assurer que l'extension et son pilote sont correctement installés en vérifiant que le pilote `io.github.prrvchr.HyperSQLOOo.Driver` est répertorié dans le **Pool de Connexions**, accessible via le menu: **Outils -> Options -> LibreOffice Base -> Connexions**. Il n'est pas nécessaire d'activer le pool de connexions.

Si le pilote n'est pas répertorié, la raison de l'échec du chargement du pilote peut être trouvée dans la journalisation de l'extension. Cette journalisation est accessible via le menu: **Outils -> Options -> LibreOffice Base -> Pilote HslqDB intégré -> Options de journalisation**.  
La journalisation `HyperSQLLogger` doit d'abord être activée, puis LibreOffice redémarré pour obtenir le message d'erreur dans le journal.

N'oubliez pas au préalable de mettre à jour la version du JRE ou JDK Java installée sur votre ordinateur, cette extension utilise la nouvelle version de jdbcDriverOOo qui nécessite **Java version 17 ou ultérieure** au lieu de Java 11 auparavant.

___

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice aller à: **Fichier -> Nouveau -> Base de données...**:

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

### Comment importer des données depuis un fichier Calc:

LibreOffice vous offre la possibilité d'importer des données depuis Calc directement dans une table existante ou créée pour cet import. Voici la procédure à suivre:
- Vous devez d'abord créer une nouvelle base de données HsqlDB comme décrit dans la [section précédente][30].
- Dans Calc sélectionner une plage de cellules puis: **Edition -> Copier**. Lors de la création d'une nouvelle table, il est possible de mettre dans la première ligne les noms des colonnes telles qu'elles seront importées dans cette nouvelle table.
- Dans Base (ie: la nouvelle base de données HsqlDB), après avoir sélectionné **Tables** dans le volet **Base de données**, faites un clic droit dans le volet **Tables** puis: **Coller** et suivez l'assistant proposé par LibreOffice. **Il est important de nommer la table avec un nom complet** (ie: **PUBLIC.PUBLIC.Table1**). Voir la [documentation HsqlDB][31] sur le **catalogue et le schéma par défaut**.

### Comment migrer une base de données intégrée:

Si vous souhaitez migrer une base de données intégrée (HsqlDB version 1.8.0) vers une version plus récente (par exemple 2.7.2), procédez comme suit:
1. Faite une copie (sauvegarde) de votre base de données (fichier odb).
2. Si elles ne sont pas déjà installées, installez cette extension et l'extension [jdbcDriverOOo][10].
3. Changez l'archive du pilote HsqlDB dans: **Outils -> Options -> Pilotes Base -> Pilote JDBC -> Options des pilotes JDBC -> Archive -> Changer**, par une version [1.8.1.10][11].
4. Redémarrer LibreOffice / OpenOffice aprés le changement du pilote (hsqldb.jar).
5. Ouvrir le fichier odb dans Base (double clique sur le fichier odb).
6. Dans Base allez à: **Outils -> SQL** et tapez la commande SQL: `SHUTDOWN COMPACT` ou `SHUTDOWN SCRIPT`.

- Recommencez cette procédure à l'étape 3 en utilisant une version [2.4.0][32] ou [2.4.1][33] ou [2.5.0][34].
- Recommencez cette procédure à l'étape 3 en utilisant la version [2.7.2][35].

___

## Comment ça marche:

HyperSQLOOo est un service [com.sun.star.sdbc.Driver][36] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][10] permettant de stocker la base de données HsqlDB dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, plusieurs choses sont faites:
  - S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers HsqlDB sont extraits du répertoire **database** du fichier odb (décompression).
  - L'extension [jdbcDriverOOo][10] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][37] à partir du chemin du **sous-répertoire** + `/hsqldb`.
  - Si la connexion réussi, un [DocumentHandler][38] est ajouté en tant que [com.sun.star.util.XCloseListener][39] et [com.sun.star.document.XStorageChangeListener][40] au fichier odb.
  - Si la connexion échoue et que les fichiers ont été extraits lors de la phase 1, le **sous-répertoire** est supprimé.
- Lors de la fermeture ou du changement de nom (Enregistrer sous) du fichier odb, si la connexion a réussi, le [DocumentHandler][38] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (zip), puis supprime le **sous-répertoire**.

Le but principal de ce mode de fonctionnement est de profiter des caractéristiques ACID de la base de données sous-jacente en cas de fermeture anormale de LibreOffice.
En contre partie, la fonction: **fichier -> Sauvegarder** n'a **aucun effet sur la base de données sous jacente**. Seul la fermeture du fichier odb ou son enregistrement sous un nom different (Fichier -> Enregistrer sous) effectura la sauvegarde de la base de donnée dans le fichier odb.

___

## Comment créer l'extension:

Normalement, l'extension est créée avec Eclipse pour Java et [LOEclipse][41]. Pour contourner Eclipse, j'ai modifié LOEclipse afin de permettre la création de l'extension avec Apache Ant.  
Pour créer l'extension HyperSQLOOo avec l'aide d'Apache Ant, vous devez:
- Installer le [SDK Java][42] version 8 ou supérieure.
- Installer [Apache Ant][43] version 1.10.0 ou supérieure.
- Installer [LibreOffice et son SDK][44] version 7.x ou supérieure.
- Cloner le dépôt [HyperSQLOOo][45] sur GitHub dans un dossier.
- Depuis ce dossier, accédez au répertoire: `source/HyperSQLOOo/`
- Dans ce répertoire, modifiez le fichier `build.properties` afin que les propriétés `office.install.dir` et `sdk.dir` pointent vers les dossiers d'installation de LibreOffice et de son SDK, respectivement.
- Lancez la création de l'archive avec la commande: `ant`
- Vous trouverez l'archive générée dans le sous-dossier: `dist/`

___

## A été testé avec:

* LibreOffice 24.2.1.2 (x86_64)- Windows 10

* LibreOffice 7.3.7.2 - Lubuntu 22.04

* LibreOffice 24.2.1.2 - Lubuntu 22.04

* LibreOffice 24.8.0.3 (X86_64) - Windows 10(x64) - Python version 3.9.19 (sous Lubuntu 22.04 / VirtualBox 6.1.38)

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][16]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 0.0.1:

- La rédaction de ce pilote a été facilitée par une [discussion avec Villeroy][46], sur le forum OpenOffice, que je tiens à remercier, car la connaissance ne vaut que si elle est partagée...

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

- Modification de [Driver.py][47] afin de rendre possible l'utilisation du service Uno: `com.sun.star.sdb.RowSet`.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 0.0.5:

- Ecriture d'un [DocumentHandler][38] responsable:
    - De l'extraction des fichiers de base de données contenus dans le fichier **odb** à la connexion.
    - De la sauvegarde des fichiers de base de données dans le fichier **odb** lors de sa fermeture.

- Réécriture de [Driver.py][47] afin de permettre:
    - Son fonctionnement avec le nouveau pilote JDBC fourni par l'extension [jdbcDriverOOo][10] version 0.0.4.
    - La prise en charge du nouveau [DocumentHandler][38] afin de rendre les fichiers **odb** portables tels qu'ils étaient dans LibreOffice / OpenOffice avec la version 1.8 de HsqlDB.

- Beaucoup d'autres correctifs...

### Ce qui a été fait pour la version 1.0.0:

- Renommage de l'extension de HsqlDBembeddedOOo en HsqlDriverOOo.

- Integration de HyperSQL version 2.7.2.

### Ce qui a été fait pour la version 1.0.1:

- Renommage de l'extension de HsqlDriverOOo en HyperSQLOOo.

- Résolution du [dysfonctionnement 156511][48] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][49] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **HyperSQLOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Ce qui a été fait pour la version 1.1.0:

- Tous les paquets Python nécessaires à l'extension sont désormais enregistrés dans un fichier [requirements.txt][50] suivant la [PEP 508][51].
- Désormais si vous n'êtes pas sous Windows alors les paquets Python nécessaires à l'extension peuvent être facilement installés avec la commande:  
  `pip install requirements.txt`
- Modification de la section [Prérequis][52].

### Ce qui a été fait pour la version 1.1.1:

- Prise en charge des [nouvelles fonctionnalités][53] de **jdbcDriverOOo 1.1.2**.

### Ce qui a été fait pour la version 1.1.2:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.3.1**.
- Lors de l'enregistrement sous un nom différent, la base de données si ouverte sera fermée correctement.
- Lors de l'ouverture d'un fichier odb, si la connexion échoue, pour éviter la destruction des données, la recompression des fichiers de la base de données n'aura pas lieu. Merci à Robert d'avoir su détecter ce [dysfonctionnement][54].

### Ce qui a été fait pour la version 1.1.3:

- Utilisation du nouveau format de données implémenté dans la version 1.1.2. Par conséquent, si vous devez ouvrir des fichiers odb créés avec une version inférieure à 1.1.2, vous devez d'abord les ouvrir avec la version 1.1.2, sinon une erreur sera générée.

### Ce qui a été fait pour la version 1.1.4:

- Mise à jour du paquet [Python packaging][55] vers la version 24.1.
- Mise à jour du paquet [Python setuptools][56] vers la version 72.1.0.
- L'extension vous demandera d'installer l'extensions jdbcDriverOOo en version 1.4.2 minimum.

### Ce qui a été fait pour la version 1.1.5:

- Correction du [problème n°2][57] qui semble être une régression liée à la sortie de JaybirdOOo. Merci à TeddyBoomer de l'avoir signalé.
- Mise à jour du paquet [Python setuptools][56] vers la version 73.0.1.
- Les options de l'extension sont désormais accessibles via: **Outils -> Options -> LibreOffice Base -> Pilote HsqlDB intégré**

### Ce qui a été fait pour la version 1.1.6:

- La journalisation accessible dans les options de l’extension s’affiche désormais correctement sous Windows.
- Les modifications apportées aux options de l'extension, qui nécessitent un redémarrage de LibreOffice, entraîneront l'affichage d'un message.
- Support de LibreOffice version 24.8.x.

### Ce qui a été fait pour la version 1.1.7:

- Nécessite la dernière version de **jdbcDriverOOo 1.4.4**.
- Dans les options de l'extension il est possible de définir les options: **Afficher les tables système**, **Utiliser les signets** et **Forcer le mode SQL** qui seront spécifiques à ce pilote.

### Ce qui a été fait pour la version 1.1.8:

- L'extension vous demandera d'installer l'extensions jdbcDriverOOo en version 1.4.6 minimum.
- Modification des options de l'extension accessibles via : **Outils -> Options -> LibreOffice Base -> Pilote HsqlDB intégré** afin de respecter la nouvelle charte graphique.

### Ce qui a été fait pour la version 1.2.0:

- Mise à jour du paquet [Python packaging][55] vers la version 25.0.
- Mise à jour du paquet [Python setuptools][56] vers la version 75.3.2.
- Déploiement de l'enregistrement passif permettant une installation beaucoup plus rapide des extensions et de différencier les services UNO enregistrés de ceux fournis par une implémentation Java ou Python. Cet enregistrement passif est assuré par l'extension [LOEclipse][41] via les [PR#152][58] et [PR#157][59].
- Modification de [LOEclipse][41] pour prendre en charge le nouveau format de fichier `rdb` produit par l'utilitaire de compilation `unoidl-write`. Les fichiers `idl` ont été mis à jour pour prendre en charge les deux outils de compilation disponibles: idlc et unoidl-write.
- Il est désormais possible de créer le fichier oxt de l'extension HyperSQLOOo uniquement avec Apache Ant et une copie du dépôt GitHub. La section [Comment créer l'extension][60] a été ajoutée à la documentation.
- Toute erreur survenant lors du chargement du pilote sera consignée dans le journal de l'extension si la journalisation a été préalablement activé. Cela facilite l'identification des problèmes d'installation sous Windows.
- Nécessite l'extension **jdbcDriverOOo en version 1.5.0 minimum**.

### Que reste-t-il à faire pour la version 1.2.0:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: </img/hypersql.svg#collapse>
[2]: <https://prrvchr.github.io/HyperSQLOOo/>
[3]: <https://prrvchr.github.io/HyperSQLOOo/>
[4]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_fr>
[5]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-120>
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
[20]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#pr%C3%A9requis>
[21]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[22]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[23]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[24]: <img/HyperSQLOOo.svg#middle>
[25]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[26]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.2.0#right>
[27]: <img/HyperSQLOOo-1_fr.png>
[28]: <img/HyperSQLOOo-2_fr.png>
[29]: <img/HyperSQLOOo-3_fr.png>
[30]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#comment-cr%C3%A9er-une-nouvelle-base-de-donn%C3%A9es>
[31]: <https://hsqldb.org/doc/guide/databaseobjects-chapt.html#dbc_schemas_schema_objects>
[32]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[33]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[34]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[35]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.7.2/hsqldb-2.7.2.jar>
[36]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[37]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[38]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/documenthandler.py>
[39]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[40]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[41]: <https://github.com/LibreOffice/loeclipse>
[42]: <https://adoptium.net/temurin/releases/?version=8&package=jdk>
[43]: <https://ant.apache.org/manual/install.html>
[44]: <https://downloadarchive.documentfoundation.org/libreoffice/old/7.6.7.2/>
[45]: <https://github.com/prrvchr/HyperSQLOOo.git>
[46]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[47]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/driver.py>
[48]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[49]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[50]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/requirements.txt>
[51]: <https://peps.python.org/pep-0508/>
[52]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#pr%C3%A9requis>
[53]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-112>
[54]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471#c54>
[55]: <https://pypi.org/project/packaging/>
[56]: <https://pypi.org/project/setuptools/>
[57]: <https://github.com/prrvchr/HyperSQLOOo/issues/2>
[58]: <https://github.com/LibreOffice/loeclipse/pull/152>
[59]: <https://github.com/LibreOffice/loeclipse/pull/157>
[60]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#comment-cr%C3%A9er-lextension>
