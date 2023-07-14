# Documentation

**Ce [document][2] en français.**

**The use of this software subjects you to our [Terms Of Use][3].**

# version [1.0.0][4]

## Introduction:

**HsqlDriverOOo** is part of a [Suite][5] of [LibreOffice][6] and/or [OpenOffice][7] extensions allowing to offer you innovative services in these office suites.  

This extension allows you:
- To overcome [bug 139538][8] for users of **LibreOffice on Linux**.
- To use HsqlDB in embedded mode, making the database portable (a single odb file), with the HsqlDB driver version of your choice.
- To take advantage of the improvements offered by the [jdbcDriverOOo][9] extension with the management of users and roles (groups).
- To replace the integrated [HsqlDB 1.8][10] driver provided by LibreOffice / OpenOffice, a version that will soon be more than 20 years old, with a recent HsqlDB version of your choice.

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

If you are using **LibreOffice on Linux**, then you are subject to [bug 139538][8]. To work around the problem, please **uninstall the packages** with commands:
- `sudo apt remove libreoffice-sdbc-hsqldb` (to uninstall the libreoffice-sdbc-hsqldb package)
- `sudo apt remove libhsqldb1.8.0-java` (to uninstall the libhsqldb1.8.0-java package)

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![jdbcDriverOOo logo][16] **[jdbcDriverOOo.oxt][17]** extension version 0.0.4.  
This extension is necessary to use HsqlDB version 2.5.1 with all its features.

- Install ![HsqlDriverOOo logo][1] **[HsqlDriverOOo.oxt][18]** extension version 1.0.0.

Restart LibreOffice / OpenOffice after installation.

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HsqlDriverOOo screenshot 1][19]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HsqlDriverOOo screenshot 2][20]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HsqlDriverOOo screenshot 3][21]

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to a newer version (for example 2.5.1), follow these steps:
- 1 - Make a copy (backup) of your database (odb file).
- 2 - If not already installed, install this extension and the [jdbcDriverOOo][9] extension.
- 3 - Update driver archive of the HsqlDB driver in: **Tools -> Options -> Base drivers -> JDBC driver -> JDBC drivers settings**, with a version [1.8.0.10][10].
- 4 - Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
- 5 - Open the odb file in Base (double click on the odb file).
- 6 - In Base go to: **Tools -> SQL** and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.
- 7 - Update driver archive of the HsqlDB driver in: **Tools -> Options -> Base drivers -> JDBC driver -> JDBC drivers settings**, with a version [2.4.0][22] or [2.4.1][23] or [2.5.0][24].
- 8 - Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
- Repeat this procedure at step 5 using version [2.5.1][25].
- To finish, repeat step 5 then 6.

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

- The writing of this driver was facilitated by a [discussion with Villeroy][26], on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

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

- Modification of [Driver.py][27] in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

- Many other fix...

### What has been done for version 0.0.5:

- Writing a [DocumentHandler][28] to allow:
  - The extraction of the database files contained in the **odb** file on connection.
  - Saving database files to **odb** file when closing it.

- Rewrote [Driver.py][27] to allow:
  - Its operation with the new JDBC driver provided by the extension [jdbcDriverOOo][9] version 0.0.4.
  - The support for the new [DocumentHandler][28] to make **odb** files portable as they were in LibreOffice / OpenOffce with version 1.8 of HsqlDB.

- Many other fix...

### What remains to be done for version 0.0.5:

- Add new language for internationalization...

- Anything welcome...

[1]: <img/HsqlDriverOOo.svg>
[2]: <https://prrvchr.github.io/HsqlDriverOOo/README_fr>
[3]: <https://prrvchr.github.io/HsqlDriverOOo/source/HsqlDriverOOo/registration/TermsOfUse_en>
[4]: <https://prrvchr.github.io/HsqlDriverOOo#historical>
[5]: <https://prrvchr.github.io/>
[6]: <https://www.libreoffice.org/download/download/>
[7]: <https://www.openoffice.org/download/index.html>
[8]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[9]: <https://prrvchr.github.io/jdbcDriverOOo/>
[10]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[11]: <https://github.com/prrvchr/HsqlDriverOOo/>
[12]: <https://github.com/prrvchr/HsqlDriverOOo/issues/new>
[13]: <http://hsqldb.org/>
[14]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[15]: <https://adoptium.net/releases.html?variant=openjdk11>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg>
[17]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/jdbcDriverOOo.oxt>
[18]: <https://github.com/prrvchr/HsqlDriverOOo/raw/master/HsqlDriverOOo.oxt>
[19]: <img/HsqlDriverOOo-1.png>
[20]: <img/HsqlDriverOOo-2.png>
[21]: <img/HsqlDriverOOo-3.png>
[22]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[23]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[24]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[25]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.1/hsqldb-2.5.1.jar>
[26]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[27]: <https://github.com/prrvchr/HsqlDriverOOo/blob/master/source/HsqlDriverOOo/service/Driver.py>
[28]: <https://github.com/prrvchr/HsqlDriverOOo/blob/master/uno/lib/uno/database/documenthandler.py>
