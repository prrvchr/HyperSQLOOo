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

from com.sun.star.beans.PropertyAttribute import READONLY

from com.sun.star.container import XChild

from com.sun.star.lang import XComponent
from com.sun.star.lang import XServiceInfo

from com.sun.star.sdbc import XConnection
from com.sun.star.sdbc import XCloseable
from com.sun.star.sdbc import XWarningsSupplier

from com.sun.star.uno import XWeak

from .databasemetadata import DatabaseMetaData

from .datasource import DataSource

from .statement import Statement
from .statement import PreparedStatement
from .statement import CallableStatement

import traceback


class SdbcConnection(unohelper.Base,
                     XServiceInfo,
                     XComponent,
                     XWarningsSupplier,
                     XConnection,
                     XCloseable,
                     XChild,
                     XWeak):
    def __init__(self, connection, datasource, url, infos, user, password):
        self._connection = connection
        self._datasource = datasource
        self._url = url
        self._infos = infos
        self._username = user

    # XComponent
    def dispose(self):
        self._connection.dispose()

    def addEventListener(self, listener):
        self._connection.addEventListener(listener)

    def removeEventListener(self, listener):
        self._connection.removeEventListener(listener)

    # XWeak
    def queryAdapter(self):
        return self

    # XCloseable
    def close(self):
        self._connection.close()

    # XChild
    def getParent(self):
        return DataSource(self._datasource, self._username, self._url)
    def setParent(self):
        pass

    # XWarningsSupplier
    def getWarnings(self):
        return self._connection.getWarnings()

    def clearWarnings(self):
        self._connection.clearWarnings()

    # XConnection
    def createStatement(self):
        return Statement(self)
    def prepareStatement(self, sql):
        # TODO: sometime we cannot use: connection.prepareStatement(sql)
        # TODO: it trow a: java.lang.IncompatibleClassChangeError
        # TODO: if self._patched: fallback to connection.prepareCall(sql)
        return PreparedStatement(self, sql)
    def prepareCall(self, sql):
        return CallableStatement(self, sql)
    def nativeSQL(self, sql):
        return self._connection.nativeSQL(sql)
    def setAutoCommit(self, auto):
        self._connection.setAutoCommit(auto)
    def getAutoCommit(self):
        return self._connection.getAutoCommit()
    def commit(self):
        self._connection.commit()
    def rollback(self):
        self._connection.rollback()
    def isClosed(self):
        return self._connection.isClosed()
    def getMetaData(self):
        metadata = self._connection.getMetaData()
        return DatabaseMetaData(self, metadata, self._url, self._infos, self._username)
    def setReadOnly(self, readonly):
        self._connection.setReadOnly(readonly)
    def isReadOnly(self):
        return self._connection.isReadOnly()
    def setCatalog(self, catalog):
        self._connection.setCatalog(catalog)
    def getCatalog(self):
        return self._connection.getCatalog()
    def setTransactionIsolation(self, level):
        self._connection.setTransactionIsolation(level)
    def getTransactionIsolation(self):
        return self._connection.getTransactionIsolation()
    def getTypeMap(self):
        return self._connection.getTypeMap()
    def setTypeMap(self, typemap):
        self._connection.setTypeMap(typemap)

    # XServiceInfo
    def supportsService(self, service):
        return self._connection.supportsService(service)
    def getImplementationName(self):
        return self._connection.getImplementationName()
    def getSupportedServiceNames(self):
        return self._connection.getSupportedServiceNames()

