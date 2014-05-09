# -*- coding: utf-8 -*-

from AccessControl import getSecurityManager
from Products.CMFPlone.utils import getToolByName
from Products.Five.browser import BrowserView
from collective.dexteritytextindexer import searchable
from plone.app.textfield import RichText
from plone.app.widgets.dx import DateWidget
from plone.app.widgets.dx import RelatedItemsWidget
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from unep import _
from unep.utils import get_field
from unep.utils import get_language
from unep.utils import get_translated
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implements

import os
import tempfile
import zipfile


class IMeeting(model.Schema):
    """
    """

    form.widget('start', DateWidget)
    start = schema.Date(
        title=_(u'Meeting starts'),
        description=_(u'Date when the meeting begins.'),
        required=True,
    )

    form.widget('end', DateWidget)
    end = schema.Date(
        title=_(u'Meeting ends'),
        description=_(u'Date when the meeting ends.'),
        required=True,
    )

    searchable('location')
    location = schema.TextLine(
        title=_(u'Location'),
        description=_(u'Location where meeting is going to happen '
                      u'eg: Kingston, Jamaica'),
        required=False,
    )

    meeting_type = schema.Choice(
        title=_(u'Meeting type'),
        description=_(u'The type of meeting'),
        values=[
            _(u'CEP - IGM'),
            _(u'CEP - MONCOM'),
            _(u'SPAW - ISTAC'),
            _(u'SPAW - Workshop'),
            _(u'SPAW - COP'),
            _(u'SPAW - STAC'),
            _(u'LBS - ISTAC'),
            _(u'LBS - STAC'),
            _(u'LBS - Workshop'),
        ],
        required=False,
    )

    registration_url = schema.URI(
        title=_(u'Registration URL'),
        description=_(u''),
        required=False,
    )

    form.widget(
        'files_working',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_working = RelationList(
        title=_(u'Working documents'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_information',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_information = RelationList(
        title=_(u'Information documents'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_reference',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_reference = RelationList(
        title=_(u'Reference documents'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_conference_papers',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_conference_papers = RelationList(
        title=_(u'Conference papers'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_final_reports',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_final_reports = RelationList(
        title=_(u'Final reports'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_presentations',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_presentations = RelationList(
        title=_(u'Presentations'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget(
        'files_others',
        RelatedItemsWidget,
        pattern_options={
            "selectableTypes": ["UNEP File"],
            "folderTypes": ['UNEP File Folder'],
            "baseCriteria": [{
                'i': 'Type',
                'o': 'plone.app.querystring.operation.string.contains',
                'v': ['UNEP File'],
            }],
        })
    files_others = RelationList(
        title=_(u'Other'),
        description=_(u''),
        value_type=RelationChoice(
            title=_(u'File'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    model.fieldset(
        'language_independent',
        label=_(u'Language independent'),
        fields=[
            'start',
            'end',
            'location',
            'meeting_type',
            'registration_url',
            'files_working',
            'files_information',
            'files_reference',
            'files_conference_papers',
            'files_final_reports',
            'files_presentations',
            'files_others',
        ],
    )

    searchable('en_title')
    en_title = schema.TextLine(
        title=_(u'Meeting Name'),
        description=_(u'The name or title of the meeting'),
        required=False,
    )

    searchable('en_announcement')
    en_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    en_announcement_file = NamedBlobFile(
        title=_(u'Announcement attachement'),
        description=_(u''),
        required=False,
    )

    searchable('en_information')
    en_information = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    en_information_file = NamedBlobFile(
        title=_(u'Information note attachement'),
        description=_(u''),
        required=False,
    )

    searchable('en_additional')
    en_additional = RichText(
        title=_(u'Other'),
        description=_(u''),
        required=False,
    )

    model.fieldset(
        'en',
        label=u'English',
        fields=[
            'en_title',
            'en_announcement',
            'en_announcement_file',
            'en_information',
            'en_information_file',
            'en_additional',
        ]
    )

    searchable('es_title')
    es_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    searchable('es_announcement')
    es_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    es_announcement_file = NamedBlobFile(
        title=_(u'Announcement attachement'),
        description=_(u''),
        required=False,
    )

    searchable('es_information')
    es_information = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    es_information_file = NamedBlobFile(
        title=_(u'Information note attachement'),
        description=_(u''),
        required=False,
    )

    searchable('es_additional')
    es_additional = RichText(
        title=_(u'Other'),
        description=_(u''),
        required=False,
    )

    model.fieldset(
        'es',
        label=u"Spanish",
        fields=[
            'es_title',
            'es_announcement',
            'es_announcement_file',
            'es_information',
            'es_information_file',
            'es_additional',
        ],
    )

    searchable('fr_title')
    fr_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    searchable('fr_announcement')
    fr_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    fr_announcement_file = NamedBlobFile(
        title=_(u'Announcement attachement'),
        description=_(u''),
        required=False,
    )

    searchable('fr_information')
    fr_information = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    fr_information_file = NamedBlobFile(
        title=_(u'Information note attachement'),
        description=_(u''),
        required=False,
    )

    searchable('fr_additional')
    fr_additional = RichText(
        title=_(u'Other'),
        description=_(u''),
        required=False,
    )

    model.fieldset(
        'fr',
        label=u"French",
        fields=[
            'fr_title',
            'fr_announcement',
            'fr_announcement_file',
            'fr_information',
            'fr_information_file',
            'fr_additional',
        ],
    )


class Meeting(Item):
    """
    """

    implements(IMeeting)

    @property
    def title(self):
        return get_field(self, 'title', '')

    def setTitle(self, value):
        return

    @property
    def description(self):
        return get_field(self, 'announcement', '')

    def setDescription(self, value):
        return


class MeetingView(BrowserView):
    """
    """

    @property
    def announcement(self):
        return get_translated(self.context, self.request, 'announcement')

    @property
    def information(self):
        return get_translated(self.context, self.request, 'information')

    @property
    def additional(self):
        return get_translated(self.context, self.request, 'additional')

    @property
    def language(self):
        return get_language(self.request)
    
    @property
    def can_add_files(self):
        sm = getSecurityManager()
        return sm.checkPermission('unep: Add File', self.context) == 1


class MeetingDownloadsView(BrowserView):
    """
    """

    def get_files(self, field_name):
        files = []
        
        for item in getattr(self.context, field_name):
            titles = {}
            if item.to_object:
                code = item.to_object.code
                title = get_field(item.to_object, 'title', '')
                description = get_field(item.to_object, 'description', '')
                languages = []

                if not title:
                    title = item.to_object.id

                _file = {
                    'code': code,
                    'title': title,
                    'description': description,
                    'uid': item.to_object.UID(),
                    'url': item.to_object.absolute_url(),
                    
                }

                if item.to_object.en_file:
                    languages.append('en')
                if item.to_object.es_file:
                    languages.append('es')
                if item.to_object.fr_file:
                    languages.append('fr')

                titles['en'] = titles['es'] = titles['fr'] = None    
                if item.to_object.en_title:
                    titles['en'] = item.to_object.en_title     
                if item.to_object.es_title:
                    titles['es'] = item.to_object.es_title
                if item.to_object.fr_title:
                    titles['fr'] = item.to_object.fr_title
                    
                _file['languages'] = languages
                _file['titles'] = titles
                
                files.append(_file)
        return files
    
    @property
    def can_add_files(self):
        sm = getSecurityManager()
        return sm.checkPermission('unep: Add File', self.context) == 1
        
    def sections(self):
        return [
            {
                'klass': 'jqopen',
                'cl' : 'working-documents',
                'title': 'Working documents',
                'files': self.get_files('files_working'),
            }, {
                'klass': '',
                'cl' : 'information-documents',
                'title': 'Information documents',
                'files': self.get_files('files_information'),
            }, {
                'klass': '',
                'cl' : 'reference-documents',
                'title': 'Reference documents',
                'files': self.get_files('files_reference'),
            }, {
                'klass': '',
                'cl' : 'conference-papers',
                'title': 'Conference papers',
                'files': self.get_files('files_conference_papers'),
            }, {
                'klass': '',
                'cl' : 'final-reports',
                'title': 'Final reports',
                'files': self.get_files('files_final_reports'),
            }, {
                'klass': '',
                'cl' : 'presentations',
                'title': 'Presentations',
                'files': self.get_files('files_presentations'),
            }, {
                'klass': '',
                'cl' : 'others',
                'title': 'Others',
                'files': self.get_files('files_others'),
            }
        ]


class MeetingDownloadsZip(BrowserView):
    """
    """

    def __call__(self):
        if self.request.REQUEST_METHOD != 'POST':
            return

        files = self.request.form.get("files", None)
        if not files:
            return

        catalog = getToolByName(self.context, 'portal_catalog')

        zip_tempfile = tempfile.mktemp()
        ZIP = zipfile.ZipFile(zip_tempfile, 'w')

        if type(files) not in [list, tuple]:
            files = [files]

        files = list(set(files))

        objects = {}
        for item in files:
            uid, lang = item.split(':')

            if uid not in objects.keys():
                objects[uid] = catalog(UID=uid)[0].getObject()

            if hasattr(objects[uid], lang + '_file') and \
                    getattr(objects[uid], lang + '_file'):
                field = getattr(objects[uid], lang + '_file')
                ZIP.writestr(field.filename, field.data)

        ZIP.close()
        data = file(zip_tempfile).read()
        os.unlink(zip_tempfile)
        response = self.request.RESPONSE
        response.setHeader('content-type', 'application/zip')
        response.setHeader('content-length', len(data))
        response.setHeader('content-disposition',
                           'attachment; filename="%s-documents.zip"' % (
                               self.context.getId()))
        return response.write(data)
  
