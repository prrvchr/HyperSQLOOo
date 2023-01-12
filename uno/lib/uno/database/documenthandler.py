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

import unohelper

from com.sun.star.embed.ElementModes import SEEKABLEREAD
from com.sun.star.embed.ElementModes import READWRITE

from com.sun.star.util import XCloseListener

from .unotool import createService
from .unotool import getSimpleFile
from .unotool import getUrlTransformer
from .unotool import parseUrl

import traceback


class DocumentHandler(unohelper.Base,
                      XCloseListener):
    def __init__(self, ctx):
        self._ctx = ctx
        self._folder = 'database'
        self._prefix = '.'
        self._suffix = '.lck'

    # XCloseListener
    def queryClosing(self, event, owner):
        document = event.Source
        name = self._getDataSourceName(document.Title)
        path = self._getDataBasePath(document.URL, name)
        if self._closeDataBase(document, path):
            sf = getSimpleFile(self._ctx)
            if sf.isFolder(path):
                sf.kill(path)

    def notifyClosing(self, event):
        pass

    # XEventListener
    def disposing(self, event):
        pass

    # Document getter methods
    def openDataBase(self, document):
        name = self._getDataSourceName(document.Title)
        path = self._getDataBasePath(document.URL, name)
        sf = getSimpleFile(self._ctx)
        storage = document.getDocumentSubStorage(self._folder, READWRITE)
        for element in storage.getElementNames():
            if storage.isStreamElement(element):
                url = self._getFileUrl(path, element)
                if not sf.exists(url):
                    input = storage.openStreamElement(element, SEEKABLEREAD).getInputStream()
                    sf.writeFile(url, input)
                    input.closeInput()
        storage.dispose()
        return path, name

    # Document private methods
    def _closeDataBase(self, document, url):
        target = document.getDocumentSubStorage(self._folder, READWRITE)
        service = 'com.sun.star.embed.FileSystemStorageFactory'
        args = (url, READWRITE)
        source = createService(self._ctx, service).createInstanceWithArguments(args)
        for element in source.getElementNames():
            if source.isStreamElement(element):
                if target.hasByName(element):
                    target.removeElement(element)
                source.moveElementTo(element, target, element)
        empty = not source.hasElements()
        target.commit()
        target.dispose()
        source.dispose()
        document.store()
        return empty

    def _getDataBasePath(self, url, name):
        path = self._getDocumentPath(url)
        return '%s%s%s%s' % (path, self._prefix, name, self._suffix)

    def _getDataSourceName(self, title):
        name, sep, extension = title.rpartition('.')
        return name

    def _getDocumentPath(self, location):
        transformer = getUrlTransformer(self._ctx)
        url = parseUrl(transformer, location)
        path = parseUrl(transformer, url.Protocol + url.Path)
        return transformer.getPresentation(path, False)

    def _getFileUrl(self, path, name):
        return '%s/%s' % (path, name)

