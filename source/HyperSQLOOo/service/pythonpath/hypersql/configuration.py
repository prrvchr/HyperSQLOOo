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

from .jdbcdriver import g_services

# General configuration
g_catalog = 'hsqldb'
g_dbname = 'HyperSQL'
g_extension = '%sOOo' % g_dbname
g_identifier = 'io.github.prrvchr.%s' % g_extension
g_resource = 'resource'
g_basename = 'Driver'
g_defaultlog = '%sLogger' % g_dbname
g_errorlog = '%sError' % g_dbname

# DataBase configuration
g_protocol = 'xdbc:hsqldb:'
g_url = 'sdbc:embedded:hsqldb'
g_user = 'SA'
g_options = ';hsqldb.default_table_type=cached;shutdown=true'
g_create = ''
g_exist = ';create=false'
g_path = False
g_driver = ''
g_shutdown = ''

# LibreOffice configuration
g_lover = '5.0'

