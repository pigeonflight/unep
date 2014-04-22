# -*- coding: utf-8 -*-

from zope.schema import TextLine
from zope.schema import Text
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from plone.dexterity.content import Item
#from plone.autoform import directives as form
from unep.utils import get_field


class IFile(model.Schema):
    """
    """

    en_code = TextLine(
        title=u'Code',
        required=False,
        )

    en_title = TextLine(
        title=u'Title',
        required=False,
        )

    en_description = Text(
        title=u'Description',
        required=False,
        )

    en_file = NamedBlobFile(
        title=u'File',
        required=False,
        )

    model.fieldset(
        'en',
        label=u"English",
        fields=['en_code', 'en_title', 'en_description', 'en_file']
        )

    es_code = TextLine(
        title=u'Code',
        required=False,
        )

    es_title = TextLine(
        title=u'Title',
        required=False,
        )

    es_description = Text(
        title=u'Description',
        required=False,
        )

    es_file = NamedBlobFile(
        title=u'File',
        required=False,
        )

    model.fieldset(
        'es',
        label=u"Spanish",
        fields=['es_code', 'es_title', 'es_description', 'es_file']
        )

    fr_code = TextLine(
        title=u'Code',
        required=False,
        )

    fr_title = TextLine(
        title=u'Title',
        required=False,
        )

    fr_description = Text(
        title=u'Description',
        required=False,
        )

    fr_file = NamedBlobFile(
        title=u'File',
        required=False,
        )

    model.fieldset(
        'fr',
        label=u"French",
        fields=['fr_code', 'fr_title', 'fr_description', 'fr_file']
        )


class File(Item):
    """
    """

    @property
    def title(self):
        return get_field(self, 'title', '')

    def setTitle(self, value):
        return

    @property
    def description(self):
        return get_field(self, 'description', '')

    def setDescription(self, value):
        return
