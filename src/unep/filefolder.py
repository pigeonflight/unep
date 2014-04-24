# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from unep import _
from zope import schema
from zope.interface import implements


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
