# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone.app.textfield import RichText
from plone.app.widgets.dx import DateWidget
from plone.app.widgets.dx import RelatedItemsWidget
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.supermodel import model
from unep import _
from unep.utils import get_field
from unep.utils import get_fieldname
from unep.utils import get_translated
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implements


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

    location = schema.TextLine(
        title=_(u'Location'),
        description=_(u'Location where meeting is going to happen '
                      u'eg: Kingston, Jamaica'),
        required=False,
    )

    meeting_type = schema.Choice(
        title=_(u'Meeting type'),
        description=_(u'TODO'),
        values=[
            ("CEP - IGM", u'CEP - IGM'),
            ("CEP - MONCOM", u'CEP - MONCOM'),
            ("SPAW - ISTAC", u'SPAW - ISTAC'),
            ("SPAW - Workshop", u'SPAW - Workshop'),
            ("SPAW - COP", u'SPAW - COP'),
            ("SPAW - STAC", u'SPAW - STAC'),
            ("LBS - ISTAC", u'LBS - ISTAC'),
            ("LBS - Workshop", u'LBS - Workshop'),
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

    en_title = schema.TextLine(
        title=_(u'Meeting Name'),
        description=_(u'The name or title of the meeting'),
        required=False,
    )

    en_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    en_travel_info = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    en_visa_info = RichText(
        title=_(u'Travel and visa information'),
        description=_(u''),
        required=False,
    )

    en_additional_text = RichText(
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
            'en_travel_info',
            'en_visa_info',
            'en_additional_text',
        ]
    )

    es_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    es_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    es_travel_info = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    es_visa_info = RichText(
        title=_(u'Travel and visa information'),
        description=_(u''),
        required=False,
    )

    es_additional_text = RichText(
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
            'es_travel_info',
            'es_visa_info',
            'es_additional_text',
        ],
    )

    fr_title = schema.TextLine(
        title=u'Title',
        required=False,
    )

    fr_announcement = RichText(
        title=_(u'Announcement'),
        description=_(u''),
        required=False,
    )

    fr_travel_info = RichText(
        title=_(u'Information note for participants'),
        description=_(u''),
        required=False,
    )

    fr_visa_info = RichText(
        title=_(u'Travel and visa information'),
        description=_(u''),
        required=False,
    )

    fr_additional_text = RichText(
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
            'fr_travel_info',
            'fr_visa_info',
            'fr_additional_text',
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
    def travel_info(self):
        return get_translated(self.context, self.request, 'travel_info')

    @property
    def visa_info(self):
        return get_translated(self.context, self.request, 'visa_info')

    @property
    def additional_text(self):
        return get_translated(self.context, self.request, 'additional_text')


class MeetingDownloadsView(BrowserView):
    """
    """

    def get_files(self, field_name):
        files = []
        for item in getattr(self.context, field_name):
            description = ''
            title = get_translated(item.to_object, self.request, 'title', True)

            if item.to_object.code:
                description = title
                title = item.to_object.code

            if not title:
                title = item.to_object.id

            field = get_field(item.to_object, 'file', None)
            fieldname = get_fieldname(item.to_object, 'file')
            if field:
                files.append({
                    'id': item.to_object.id,
                    'title': title,
                    'description': description,
                    'name': field.filename,
                    'url': '{url}/@@download/{fieldname}'.format(
                        url=item.to_object.absolute_url(),
                        fieldname=fieldname,
                    )
                })
        return files

    @property
    def files_working(self):
        return self.get_files('files_working')

    def files_information(self):
        return self.get_files('files_information')

    def files_reference(self):
        return self.get_files('files_reference')

    def files_conference_papers(self):
        return self.get_files('files_conference_papers')

    def files_final_reports(self):
        return self.get_files('files_final_reports')

    def files_presentations(self):
        return self.get_files('files_presentations')

    def files_others(self):
        return self.get_files('files_others')
