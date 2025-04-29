#!
# -*- coding: utf_8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020-25 https://prrvchr.github.io                                  ║
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

import unohelper

from com.sun.star.lang import XServiceInfo

from hypersql import sdbc
from hypersql import sdbcx

from hypersql import getConfiguration

from hypersql import g_identifier
from hypersql import g_services

from threading import Lock
import traceback

# pythonloader looks for a static g_ImplementationHelper variable
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationName = 'io.github.prrvchr.HyperSQLOOo.Driver'
g_ServiceNames = ("io.github.prrvchr.HyperSQLOOo.Driver", 'com.sun.star.sdbc.Driver')

# XXX: This class is simply a bootstrap to enable the following:
# XXX: - Provide a single entry for different services meeting the required API levels

class Driver(unohelper.Base,
             XServiceInfo):
    def __new__(cls, ctx, *args, **kwargs):
        print("Driver.__new__() 1")
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    apilevel = getConfiguration(ctx, g_identifier).getByName('ApiLevel')
                    if apilevel == 'com.sun.star.sdbc':
                        instance = sdbc.Driver(ctx, cls._lock, g_services[apilevel], g_ImplementationName)
                    else:
                        instance = sdbcx.Driver(ctx, cls._lock, g_services[apilevel], g_ImplementationName)
                    cls._instance = instance
        return cls._instance

    _instance = None
    _lock = Lock()

    # XServiceInfo
    def supportsService(self, service):
        return g_ImplementationHelper.supportsService(g_ImplementationName, service)
    def getImplementationName(self):
        return g_ImplementationName
    def getSupportedServiceNames(self):
        return g_ImplementationHelper.getSupportedServiceNames(g_ImplementationName)


g_ImplementationHelper.addImplementation(Driver,                          # UNO object class
                                         g_ImplementationName,            # Implementation name
                                         g_ServiceNames)                  # List of implemented services

