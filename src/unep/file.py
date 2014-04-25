# -*- coding: utf-8 -*-

from Acquisition import aq_parent
from Products.Five.browser import BrowserView
from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from unep import _
from unep.utils import get_field
from zope import schema
from zope.interface import Invalid
from zope.interface import implements
from zope.interface import invariant


class AtLeastOneFile(Invalid):
    __doc__ = _(u'You need to upload at least one file.')


class IFile(model.Schema):
    """
    """

    code = schema.TextLine(
        title=_(u'Code'),
        required=False,
    )

    # TODO: hidden uid

    model.fieldset(
        'language_independent',
        label=_(u'Language independent'),
        fields=['code'],
    )

    en_title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    en_description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    en_file = NamedBlobFile(
        title=_(u'File'),
        required=False,
    )

    model.fieldset(
        'en',
        label=_(u'English'),
        fields=['en_title', 'en_description', 'en_file']
    )

    es_title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    es_description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    es_file = NamedBlobFile(
        title=_(u'File'),
        required=False,
    )

    model.fieldset(
        'es',
        label=_(u'Spanish'),
        fields=['es_title', 'es_description', 'es_file']
    )

    fr_title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    fr_description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    fr_file = NamedBlobFile(
        title=_(u'File'),
        required=False,
    )

    model.fieldset(
        'fr',
        label=_(u'French'),
        fields=['fr_title', 'fr_description', 'fr_file']
    )


class File(Item):
    """
    """

    implements(IFile)

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


class INameFromFile(INameFromTitle):

    def title():
        """Return a processed title"""


class NameFromFile(object):

    implements(INameFromFile)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return self.context.code + '-' + get_field(self.context, 'title', '')


class FileView(BrowserView):
    """
    """

    def __call__(self):
        self.request.response.redirect(
            aq_parent(self.context).absolute_url())
