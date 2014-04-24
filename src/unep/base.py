# -*- coding: utf-8 -*-

from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.content import Item
from zope.interface import implements


def get_field(self, field, default):
    if hasattr(self, 'en_' + field) and getattr(self, 'en_' + field):
        return getattr(self, 'en_' + field)
    elif hasattr(self, 'es_' + field) and getattr(self, 'es_' + field):
        return getattr(self, 'es_' + field)
    elif hasattr(self, 'fr_' + field) and getattr(self, 'fr_' + field):
        return getattr(self, 'fr_' + field)
    else:
        return default


class LanguageItem(Item):

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


class INameFromLanguageItem(INameFromTitle):

    def title():
        """Return a processed title"""


class NameFromLanguageItem(object):

    implements(INameFromLanguageItem)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return get_field(self.context, 'title', '')
