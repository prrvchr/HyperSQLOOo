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

# version [1.1.4][5]

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

**Attention: If you wish to migrate odb files created with LibreOffice or OpenOffice and HsqlDB version 1.8, it is imperative to use version 1.1.2 or higher of HyperSQLOOo otherwise there is a great risk of data loss. The migration procedure is given in the [How to migrate an embedded database][14] section. Whatever happens, keep your backups up to date.**

Being free software I encourage you:
- To duplicate its [source code][15].
- To make changes, corrections, improvements.
- To open [issue][16] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

The HyperSQLOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][17].

This extension cannot be installed together with the [SQLiteOOo][18] extension.  
It's one or the other, but at the moment they can't work together (see [issue #156471][19]).

**On Linux and macOS the Python packages** used by the extension, if already installed, may come from the system and therefore **may not be up to date**.  
To ensure that your Python packages are up to date it is recommended to use the **System Info** option in the extension Options accessible by:  
**Tools -> Options -> Base drivers -> Embedded HsqlDB Driver -> View log -> System Info**  
If outdated packages appear, you can update them with the command:  
`pip install --upgrade <package-name>`

For more information see: [What has been done for version 1.1.0][20].

___

## Installation:

It seems important that the file was not renamed when it was downloaded.  
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][21]][10] Install **[jdbcDriverOOo.oxt][22]** extension [![Version][23]][22]

  This extension is necessary to use HsqlDB version 2.7.2 with all its features.

- ![HyperSQLOOo logo][24] Install **[HyperSQLOOo.oxt][25]** extension [![Version][26]][25]

Restart LibreOffice after installation.  
**Be careful, restarting LibreOffice may not be enough.**
- **On Windows** to ensure that LibreOffice restarts correctly, use Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice shuts down (and kill it if so).
- **Under Linux or macOS** you can also ensure that LibreOffice restarts correctly, by launching it from a terminal with the command `soffice` and using the key combination `Ctrl + C` if after stopping LibreOffice, the terminal is not active (no command prompt).

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HyperSQLOOo screenshot 1][27]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HyperSQLOOo screenshot 2][28]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HyperSQLOOo screenshot 3][29]

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to a newer version (for example 2.7.2), follow these steps:
1. Make a copy (backup) of your database (odb file).
2. If not already installed, install this extension and the [jdbcDriverOOo][10] extension.
3. Update driver archive of the HsqlDB driver in: **Tools -> Options -> Base drivers -> JDBC driver -> JDBC drivers settings -> Driver archive -> Update**, with a version [1.8.0.10][11].
4. Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
5. Open the odb file in Base (double click on the odb file).
6. In Base go to: **Tools -> SQL** and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.

- Repeat this procedure at step 3 using version [2.4.0][30] or [2.4.1][31] or [2.5.0][32].
- Repeat this procedure at step 3 using version [2.7.2][33].

___

## How does it work:

HyperSQLOOo is an [com.sun.star.sdbc.Driver][34] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][10] extension allowing to store the HsqlDB database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, several things are done:
  - If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all HsqlDB files are extracted from the **database** directory of the odb file (unzip).
  - The [jdbcDriverOOo][10] extension is used to get the [com.sun.star.sdbc.XConnection][35] interface from the **subdirectory** path + `/hsqldb`.
  - If the connection is successful, a [DocumentHandler][36] is added as an [com.sun.star.util.XCloseListener][37] and [com.sun.star.document.XStorageChangeListener][38] to the odb file.
  - If the connection is unsuccessful and the files was extracted in phase 1, the **subdirectory** will be deleted.
- When closing or renaming (Save As) the odb file, if the connection was successful, the [DocumentHandler][36] copies all files present in the **subdirectory** into the (new) **database** directory of the odb file (zip), then delete the **subdirectory**.

The main purpose of this mode of operation is to take advantage of the ACID characteristics of the underlying database in the event of an abnormal closure of LibreOffice.
On the other hand, the function: **file -> Save** has **no effect on the underlying database**. Only closing the odb file or saving it under a different name (File -> Save As) will save the database in the odb file.

___

## Has been tested with:

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

* LibreOffice 24.2.1.2 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][16]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy][39], on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

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

