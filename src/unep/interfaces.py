# -*- coding: utf-8 -*-

from zope.schema import TextLine
from zope.schema import Text
from plone.supermodel import model
from plone.namedfile.field import NamedBlobFile


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


class IMeeting(model.Schema):
    """
    """

    en_title = TextLine(
        title=u'Title',
        required=False,
        )

    en_description = Text(
        title=u'Description',
        required=False,
        )

    model.fieldset(
        'en',
        label=u'English',
        fields=['en_title', 'en_description']
        )

    es_title = TextLine(
        title=u'Title',
        required=False,
        )

    es_description = Text(
        title=u'Description',
        required=False,
        )

    model.fieldset(
        'es',
        label=u"Spanish",
        fields=['es_title', 'es_description']
        )

    fr_title = TextLine(
        title=u'Title',
        required=False,
        )

    fr_description = Text(
        title=u'Description',
        required=False,
        )

    model.fieldset(
        'fr',
        label=u"French",
        fields=['fr_title', 'fr_description']
        )
