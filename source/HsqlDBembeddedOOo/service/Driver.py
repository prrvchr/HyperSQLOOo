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

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from com.sun.star.sdbc import XDriver

from com.sun.star.sdbc import SQLException

from com.sun.star.sdbcx import XDataDefinitionSupplier
from com.sun.star.sdbcx import XCreateCatalog
from com.sun.star.sdbcx import XDropCatalog

from com.sun.star.uno import XWeak

from hsqldbembedded import Connection
from hsqldbembedded import DocumentHandler

from hsqldbembedded import createService
from hsqldbembedded import getDataBaseInfo
from hsqldbembedded import getUriFactory
from hsqldbembedded import getUrlTransformer
from hsqldbembedded import parseUrl

from hsqldbembedded import g_identifier
from hsqldbembedded import g_jdbcdriver
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
             XDriver,
             XWeak):

    def __init__(self, ctx):
        self._ctx = ctx
        self._supportedProtocol = 'sdbc:embedded:hsqldb'
        self._user = 'SA'
        self._password = ''
        msg = getMessage(self._ctx, g_message, 101)
        logMessage(self._ctx, INFO, msg, 'Driver', '__init__()')

    # XWeak
    def queryAdapter(self):
        return self

    # XDriver
    def connect(self, url, infos):
        try:
            document, storage, path, name = self._getConnectionInfo(infos)
            if storage is None or path is None or name is None:
                code = getMessage(self._ctx, g_message, 111)
                msg = getMessage(self._ctx, g_message, 112, url)
                raise self._getException(code, 1001, msg, self)
            driver = createService(self._ctx, g_jdbcdriver)
            if driver is None:
                code = getMessage(self._ctx, g_message, 113)
                msg = getMessage(self._ctx, g_message, 114, g_jdbcdriver)
                raise self._getException(code, 1001, msg, self)
            handler = DocumentHandler(self._ctx, storage, path)
            location = self._getConnectionUrl(handler.getDataBasePath(path, name), name)
            msg = getMessage(self._ctx, g_message, 115, location)
            logMessage(self._ctx, INFO, msg, 'Driver', 'connect()')
            if document is None:
                document = self._getDocument(location)
            else:
                document.addCloseListener(handler)
            connection = Connection(driver, document, location, url, infos, self._user, self._password)
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
            msg = getMessage(self._ctx, g_message, 131, url)
            logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            driver = createService(self._ctx, g_jdbcdriver)
            if driver is None:
                code = getMessage(self._ctx, g_message, 132)
                msg = getMessage(self._ctx, g_message, 133, g_jdbcdriver)
                raise self._getException(code, 1001, msg, self)
            drvinfo = driver.getPropertyInfo(g_protocol, infos)
            for info in drvinfo:
                msg = getMessage(self._ctx, g_message, 134, (info.Name, info.Value))
                logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            return drvinfo
        except SQLException as e:
            raise e
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

    # Driver private method
    def _getConnectionInfo(self, infos):
        document = storage = url = path = name = None
        for info in infos:
            if info.Name == 'URL':
                url = info.Value
            elif info.Name == 'Storage':
                storage = info.Value
            elif info.Name == 'Document':
                document = info.Value
        if url is not None:
            path, name = self._getUrlInfo(url)
        return document, storage, path, name

    def _getUrlInfo(self, location):
        transformer = getUrlTransformer(self._ctx)
        url = parseUrl(transformer, location)
        path = self._getDataBasePath(transformer, url)
        name = self._getDataBaseName(transformer, url)
        return path, name

    def _getDataBasePath(self, transformer, url):
        path = parseUrl(transformer, url.Protocol + url.Path)
        return transformer.getPresentation(path, False)

    def _getDataBaseName(self, transformer, location):
        url = transformer.getPresentation(location, False)
        uri = getUriFactory(self._ctx).parse(url)
        name = uri.getPathSegment(uri.getPathSegmentCount() -1)
        return self._getDocumentName(name)

    def _getDocumentName(self, title):
        name, sep, extension = title.rpartition('.')
        return name

    def _getDocument(self, url):
        service = 'com.sun.star.sdb.DatabaseContext'
        datasource = createService(self._ctx, service).createInstance()
        datasource.URL = url
        return datasource.DatabaseDocument

    def _getConnectionUrl(self, url, name):
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

