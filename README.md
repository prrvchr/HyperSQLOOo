# ![HsqlDBembeddedOOo logo][1] HsqlDBembeddedOOo

**Ce [document][2] en français.**

**The use of this software subjects you to our** [**Terms Of Use**][3]

# version [0.0.5][4]

## Introduction:

**HsqlDBembeddedOOo** is part of a [Suite][5] of [LibreOffice][6] and/or [OpenOffice][7] extensions allowing to offer you innovative services in these office suites.  

This extension allows you:
- To overcome [bug 139538][8] for users of **LibreOffice on Linux**.
- To use Embedded HsqlDB in uncompressed (split) mode, which is more robust, with the version of the HsqlDB driver of your choice.
- To migrate data from an embedded database (odb file) to the full feature HsqlDB driver: [jdbcDriverOOo][9], see: [How to migrate an embedded database][10].

HsqlDBembeddedOOo only works in split mode, with the ability to extract (decompress) the data contained in an odb file when connecting if a folder with the same name and location as the odb file does not exist. This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice driver (Embedded HsqlDB).  
If these features do not concern you, then I recommend you to use the driver [jdbcDriverOOo][9] allowing to exploit all the functionalities offered by HsqlDB.

Being free software I encourage you:
- To duplicate its [source code][11].
- To make changes, corrections, improvements.
- To open [issue][12] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

## Requirement:

[HsqlDB][13] is a database written in Java.  
Its use requires the [installation and configuration][14] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][15] as your Java installation source.

If you are using **LibreOffice on Linux**, then you are subject to [bug 139538][8].  
To work around the problem, please uninstall the packages:
- libreoffice-sdbc-hsqldb
- libhsqldb1.8.0-java

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![jdbcDriverOOo logo][16] **[jdbcDriverOOo.oxt][17]** extension version 0.0.4.  
This extension is necessary to use HsqlDB version 2.5.1 with all its features.

- Install ![HsqlDBembeddedOOo logo][18] **[HsqlDBembeddedOOo.oxt][19]** extension version 0.0.5.

Restart LibreOffice / OpenOffice after installation.

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HsqlDBembeddedOOo screenshot 1][20]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HsqlDBembeddedOOo screenshot 2][21]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HsqlDBembeddedOOo screenshot 3][22]

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to the latest version (for example 2.5.1), follow these steps:
- 1 - If it is not already installed, install this extension.
- 2 - Make a copy (backup) of your database (odb file).
- 3 - Open the odb file in Base (double click on the odb file).
- 4 - In Base go to: Tools -> SQL and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.
- 5 - Change the version of the HsqlDB driver in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver, with a version [2.4.0][23] or [2.4.1][24] or [2.5.0][25] (You must rename the jar file to hsqldb.jar for it to be taken into account).
- 6 - Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
- Repeat this procedure at step 3 using version [2.5.1][26].
- To finish, repeat step 3 then 4.

Now you can use the full feature version of the driver [jdbcDriverOOo][9], your database is in a folder with the same name and location as your odb file.

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

I encourage you in case of problem :-(  
to create an [issue][12]  
I will try to solve it ;-)

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy][27], on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

- Using the old version of HsqlDB 1.8.0 (can be easily updated).

- Added a dialog box allowing to update the driver (hsqldb.jar) in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver

- Many other fix...

### What has been done for version 0.0.2:

- Now the driver automatically splits an odb when opened... This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice HsqlDB driver ;-)

- Many other fix...

### What has been done for version 0.0.3:

- I especially want to thank fredt at [hsqldb.org][13] for:

    - His welcome for this project and his permission to use the HsqlDB logo in the extension.

    - The quality of its HsqlDB database.

- Now works with OpenOffice on Windows.

- When unzipping, a file name clash now displays a precise error.

- Now correctly handles spaces in filenames and paths.

- Many other fix...

### What has been done for version 0.0.4:

- Modification of [Driver.py][28] in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

### What has been done for version 0.0.5:

- Rewrote [Driver.py][28] to allow:
  - Its operation with the new JDBC driver provided by the extension [jdbcDriverOOo][9] version 0.0.4.
  - The extraction of the database files contained in the **odb** file on connection.
  - Saving database files to **odb** file when closing it.
  - To make **odb** files portable as they were with version 1.8 of HsqlDB.

- Many other fix...

### What remains to be done for version 0.0.5:

- Add new language for internationalization...

- Anything welcome...

[1]: <img/HsqlDBembeddedOOo.png>
[2]: <https://prrvchr.github.io/HsqlDBembeddedOOo/README_fr>
[3]: <https://prrvchr.github.io/HsqlDBembeddedOOo/source/HsqlDBembeddedOOo/registration/TermsOfUse_en>
[4]: <https://prrvchr.github.io/HsqlDBembeddedOOo#historical>
[5]: <https://prrvchr.github.io/>
[6]: <https://www.libreoffice.org/download/download/>
[7]: <https://www.openoffice.org/download/index.html>
[8]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[9]: <https://prrvchr.github.io/jdbcDriverOOo/>
[10]: <https://prrvchr.github.io/HsqlDBembeddedOOo/#how-to-migrate-an-embedded-database>
[11]: <https://github.com/prrvchr/HsqlDBembeddedOOo/>
[12]: <https://github.com/prrvchr/HsqlDBembeddedOOo/issues/new>
[13]: <http://hsqldb.org/>
[14]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[15]: <https://adoptium.net/releases.html?variant=openjdk11>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.png>
[17]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/jdbcDriverOOo.oxt>
[18]: <img/HsqlDBembeddedOOo.png>
[19]: <https://github.com/prrvchr/HsqlDBembeddedOOo/raw/master/HsqlDBembeddedOOo.oxt>
[20]: <img/HsqlDBembeddedOOo-1.png>
[21]: <img/HsqlDBembeddedOOo-2.png>
[22]: <img/HsqlDBembeddedOOo-3.png>
[23]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[24]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[25]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[26]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.1/hsqldb-2.5.1.jar>
[27]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[28]: <https://github.com/prrvchr/HsqlDBembeddedOOo/blob/master/source/HsqlDBembeddedOOo/service/Driver.py>