- Modification of [Driver.py][40] in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

- Many other fix...

### What has been done for version 0.0.5:

- Writing a [DocumentHandler][36] to allow:
    - The extraction of the database files contained in the **odb** file on connection.
    - Saving database files to **odb** file when closing it.

- Rewrote [Driver.py][40] to allow:
    - Its operation with the new JDBC driver provided by the extension [jdbcDriverOOo][10] version 0.0.4.
    - The support for the new [DocumentHandler][36] to make **odb** files portable as they were in LibreOffice / OpenOffice with version 1.8 of HsqlDB.

- Many other fix...

### What has been done for version 1.0.0:

- Renamed the extension from HsqlDBembeddedOOo to HsqlDriverOOo.

- Integration of HyperSQL version 2.7.2.

### What has been done for version 1.0.1:

- Renamed the extension from HsqlDriverOOo to HyperSQLOOo.

- Fixed [bug 156511][41] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][42] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **HyperSQLOOo** now displays an error message.

- Many other things...

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][43] file following [PEP 508][44].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][45] section.

### What has been done for version 1.1.1:

- Support for [new features][46] in **jdbcDriverOOo 1.1.2**.

### What has been done for version 1.1.2:

- Support for the latest version of **jdbcDriverOOo 1.3.1**.
- When saving under a different name, the database if open will be closed correctly.
- When opening an odb file, if the connection fails, to avoid data destruction, recompression of the database files will not take place. Thanks to Robert for being able to detect this [issue][47].

### What has been done for version 1.1.3:

- Use of the new data format implemented in version 1.1.2. As a result, if you need to open odb files created with a version lower than 1.1.2 you must first open them with version 1.1.2, otherwise an error will be thrown.

### What has been done for version 1.1.4:

- Updated the [Python packaging][48] package to version 24.1.
- Updated the [Python setuptools][49] package to version 72.1.0 in order to respond to the [Dependabot security alert][50].
- The extension will ask you to install the jdbcDriverOOo extension in versions 1.4.2 minimum.

### What remains to be done for version 1.1.4:

- Add new language for internationalization...

- Anything welcome...

[1]: </img/hypersql.svg#collapse>
[2]: <https://prrvchr.github.io/HyperSQLOOo/>
[3]: <https://prrvchr.github.io/HyperSQLOOo/README_fr>
[4]: <https://prrvchr.github.io/HyperSQLOOo/source/HyperSQLOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/HyperSQLOOo#what-has-been-done-for-version-114>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[10]: <https://prrvchr.github.io/jdbcDriverOOo/>
[11]: <https://repo1.maven.org/maven2/org/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.jar>
[12]: <https://en.wikipedia.org/wiki/ACID>
[13]: <http://hsqldb.org/>
[14]: <https://prrvchr.github.io/HyperSQLOOo/#how-to-migrate-an-embedded-database>
[15]: <https://github.com/prrvchr/HyperSQLOOo/>
[16]: <https://github.com/prrvchr/HyperSQLOOo/issues/new>
[17]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[18]: <https://prrvchr.github.io/SQLiteOOo/#requirement>
[19]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[20]: <https://prrvchr.github.io/HyperSQLOOo/#what-has-been-done-for-version-110>
[21]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[22]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[23]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[24]: <img/HyperSQLOOo.svg#middle>
[25]: <https://github.com/prrvchr/HyperSQLOOo/releases/latest/download/HyperSQLOOo.oxt>
[26]: <https://img.shields.io/github/downloads/prrvchr/HyperSQLOOo/latest/total?label=v1.1.4#right>
[27]: <img/HyperSQLOOo-1.png>
[28]: <img/HyperSQLOOo-2.png>
[29]: <img/HyperSQLOOo-3.png>
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
[45]: <https://prrvchr.github.io/HyperSQLOOo/#requirement>
[46]: <https://prrvchr.github.io/jdbcDriverOOo/#what-has-been-done-for-version-112>
[47]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471#c54>
[48]: <https://pypi.org/project/packaging/>
[49]: <https://pypi.org/project/setuptools/>
[50]: <https://github.com/prrvchr/HyperSQLOOo/security/dependabot/1>
