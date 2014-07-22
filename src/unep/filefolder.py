# -*- coding: utf-8 -*-

from AccessControl import getSecurityManager
from Products.CMFPlone.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from mimetypes import guess_type
from os.path import splitext
from plone.dexterity.content import Container
from plone.dexterity.utils import addContentToContainer
from plone.dexterity.utils import createContent
from plone.namedfile.file import NamedBlobFile
from plone.supermodel import model
from thread import allocate_lock
from unep import _
from unep.utils import get_language
from zope import schema
from zope.interface import implements

import json
import hashlib
import transaction

upload_lock = allocate_lock()


class IFileFolder(model.Schema):
    """
    """

    title = schema.TextLine(
        title=u'Title',
        required=False,
    )


class FileFolder(Container):
    """
    """

    implements(IFileFolder)


class FileFolderView(BrowserView):
    """
    """

    @property
    def can_add_files(self):
        sm = getSecurityManager()
        return sm.checkPermission('unep: Add File', self.context) == 1

    @property
    def js_i18n(self):
        i18n = {}
        for item in [
                'Uploading...',
                'Error',
                ' does not have a language identifier at the end of it\'s name (-en,-es,-fr). Please rename with a language identifier and attempt to upload again.',
                'Upload successful: ',
                'Following documents were created/updated.',
                'Click on link to edit their metadata.',
                ]:
            i18n[item] = self.translate(item)
        return json.dumps(i18n)

    def translate(self, text):
        language = get_language(self.request)
        tool = getToolByName(self.context, 'translation_service')
        return tool.translate(
            text,
            'unep',
            context=self.context,
            target_language=language,
            default=text
        )


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
        obj_id = hashlib.md5(splitext(filename)[0][:-3]).hexdigest()

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
                obj = createContent(
                    'unep.file',
                    **({language + '_file': file_})
                )
                obj.id = obj_id
                obj = addContentToContainer(self.context, obj)

            obj.reindexObject()
            transaction.commit()

        finally:
            upload_lock.release()

        if language == 'en':
            language = 'English'
        elif language == 'es':
            language = 'Spanish'
        elif language == 'fr':
            language = 'French'

        self.request.RESPONSE.setHeader('content-type', 'application/json')
        return json.dumps({
            'uid': obj.UID(),
            'title': obj.title,
            'language': language,
            'url': obj.absolute_url(),
        })
