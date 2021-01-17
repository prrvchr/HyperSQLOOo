**Ce [document](https://prrvchr.github.io/HsqlDBembeddedOOo/README_fr) en français.**

**The use of this software subjects you to our** [**Terms Of Use**](https://prrvchr.github.io/HsqlDBembeddedOOo/HsqlDBembeddedOOo/registration/TermsOfUse_en)

# version [0.0.3](https://prrvchr.github.io/HsqlDBembeddedOOo#historical)

## Introduction:

**HsqlDBembeddedOOo** is part of a [Suite](https://prrvchr.github.io/) of [LibreOffice](https://www.libreoffice.org/download/download/) and/or [OpenOffice](https://www.openoffice.org/download/index.html) extensions allowing to offer you innovative services in these office suites.  
This extension allows you:
- To overcome [bug 139538](https://bugs.documentfoundation.org/show_bug.cgi?id=139538) for users of **LibreOffice on Linux**.
- To use Embedded HsqlDB in uncompressed (split) mode, which is more robust, with the version of the HsqlDB driver of your choice.
- To migrate data from an embedded database (odb file) to the full feature HsqlDB driver: [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/).

If these possibilities do not concern you, then I recommend you to use the driver [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/) allowing to exploit all the functionalities offered by HsqlDB.

Being free software I encourage you:
- To duplicate its [source code](https://github.com/prrvchr/HsqlDBembeddedOOo/).
- To make changes, corrections, improvements.
- To open [issue](https://github.com/prrvchr/HsqlDBembeddedOOo/issues/new) if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

## Requirement:

[HsqlDB](http://hsqldb.org/) is a database written in Java.  
The use of HsqlDB requires the installation and configuration within LibreOffice / OpenOffice of a **JRE version 1.8 minimum** (ie: Java version 8)  
I recommend [AdoptOpenJDK](https://adoptopenjdk.net/) as your Java installation source.

If you are using **LibreOffice on Linux**, then you are subject to [bug 139538](https://bugs.documentfoundation.org/show_bug.cgi?id=139538).  
To work around the problem, please uninstall the packages:
- libreoffice-sdbc-hsqldb
- libhsqldb1.8.0-java

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install [HsqlDBembeddedOOo.oxt](https://github.com/prrvchr/HsqlDBembeddedOOo/releases/download/v0.0.3/HsqlDBembeddedOOo.oxt) extension version 0.0.3.

Restart LibreOffice / OpenOffice after installation.

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HsqlDBembeddedOOo screenshot 1](HsqlDBembeddedOOo-1.png)

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HsqlDBembeddedOOo screenshot 2](HsqlDBembeddedOOo-2.png)

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HsqlDBembeddedOOo screenshot 3](HsqlDBembeddedOOo-3.png)

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.O) to the latest version (for example 2.5.1), follow these steps:
- 1 - Make a copy (backup) of your database (odb file).
- 2 - After installing this extension, open this odb file in Base (double click on the odb).
- 3 - In Base go to: Tools -> SQL and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`
- 4 - Change the version of the HsqlDB driver in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver by a version 2.4.x or 2.5.0
- 5 - Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
- Repeat this procedure at step 2 using version 2.5.1.

Now you can use the full feature version of the driver [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/), your database is in a folder with the same name and location as your odb file.

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

I encourage you in case of problem :-(  
to create an [issue](https://github.com/prrvchr/HsqlDBembeddedOOo/issues/new)  
I will try to solve it ;-)

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy](https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912), on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

- Using the old version of HsqlDB 1.8.0 (can be easily updated).

- Added a dialog box allowing to update the driver (hsqldb.jar) in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver

- Many other fix...

### What has been done for version 0.0.2:

- Now the driver automatically splits an odb when opened... This makes the driver backward compatible with the build-in LibreOffice HsqlDB Embedded Driver ;-)

- Many other fix...

### What has been done for version 0.0.3:

- I especially want to thank fredt at [hsqldb.org](http://hsqldb.org/) for:

    - His welcome for this project and his permission to use the HsqlDB logo in the extension.

    - The quality of its HsqlDB database.

- Now works with OpenOffice on Windows.

- When unzipping, a file name clash now displays a precise error.

- Now correctly handles spaces in filenames and paths.

- Many other fix...

### What remains to be done for version 0.0.3:

- Add new language for internationalization...

- Anything welcome...
