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

**Ce [document][3] en français.**

**The use of this software subjects you to our [Terms Of Use][4].**

# version [1.1.0][5]

## Introduction:

**HyperSQLOOo** is part of a [Suite][6] of [LibreOffice][7] ~~and/or [OpenOffice][8]~~ extensions allowing to offer you innovative services in these office suites.  

This extension allows you:
- To overcome [bug 139538][9] for users of **LibreOffice on Linux**.
- To use HyperSQL database in embedded mode, making the database portable (a single odb file).
- To take advantage of the improvements offered by the [jdbcDriverOOo][10] extension:
    - The management of users and roles (groups).
    - The management of nanoseconds and time zones.
    - The management of `java.sql.Array`, `java.sql.Blob`, `java.sql.Clob`...
- To replace the integrated [HsqlDB 1.8][11] driver provided by LibreOffice / OpenOffice, a version that will soon be more than 20 years old, with a recent HsqlDB version of your choice.
- **To support the [ACID][12] properties of the underlying [HsqlDB][13] database.**

Being free software I encourage you:
- To duplicate its [source code][14].
- To make changes, corrections, improvements.
- To open [issue][15] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

The HyperSQLOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][16].

This extension cannot be installed together with the [SQLiteOOo][17] extension.  
It's one or the other, but at the moment they can't work together (see [issue #156471][40]).

**On Linux and macOS the Python packages** used by the extension, if already installed, may come from the system and therefore **may not be up to date**.  
To ensure that your Python packages are up to date it is recommended to use the **System Info** option in the extension Options accessible by:  
**Tools -> Options -> Base drivers -> Embedded HsqlDB Driver -> View log -> System Info**  
If outdated packages appear, you can update them with the command:  
`pip install --upgrade <package-name>`

For more information see: [What has been done for version 1.1.0][41].

___

## Installation:

It seems important that the file was not renamed when it was downloaded.  
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][18]][10] Install **[jdbcDriverOOo.oxt][19]** extension [![Version][20]][19]

  This extension is necessary to use HsqlDB version 2.7.2 with all its features.

- ![HyperSQLOOo logo][21] Install **[HyperSQLOOo.oxt][22]** extension [![Version][23]][22]

Restart LibreOffice after installation.  
**Be careful, restarting LibreOffice may not be enough.**
- **On Windows** to ensure that LibreOffice restarts correctly, use Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice shuts down (and kill it if so).
- **Under Linux or macOS** you can also ensure that LibreOffice restarts correctly, by launching it from a terminal with the command `soffice` and using the key combination `Ctrl + C` if after stopping LibreOffice, the terminal is not active (no command prompt).

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HyperSQLOOo screenshot 1][24]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HyperSQLOOo screenshot 2][25]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HyperSQLOOo screenshot 3][26]

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to a newer version (for example 2.7.2), follow these steps:
1. Make a copy (backup) of your database (odb file).
2. If not already installed, install this extension and the [jdbcDriverOOo][10] extension.
3. Update driver archive of the HsqlDB driver in: **Tools -> Options -> Base drivers -> JDBC driver -> JDBC drivers settings -> Driver archive -> Update**, with a version [1.8.0.10][9].
4. Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
5. Open the odb file in Base (double click on the odb file).
6. In Base go to: **Tools -> SQL** and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.

- Repeat this procedure at step 3 using version [2.4.0][27] or [2.4.1][28] or [2.5.0][29].
- Repeat this procedure at step 3 using version [2.7.2][30].

___

## How does it work:

HyperSQLOOo is an [com.sun.star.sdbc.Driver][31] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][10] extension allowing to store the HyperSQL database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, three things are done:
    1. If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all HyperSQL files are extracted from the **database** directory of the odb file (unzip).
    2. A [DocumentHandler][32] is added as an [com.sun.star.util.XCloseListener][33] and [com.sun.star.document.XStorageChangeListener][34] to the odb file.
    3. The [jdbcDriverOOo][10] extension is used to get the [com.sun.star.sdbc.XConnection][35] interface from the **subdirectory** path + `odb_file_name`.

- When closing or renaming (Save as) an odb file the [DocumentHandler][32] copy all the files present in the **subdirectory** into the (new) **database** directory of the odb file (zip) and then delete the **subdirectory**.

___

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][12]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy][36], on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

- Using the old version of HsqlDB 1.8.0 (can be easily updated).

- Added a dialog box allowing to update the driver (hsqldb.jar) in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver

- Many other fix...

### What has been done for version 0.0.2:

- Now the driver automatically splits an odb when opened... This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice HsqlDB driver :wink:

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

- Modification of [Driver.py][37] in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

- Many other fix...

### What has been done for version 0.0.5:

- Writing a [DocumentHandler][32] to allow:
    - The extraction of the database files contained in the **odb** file on connection.
    - Saving database files to **odb** file when closing it.

- Rewrote [Driver.py][37] to allow:
    - Its operation with the new JDBC driver provided by the extension [jdbcDriverOOo][10] version 0.0.4.
    - The support for the new [DocumentHandler][32] to make **odb** files portable as they were in LibreOffice / OpenOffice with version 1.8 of HsqlDB.

- Many other fix...

### What has been done for version 1.0.0:

- Renamed the extension from HsqlDBembeddedOOo to HsqlDriverOOo.

- Integration of HyperSQL version 2.7.2.

### What has been done for version 1.0.1:

- Renamed the extension from HsqlDriverOOo to HyperSQLOOo.

- Fixed [bug 156511][38] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][39] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **HyperSQLOOo** now displays an error message.

- Many other things...

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][42] file following [PEP 508][43].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][44] section.

### What remains to be done for version 1.1.0:

- Add new language for internationalization...

- Anything welcome...

[1]: </img/hypersql.svg#collapse>
[2]: <https://prrvchr.github.io/HyperSQLOOo/>
[3]: <https://prrvchr.github.io/HyperSQLOOo/README_fr>
[4]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/HyperSQLOOo#what-has-been-done-for-version-100>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[10]: <https://prrvchr.github.io/jdbcDriverOOo/>
[11]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[12]: <https://en.wikipedia.org/wiki/ACID>
[13]: <http://hsqldb.org/>
[14]: <https://github.com/prrvchr/HyperSQLOOo/>
[15]: <https://github.com/prrvchr/HyperSQLOOo/issues/new>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[17]: <https://prrvchr.github.io/SQLiteOOo/#requirement>
[18]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[19]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[20]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[21]: <img/HyperSQLOOo.svg#middle>
[22]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[23]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.1.0#right>
[24]: <img/HyperSQLOOo-1.png>
[25]: <img/HyperSQLOOo-2.png>
[26]: <img/HyperSQLOOo-3.png>
[27]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar>
[28]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar>
[29]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar>
[30]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.7.2/hsqldb-2.7.2.jar>
[31]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[32]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/documenthandler.py>
[33]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[34]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[35]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[36]: <https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912>
[37]: <https://github.com/prrvchr/HyperSQLOOo/blob/master/uno/lib/uno/embedded/driver.py>
[38]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[39]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[40]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[41]: <https://prrvchr.github.io/HyperSQLOOo/#what-has-been-done-for-version-110>
[42]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/requirements.txt>
[43]: <https://peps.python.org/pep-0508/>
[44]: <https://prrvchr.github.io/HyperSQLOOo/#requirement>
