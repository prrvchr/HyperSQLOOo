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
    def __init__(self, ctx, storage, path):
        self._ctx = ctx
        self._folder = 'database'
        self._prefix = '.'
        self._suffix = '.lck'
        if storage.hasByName(self._folder) and storage.isStorageElement(self._folder):
            self._openDataBase(storage, path)

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
    def getDataBasePath(self, path, name):
        return '%s%s%s%s' % (path, self._prefix, name, self._suffix)

    # Document private methods
    def _openDataBase(self, storage, path):
        sf = getSimpleFile(self._ctx)
        source = storage.openStorageElement(self._folder, READWRITE)
        # FIXME: With OpenOffice getElementNames() return a String
        # FIXME: if source has no elements.
        if source.hasElements():
            for name in source.getElementNames():
                url = self._getFileUrl(path, name)
                if not sf.exists(url):
                    if source.isStreamElement(name):
                        stream = source.openStreamElement(name, SEEKABLEREAD)
                        input = stream.getInputStream()
                        sf.writeFile(url, input)
                        input.closeInput()
                        stream.dispose()
        source.dispose()

    def _closeDataBase(self, document, url):
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

    def _getDataBasePath(self, url, name):
        path = self._getDocumentPath(url)
        return self.getDataBasePath(path, name)

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

