# -*- coding: utf-8 -*-

from plone.dexterity.utils import createContentInContainer
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from mimetypes import guess_type
from os.path import splitext
from plone.dexterity.content import Container
from plone.namedfile.file import NamedBlobFile
from plone.supermodel import model
from thread import allocate_lock
from unep import _
from zope import schema
from zope.interface import implements

import json
import transaction

upload_lock = allocate_lock()


class IFileFolder(model.Schema):
    """
    """

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )


class FileFolder(Container):
    """
    """

    implements(IFileFolder)


class FileFolderView(BrowserView):
    """
    """


class FileFolderUpload(BrowserView):
    """
    """

    def __call__(self):
        if self.request.REQUEST_METHOD != 'POST':
            return

        filedata = self.request.form.get("file", None)
        if not filedata:
            return

        filename = safe_unicode(filedata.filename.decode("utf8"))
        content_type = guess_type(filename)[0] or ""
        language = splitext(filename)[0][-2:]
        obj_id = splitext(filename)[0][:-3]

        # otherwise I get ZPublisher.Conflict ConflictErrors
        # when uploading multiple files
        upload_lock.acquire()

        try:
            transaction.begin()

            file_ = NamedBlobFile(
                data=filedata,
                filename=filename,
                contentType=content_type,
            )

            if obj_id in self.context.objectIds():
                obj = self.context[obj_id]
                setattr(obj, language + '_file', file_)
            else:
                obj = createContentInContainer(self.context, 'unep.file',
                                               **({language + '_file': file_}))

            obj.reindexObject()
            transaction.commit()

        finally:
            upload_lock.release()

        if language == 'en':
            language = _('English')
        elif language == 'es':
            language = _('Spanish')
        elif language == 'fr':
            language = _('French')

        return json.dumps({
            'id': obj.UID(),
            'title': obj.title_or_id(),
            'language': language,
            'url': obj.absolute_url(),
        })
