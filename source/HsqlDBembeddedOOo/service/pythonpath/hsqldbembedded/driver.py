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

from .sdbconnection import SdbConnection
from .sdbcconnection import SdbcConnection
from .sdbcxconnection import SdbcxConnection

from .documenthandler import DocumentHandler

from .unotool import createService

from .configuration import g_identifier

from .dbconfig import g_protocol

from .logger import logMessage
from .logger import getMessage
g_message = 'Driver'

import traceback


class Driver(unohelper.Base,
             XServiceInfo,
             XDriver):

    def __init__(self, ctx, lock, service, name):
        self._ctx = ctx
        self._supportedProtocol = 'sdbc:embedded:hsqldb'
        self._user = 'SA'
        self._password = ''
        self._lock = lock
        self._service = service
        self._name = name
        # FIXME: Driver is not a Singleton we need to load only once.
        self._driver = None
        # FIXME: If we want to add the StorageChangeListener only once,
        # FIXME: we need to be able to retrieve the DocumentHandler (keep a reference)
        self._handlers = []

    # XDriver
    def connect(self, url, infos):
        try:
            document, storage, location = self._getConnectionInfo(infos)
            if storage is None or location is None:
                code = getMessage(self._ctx, g_message, 111)
                msg = getMessage(self._ctx, g_message, 112, url)
                raise self._getException(code, 1001, msg, self)
            driver = self._getDriver()
            handler = self._getDocumentHandler(location)
            datasource, path = handler.getDocumentInfo(document, storage, location)
            msg = getMessage(self._ctx, g_message, 113, location)
            logMessage(self._ctx, INFO, msg, 'Driver', 'connect()')
            connection = self._getConnection(driver.connect(path, infos), datasource, url, infos)
            version = connection.getMetaData().getDriverVersion()
            msg = getMessage(self._ctx, g_message, 114, version, self._user)
            logMessage(self._ctx, INFO, msg, 'Driver', 'connect()')
            return connection
        except SQLException as e:
            raise e
        except Exception as e:
            msg = getMessage(self._ctx, g_message, 117, e, traceback.print_exc())
            logMessage(self._ctx, SEVERE, msg, 'Driver', 'connect()')

    def acceptsURL(self, url):
        accept = url.startswith(self._supportedProtocol)
        msg = getMessage(self._ctx, g_message, 121, url, accept)
        logMessage(self._ctx, INFO, msg, 'Driver', 'acceptsURL()')
        return accept

    def getPropertyInfo(self, url, infos):
        try:
            msg = getMessage(self._ctx, g_message, 131, url)
            logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            driver = self._getDriver()
            drvinfo = driver.getPropertyInfo(g_protocol, infos)
            for info in drvinfo:
                msg = getMessage(self._ctx, g_message, 132, info.Name, info.Value)
                logMessage(self._ctx, INFO, msg, 'Driver', 'getPropertyInfo()')
            return drvinfo
        except SQLException as e:
            raise e
        except Exception as e:
            msg = getMessage(self._ctx, g_message, 133, e, traceback.print_exc())
            logMessage(self._ctx, SEVERE, msg, 'Driver', 'getPropertyInfo()')

    def getMajorVersion(self):
        return 1
    def getMinorVersion(self):
        return 0

    # XServiceInfo
    def supportsService(self, service):
        return service in self._services
    def getImplementationName(self):
        return self._name
    def getSupportedServiceNames(self):
        return self._services

    # Driver private getter methods
    def _getDriver(self):
        # FIXME: If jdbcDriverOOo is not installed,
        # FIXME: we need to throw SQLException
        if self._driver is None:
            driver = createService(self._ctx, self._service)
            if driver is None:
                code = getMessage(self._ctx, g_message, 181)
                msg = getMessage(self._ctx, g_message, 182, self._service)
                raise self._getException(code, 1001, msg, self)
            self._driver = driver
        return self._driver

    def _getConnectionInfo(self, infos):
        document = storage = url = None
        for info in infos:
            if info.Name == 'URL':
                url = info.Value
            elif info.Name == 'Storage':
                storage = info.Value
            elif info.Name == 'Document':
                document = info.Value
        return document, storage, url

    def _getHandler(self, location):
        document = None
        for handler in self._handlers:
            url = handler.URL
            if url is None:
                self._handlers.remove(handler)
            elif url == location:
                document = handler
        return document

    def _getDocumentHandler(self, location):
        with self._lock:
            handler = self._getHandler(location)
            if handler is None:
                handler = DocumentHandler(self._ctx, self._lock, location)
                self._handlers.append(handler)
            return handler

    def _getConnection(self, connection, datasource, url, infos):
        if connection.supportsService('com.sun.star.sdb.Connection'):
            return SdbConnection(connection, datasource, url, infos, self._user, self._password)
        elif connection.supportsService('com.sun.star.sdbcx.Connection'):
            return SdbcxConnection(connection, datasource, url, infos, self._user, self._password)
        elif connection.supportsService('com.sun.star.sdbc.Connection'):
            return SdbcConnection(connection, datasource, url, infos, self._user, self._password)

    def _getException(self, state, code, message, context=None, exception=None):
        error = SQLException()
        error.SQLState = state
        error.ErrorCode = code
        error.NextException = exception
        error.Message = message
        error.Context = context
        return error

