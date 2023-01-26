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

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from com.sun.star.sdbcx import XDataDefinitionSupplier
from com.sun.star.sdbcx import XCreateCatalog
from com.sun.star.sdbcx import XDropCatalog

from .driver import Driver

from .logger import logMessage
from .logger import getMessage
g_message = 'Driver'

import traceback


class SdbcxDriver(Driver,
                  XDataDefinitionSupplier,
                  XCreateCatalog,
                  XDropCatalog):

    def __init__(self, ctx, lock, name):
        Driver.__init__(self, ctx, lock, name)
        self._service = 'io.github.prrvchr.jdbcdriver.sdbcx.Driver'
        self._services = ('com.sun.star.sdbc.Driver', 'com.sun.star.sdbcx.Driver')
        msg = getMessage(self._ctx, g_message, 101)
        logMessage(self._ctx, INFO, msg, 'SdbcxDriver', '__init__()')

    # XDataDefinitionSupplier
    def getDataDefinitionByConnection(self, connection):
        try:
            msg = getMessage(self._ctx, g_message, 141)
            logMessage(self._ctx, INFO, msg, 'Driver', 'getDataDefinitionByConnection()')
            driver = self._getDriver()
            if driver is None:
                code = getMessage(self._ctx, g_message, 142)
                msg = getMessage(self._ctx, g_message, 143, self._service)
                raise self._getException(code, 1001, msg, self)
            return driver.getDataDefinitionByConnection(connection)
        except SQLException as e:
            raise e
        except Exception as e:
            msg = getMessage(self._ctx, g_message, 144, (e, traceback.print_exc()))
            logMessage(self._ctx, SEVERE, msg, 'Driver', 'getDataDefinitionByConnection()')

    def getDataDefinitionByURL(self, url, infos):
        msg = getMessage(self._ctx, g_message, 151, url)
        logMessage(self._ctx, INFO, msg, 'Driver', 'getDataDefinitionByURL()')
        return self.getDataDefinitionByConnection(connect(url, infos))

    # XCreateCatalog
    def createCatalog(self, info):
        msg = getMessage(self._ctx, g_message, 161)
        logMessage(self._ctx, INFO, msg, 'Driver', 'createCatalog()')

    # XDropCatalog
    def dropCatalog(self, name, info):
        msg = getMessage(self._ctx, g_message, 171, name)
        logMessage(self._ctx, INFO, msg, 'Driver', 'dropCatalog()')

