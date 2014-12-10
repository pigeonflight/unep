# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from collective.dexteritytextindexer import searchable
from os.path import splitext
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from unep import _
from unep.utils import get_field
from zope import schema
from zope.interface import Invalid
from zope.interface import implements


class AtLeastOneFile(Invalid):
    __doc__ = u'You need to upload at least one file.'


class IFile(model.Schema):
    """
    """

    searchable('code')
    code = schema.TextLine(
        title=u'Code',
        required=False,
    )

    model.fieldset(
        'language_independent',
        label=u'Language independent',
        fields=[
            'code',
        ],
    )

    searchable('en_title')
    en_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    searchable('en_description')
    en_description = schema.Text(
        title=u'Notes',
        required=False,
    )

    en_file = NamedBlobFile(
        title=u'File',
        required=False,
    )

    model.fieldset(
        'en',
        label=u'English',
        fields=['en_title', 'en_description', 'en_file']
    )

    searchable('es_title')
    es_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    searchable('es_description')
    es_description = schema.Text(
        title=u'Notes',
        required=False,
    )

    es_file = NamedBlobFile(
        title=u'File',
        required=False,
    )

    model.fieldset(
        'es',
        label=u'Spanish',
        fields=['es_title', 'es_description', 'es_file']
    )

    searchable('fr_title')
    fr_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    searchable('fr_description')
    fr_description = schema.Text(
        title=u'Notes',
        required=False,
    )

    fr_file = NamedBlobFile(
        title=u'File',
        required=False,
    )

    model.fieldset(
        'fr',
        label=u'French',
        fields=['fr_title', 'fr_description', 'fr_file']
    )


class File(Item):
    """
    """

    implements(IFile)

    @property
    def title(self):
        title = get_field(self, 'title', '')
        if self.code:
            title = '(' + self.code + ')' + title
        if not title:
            field = get_field(self, 'file', None)
            if field:
                title = splitext(field.filename)[0]
        return title

    def setTitle(self, value):
        return

    @property
    def description(self):
        return get_field(self, 'description', '')

    def setDescription(self, value):
        return


def setFileId(context, event):
    filename = None
    if context.en_file:
        filename = context.en_file.filename
    elif context.es_file:
        filename = context.es_file.filename
    elif context.fr_file:
        filename = context.fr_file.filename

    if filename:
        context.id = splitext(filename)[0][:-3]


class FileView(BrowserView):
    """
    """

    pass
    #def __call__(self):
    #    self.request.response.redirect(
    #        self.context.absolute_url() + '/edit')
