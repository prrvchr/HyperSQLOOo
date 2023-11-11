# Documentation

**Ce [document][1] en français.**

**The use of this software subjects you to our [Terms Of Use][2].**

# version [1.0.2][3]

## Introduction:

**HyperSQLOOo** is part of a [Suite][4] of [LibreOffice][5] and/or [OpenOffice][6] extensions allowing to offer you innovative services in these office suites.  

This extension allows you:
- To overcome [bug 139538][7] for users of **LibreOffice on Linux**.
- To use HyperSQL database in embedded mode, making the database portable (a single odb file).
- To take advantage of the improvements offered by the [jdbcDriverOOo][8] extension:
    - The management of users and roles (groups).
    - The management of nanoseconds and time zones.
    - The management of `java.sql.Array`, `java.sql.Blob`, `java.sql.Clob`...
- To replace the integrated [HsqlDB 1.8][9] driver provided by LibreOffice / OpenOffice, a version that will soon be more than 20 years old, with a recent HsqlDB version of your choice.

Being free software I encourage you:
- To duplicate its [source code][10].
- To make changes, corrections, improvements.
- To open [issue][11] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

[HsqlDB][12] is a database written in Java.  
Its use requires the [installation and configuration][13] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][14] as your Java installation source.

If you are using **LibreOffice on Linux**, then you are subject to [bug 139538][7]. To work around the problem, please **uninstall the packages** with commands:
- `sudo apt remove libreoffice-sdbc-hsqldb` (to uninstall the libreoffice-sdbc-hsqldb package)
- `sudo apt remove libhsqldb1.8.0-java` (to uninstall the libhsqldb1.8.0-java package)

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

___

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][15]][8] Install **[jdbcDriverOOo.oxt][16]** extension [![Version][17]][16]

    This extension is necessary to use HsqlDB version 2.7.2 with all its features.

- ![HyperSQLOOo logo][18] Install **[HyperSQLOOo.oxt][19]** extension [![Version][20]][19]

Restart LibreOffice / OpenOffice after installation.

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HyperSQLOOo screenshot 1][21]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HyperSQLOOo screenshot 2][22]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HyperSQLOOo screenshot 3][23]

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to a newer version (for example 2.7.2), follow these steps:
1. Make a copy (backup) of your database (odb file).
2. If not already installed, install this extension and the [jdbcDriverOOo][8] extension.
3. Update driver archive of the HsqlDB driver in: **Tools -> Options -> Base drivers -> JDBC driver -> JDBC drivers settings -> Driver archive -> Update**, with a version [1.8.0.10][9].
4. Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
5. Open the odb file in Base (double click on the odb file).
6. In Base go to: **Tools -> SQL** and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.

- Repeat this procedure at step 3 using version [2.4.0][24] or [2.4.1][25] or [2.5.0][26].
- Repeat this procedure at step 3 using version [2.7.2][27].

___

## How does it work:

HyperSQLOOo is an [com.sun.star.sdbc.Driver][28] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][8] extension allowing to store the HyperSQL database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, three things are done:
    1. If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all HyperSQL files are extracted from the **database** directory of the odb file (unzip).
    2. A [DocumentHandler][29] is added as an [com.sun.star.util.XCloseListener][30] and [com.sun.star.document.XStorageChangeListener][31] to the odb file.
    3. The [jdbcDriverOOo][8] extension is used to get the [com.sun.star.sdbc.XConnection][32] interface from the **subdirectory** path + `odb_file_name`.

- When closing or renaming (Save as) an odb file the [DocumentHandler][29] copy all the files present in the **subdirectory** into the (new) **database** directory of the odb file (zip) and then delete the **subdirectory**.

___

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][11]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy][33], on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

- Using the old version of HsqlDB 1.8.0 (can be easily updated).

- Added a dialog box allowing to update the driver (hsqldb.jar) in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver

- Many other fix...

### What has been done for version 0.0.2:

- Now the driver automatically splits an odb when opened... This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice HsqlDB driver :wink:

- Many other fix...

### What has been done for version 0.0.3:

- I especially want to thank fredt at [hsqldb.org][12] for:

    - His welcome for this project and his permission to use the HsqlDB logo in the extension.

    - The quality of its HsqlDB database.

- Now works with OpenOffice on Windows.

- When unzipping, a file name clash now displays a precise error.

- Now correctly handles spaces in filenames and paths.

- Many other fix...

### What has been done for version 0.0.4:

- Modification of [Driver.py][34] in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

- Many other fix...

### What has been done for version 0.0.5:

- Writing a [DocumentHandler][29] to allow:
    - The extraction of the database files contained in the **odb** file on connection.
    - Saving database files to **odb** file when closing it.

- Rewrote [Driver.py][34] to allow:
    - Its operation with the new JDBC driver provided by the extension [jdbcDriverOOo][8] version 0.0.4.
    - The support for the new [DocumentHandler][29] to make **odb** files portable as they were in LibreOffice / OpenOffice with version 1.8 of HsqlDB.

- Many other fix...

### What has been done for version 1.0.0:

- Renamed the extension from HsqlDBembeddedOOo to HsqlDriverOOo.

- Integration of HyperSQL version 2.7.2.

### What has been done for version 1.0.1:

- Renamed the extension from HsqlDriverOOo to HyperSQLOOo.

- Fixed [bug 156511][35] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][36] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **HyperSQLOOo** now displays an error message.

- Many other things...

### What remains to be done for version 1.0.2:

- Add new language for internationalization...

- Anything welcome...

[1]: <https://prrvchr.github.io/HyperSQLOOo/README_fr>
[2]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_en>
[3]: <https://prrvchr.github.io/HyperSQLOOo#historical>
[4]: <https://prrvchr.github.io/>
[5]: <https://www.libreoffice.org/download/download/>
[6]: <https://www.openoffice.org/download/index.html>
[7]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[8]: <https://prrvchr.github.io/jdbcDriverOOo/>
[9]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[10]: <https://github.com/prrvchr/HyperSQLOOo/>
[11]: <https://github.com/prrvchr/HyperSQLOOo/issues/new>
[12]: <http://hsqldb.org/>
[13]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[14]: <https://adoptium.net/releases.html?variant=openjdk11>
[15]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[16]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[17]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[18]: <img/HyperSQLOOo.svg#middle>
[19]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[20]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.0.2#right>
[21]: <img/HyperSQLOOo-1.png>
[22]: <img/HyperSQLOOo-2.png>
[23]: <img/HyperSQLOOo-3.png>
[24]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[25]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[26]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[27]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.7.2/hsqldb-2.7.2.jar>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[29]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/documenthandler.py>
[30]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[31]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[32]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[33]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[34]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/driver.py>
[35]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[36]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
