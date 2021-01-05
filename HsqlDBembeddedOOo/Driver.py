#!
# -*- coding: utf_8 -*-

"""
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
"""

import uno
import unohelper

from com.sun.star.lang import XServiceInfo
from com.sun.star.sdbc import XDriver
from com.sun.star.sdbcx import XDataDefinitionSupplier
from com.sun.star.sdbcx import XCreateCatalog
from com.sun.star.sdbcx import XDropCatalog

from com.sun.star.sdbc import SQLException

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from com.sun.star.uno import Exception as UnoException

from unolib import getResourceLocation
from unolib import createService
from unolib import getSimpleFile
from unolib import getUrl
from unolib import getNamedValueSet

from hsqldbembedded import Connection
from hsqldbembedded import getDataBaseInfo
from hsqldbembedded import g_identifier
from hsqldbembedded import g_protocol
from hsqldbembedded import g_path
from hsqldbembedded import g_jar
from hsqldbembedded import g_class
from hsqldbembedded import g_options
from hsqldbembedded import g_shutdown

from hsqldbembedded import logMessage
from hsqldbembedded import getMessage
g_message = 'Driver'

import traceback

# pythonloader looks for a static g_ImplementationHelper variable
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationName = '%s.Driver' % g_identifier


class Driver(unohelper.Base,
             XServiceInfo,
             XDataDefinitionSupplier,
             XCreateCatalog,
             XDropCatalog,
             XDriver):

    def __init__(self, ctx):
        self.ctx = ctx
        self._supportedProtocol = 'sdbc:embedded:hsqldb'
        self._dbdir = 'database/'
        self._dbfiles = ('script', 'properties', 'data', 'backup', 'log')
        self._defaultUser = 'SA'
        print("Driver.__init__()")

    def __del__(self):
        print("Driver.__del__()")

    # XDataDefinitionSupplier
    def getDataDefinitionByConnection(self, connection):
        print("Driver.getDataDefinitionByConnection()")
        return connection
    def getDataDefinitionByURL(self, url, infos):
        print("Driver.getDataDefinitionByURL()")
        connection = self.connect(url, infos)
        return self.getDataDefinitionByConnection(connection)

    # XCreateCatalog
    def createCatalog(self, info):
        print("Driver.createCatalog()")

    # XDropCatalog
    def dropCatalog(self, name, info):
        print("Driver.dropCatalog()")

    # XDriver
    def connect(self, url, infos):
        try:
            print("Driver.connect() 1 %s" % (url, ))
            location = self._getUrl(infos)
            name = self._getDataSourceName(location)
            print("Driver.connect() 2 %s - %s" % (location.Path, name))
            sf = getSimpleFile(self.ctx)
            if not sf.isFolder('%s%s' % (location.Path, name)):
                self._splitDataBase(sf, location, name)
            datasource = self._getDataSource(location, name)
            print("Driver.connect() 3: %s\n%s" % (datasource.URL, datasource.Settings.JavaDriverClassPath))
            connection = datasource.getConnection('', '')
            version = connection.getMetaData().getDriverVersion()
            print("Driver.connect() 4 %s" % version)
            print("Driver.connect() 5 %s" % url)
            return Connection(self.ctx, connection, url, self._defaultUser)
        except SQLException as e:
            raise e
        except Exception as e:
            print("Driver.connect() ERROR: %s - %s" % (e, traceback.print_exc()))

    def acceptsURL(self, url):
        print("Driver.acceptsURL() %s" % url)
        return url.startswith(self._supportedProtocol)

    def getPropertyInfo(self, url, infos):
        try:
            print("Driver.getPropertyInfo() %s" % url)
            for info in infos:
                print("Driver.getPropertyInfo():   %s - '%s'" % (info.Name, info.Value))
            drvinfo = []
            dbinfo = getDataBaseInfo()
            for info in dbinfo:
                drvinfo.append(self._getDriverPropertyInfo(info, dbinfo[info]))
            for info in infos:
                if info.Name not in dbinfo:
                    drvinfo.append(self._getDriverPropertyInfo(info.Name, info.Value))
            print("Driver.getPropertyInfo():\n")
            for info in drvinfo:
                print("Driver.getPropertyInfo():   %s - %s" % (info.Name, info.Value))
            return tuple(drvinfo)
        except Exception as e:
            print("Driver.getPropertyInfo() ERROR: %s - %s" % (e, traceback.print_exc()))

    def getMajorVersion(self):
        print("Driver.getMajorVersion()")
        return 1
    def getMinorVersion(self):
        print("Driver.getMinorVersion()")
        return 0

    def _splitDataBase(self, sf, location, dbname):
        service = 'com.sun.star.packages.zip.ZipFileAccess'
        args = (location.Main, )
        zip = createService(self.ctx, service, *args)
        for name in self._dbfiles:
            path = '%s%s' % (self._dbdir, name)
            if zip.hasByName(path):
                url = self._getDataBaseUrl(location, dbname, name)
                if not sf.exists(url):
                    input = zip.getStreamByPattern(path)
                    sf.writeFile(url, input)
                    input.closeInput()
                    print("Driver._splitDataBase() %s - %s" % (path, url))

    def _getDataBaseUrl(self, location, dbname, name):
        return '%s%s/%s.%s' % (location.Path, dbname, dbname, name)

    def _getInfo(self, infos):
        for info in infos:
            print("Driver._getInfo() %s - %s" % (info.Name, info.Value))
            if info.Name == 'URL':
                url = info.Value.strip()
                break
        return url

    def _getUrl(self, infos):
        url = self._getInfo(infos)
        return getUrl(self.ctx, url)

    def _getException(self, state, code, message, context=None, exception=None):
        error = SQLException()
        error.SQLState = state
        error.ErrorCode = code
        error.NextException = exception
        error.Message = message
        error.Context = context
        return error

    def _getDriverPropertyInfo(self, name, value):
        info = uno.createUnoStruct('com.sun.star.sdbc.DriverPropertyInfo')
        print("Driver._getDriverPropertyInfo() %s - %s - %s" % (name, value, type(value)))
        info.Name = name
        required = value is not None and not isinstance(value, tuple)
        info.IsRequired = required
        if required:
            info.Value = value
        info.Choices = ()
        return info

    def _getDataSource(self, url, name):
        service = 'com.sun.star.sdb.DatabaseContext'
        datasource = createService(self.ctx, service).createInstance()
        self._setDataSource(datasource, url, name)
        return datasource

    def _setDataSource(self, datasource, url, name):
        datasource.URL = self._getDataSourceUrl(url, name)
        datasource.Settings.JavaDriverClass = g_class
        datasource.Settings.JavaDriverClassPath = self._getDataSourceClassPath()

    def _getDataSourceName(self, url):
        name, sep, extension = url.Name.rpartition('.')
        return name

    def _getDataSourceUrl(self, url, name):
        path = uno.fileUrlToSystemPath('%s%s%s/%s' % (url.Protocol, url.Path, name, name))
        location = '%s%s%s%s%s' % (g_protocol, url.Protocol, path, g_options, g_shutdown)
        return location

    def _getDataSourceClassPath(self):
        path = getResourceLocation(self.ctx, g_identifier, g_path)
        return '%s/%s' % (path, g_jar)

    # XServiceInfo
    def supportsService(self, service):
        return g_ImplementationHelper.supportsService(g_ImplementationName, service)
    def getImplementationName(self):
        return g_ImplementationName
    def getSupportedServiceNames(self):
        return g_ImplementationHelper.getSupportedServiceNames(g_ImplementationName)


g_ImplementationHelper.addImplementation(Driver,
                                         g_ImplementationName,
                                        (g_ImplementationName,
                                        'com.sun.star.sdbc.Driver',
                                        'com.sun.star.sdbcx.Driver'))
