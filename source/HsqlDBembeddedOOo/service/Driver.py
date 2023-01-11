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

from com.sun.star.embed.ElementModes import SEEKABLEREAD
from com.sun.star.embed.ElementModes import READWRITE
from com.sun.star.embed.ElementModes import TRUNCATE

from com.sun.star.lang import XServiceInfo

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from com.sun.star.sdbc import XDriver

from com.sun.star.sdbc import SQLException

from com.sun.star.sdbcx import XDataDefinitionSupplier
from com.sun.star.sdbcx import XCreateCatalog
from com.sun.star.sdbcx import XDropCatalog

from com.sun.star.util import XCloseListener

from com.sun.star.util import CloseVetoException

from hsqldbembedded import Connection

from hsqldbembedded import createService
from hsqldbembedded import getDataBaseInfo
from hsqldbembedded import getSimpleFile
from hsqldbembedded import getUrlTransformer
from hsqldbembedded import parseUrl

from hsqldbembedded import g_identifier
from hsqldbembedded import g_protocol
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
        self._ctx = ctx
        self._supportedProtocol = 'sdbc:embedded:hsqldb'
        self._folder = 'database'
        self._suffix = '.lck'
        self._user = 'SA'
        self._password = ''
        self._transformer = getUrlTransformer(self._ctx)
        msg = getMessage(self._ctx, g_message, 101)
        logMessage(self._ctx, INFO, msg, 'Driver', '__init__()')

    # XDriver
    def connect(self, url, infos):
        try:
            path, document, storage = self._getConnectionInfo(infos)
            if path is None or document is None or storage is None:
                code = getMessage(self._ctx, g_message, 111)
                msg = getMessage(self._ctx, g_message, 112, url)
                raise self._getException(code, 1001, msg, self)
            msg = getMessage(self._ctx, g_message, 113, path)
            logMessage(self._ctx, INFO, msg, 'Driver', 'connect()')
            self._splitDataBase(document, path)
            location = self._getConnectionUrl(document, path)
            connection = Connection(self._ctx, document, location, url, infos, self._user, self._password)
            document.addCloseListener(CloseListener(self))
            version = connection.getMetaData().getDriverVersion()
            msg = getMessage(self._ctx, g_message, 116, (version, self._user))
            logMessage(self._ctx, INFO, msg, 'Driver', 'connect()')
            return connection
        except SQLException as e:
            raise e
        except Exception as e:
            msg = getMessage(self._ctx, g_message, 117, (e, traceback.print_exc()))
            logMessage(self._ctx, SEVERE, msg, 'Driver', 'connect()')

    def acceptsURL(self, url):
        accept = url.startswith(self._supportedProtocol)
        msg = getMessage(self._ctx, g_message, 121, (url, accept))
        logMessage(self._ctx, INFO, msg, 'Driver', 'acceptsURL()')
        return accept

    def getPropertyInfo(self, url, infos):
        try:
            print("Driver.getPropertyInfo() Infos: %s" % (infos, ))
            msg = getMessage(self._ctx, g_message, 131, url)
            logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            for info in infos:
                msg = getMessage(self._ctx, g_message, 132, (info.Name, info.Value))
                logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            drvinfo = []
            dbinfo = getDataBaseInfo()
            for info in dbinfo:
                drvinfo.append(self._getDriverPropertyInfo(info, dbinfo[info]))
            for info in infos:
                if info.Name not in dbinfo:
                    drvinfo.append(self._getDriverPropertyInfo(info.Name, info.Value))
            for info in drvinfo:
                msg = getMessage(self._ctx, g_message, 133, (info.Name, info.Value))
                logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            return tuple(drvinfo)
        except Exception as e:
            msg = getMessage(self._ctx, g_message, 134, (e, traceback.print_exc()))
            logMessage(self._ctx, SEVERE, msg, 'Driver', 'getPropertyInfo()')

    def getMajorVersion(self):
        return self._connection.getMajorVersion()
    def getMinorVersion(self):
        return self._connection.getMinorVersion()

    # XDataDefinitionSupplier
    def getDataDefinitionByConnection(self, connection):
        msg = getMessage(self._ctx, g_message, 141)
        logMessage(self._ctx, INFO, msg, 'Driver', 'getDataDefinitionByConnection()')
        return self._connection.getDataDefinitionByConnection(connection)
    def getDataDefinitionByURL(self, url, infos):
        msg = getMessage(self._ctx, g_message, 151, url)
        logMessage(self._ctx, INFO, msg, 'Driver', 'getDataDefinitionByURL()')
        return self._connection.getDataDefinitionByURL(url, infos)

    # XCreateCatalog
    def createCatalog(self, info):
        msg = getMessage(self._ctx, g_message, 161)
        logMessage(self._ctx, INFO, msg, 'Driver', 'createCatalog()')

    # XDropCatalog
    def dropCatalog(self, name, info):
        msg = getMessage(self._ctx, g_message, 171, name)
        logMessage(self._ctx, INFO, msg, 'Driver', 'dropCatalog()')

    # Driver setter method
    def queryClosingDocument(self, document):
        path = self._parseUrl(document.URL)
        name = self._getDataSourceName(document.Title)
        url = self._getSplitUrl(path, name)
        if self._closeDocument(document, url):
            sf = getSimpleFile(self._ctx)
            if sf.isFolder(url):
                sf.kill(url)

    # Driver private method
    def _closeDocument(self, document, url):
        target = document.getDocumentSubStorage(self._folder, READWRITE)
        service = 'com.sun.star.embed.FileSystemStorageFactory'
        args = (url, READWRITE)
        source = createService(self._ctx, service).createInstanceWithArguments(args)
        for name in source.getElementNames():
            if source.isStreamElement(name):
                if target.hasByName(name):
                    target.removeElement(name)
                source.moveElementTo(name, target, name)
        empty = not source.hasElements()
        target.commit()
        target.dispose()
        source.dispose()
        document.store()
        return empty

    def _getConnectionInfo(self, infos):
        path = document = storage = None
        for info in infos:
            if info.Name == 'URL':
                path = self._parseUrl(info.Value)
            elif info.Name == 'Document':
                document = info.Value
            elif info.Name == 'Storage':
                storage = info.Value
        return path, document, storage

    def _parseUrl(self, url):
        location = parseUrl(self._transformer, url)
        path = parseUrl(self._transformer, location.Protocol + location.Path)
        return self._transformer.getPresentation(path, False)

    def _getDataSourceName(self, title):
        name, sep, extension = title.rpartition('.')
        return name

    def _splitDataBase(self, document, path):
        sf = getSimpleFile(self._ctx)
        storage = document.getDocumentSubStorage(self._folder, READWRITE)
        url = self._getSplitUrl(path, self._getDataSourceName(document.Title))
        for name in storage.getElementNames():
            if storage.isStreamElement(name):
                location = self._getSplitLocation(url, name)
                if not sf.exists(location):
                    input = storage.openStreamElement(name, SEEKABLEREAD).getInputStream()
                    sf.writeFile(location, input)
                    input.closeInput()
        storage.dispose()

    def _getSplitUrl(self, path, name):
        return '%s.%s%s' % (path, name, self._suffix)

    def _getSplitLocation(self, url, name):
        return '%s/%s' % (url, name)

    def _getConnectionUrl(self, document, path):
        name = self._getDataSourceName(document.Title)
        url = self._getSplitUrl(path, name)
        return '%s%s/%s%s%s' % (g_protocol, url, name, g_options, g_shutdown)

    def _getDriverPropertyInfo(self, name, value):
        info = uno.createUnoStruct('com.sun.star.sdbc.DriverPropertyInfo')
        info.Name = name
        required = value is not None and not isinstance(value, tuple)
        info.IsRequired = required
        if required:
            info.Value = value
        info.Choices = ()
        return info

    def _getException(self, state, code, message, context=None, exception=None):
        error = SQLException()
        error.SQLState = state
        error.ErrorCode = code
        error.NextException = exception
        error.Message = message
        error.Context = context
        return error

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


class CloseListener(unohelper.Base,
                    XCloseListener):
    def __init__(self, driver):
        self._driver = driver

    # XCloseListener
    def queryClosing(self, event, owner):
        self._driver.queryClosingDocument(event.Source)

    def notifyClosing(self, event):
        pass

    # XEventListener
    def disposing(self, event):
        pass

