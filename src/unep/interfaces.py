# -*- coding: utf-8 -*-

from plone.app.event.dx.behaviors import default_end
from plone.app.event.dx.behaviors import default_start
from plone.app.textfield import RichText
from plone.autoform import directives as form
from plone.app.widgets.dx import DatetimeWidget
from plone.app.widgets.dx import RelatedItemsWidget
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from unep import _
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema


class IFile(model.Schema):
    """
    """

    code = schema.TextLine(
        title=_(u'Code'),
        required=True,
        )

    model.fieldset(
        'general',
        label=_(u'General'),
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


class IMeeting(model.Schema):
    """
    """

    form.widget('start', DatetimeWidget)
    start = schema.Datetime(
        title=_(u'Meeting starts'),
        description=_(u'Date and Time, when the meeting begins.'),
        required=True,
        #defaultFactory=default_start,
    )

    form.widget('end', DatetimeWidget)
    end = schema.Datetime(
        title=_(u'Meeting ends'),
        description=_(u'Date and Time, when the meeting ends.'),
        required=True,
        #defaultFactory=default_end,
    )

    address = schema.Text(
        title=_(u'Address'),
        description=_(u'Address where meeting is going to happen '
                      u'eg: Sunny road 11/2.'),
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

    form.widget('files_working', RelatedItemsWidget)
    files_working = RelationList(
        title=_(u'Working documents'),
        description=_(u'TODO'),
        value_type=RelationChoice(
            title=_(u'Working document'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget('files_information', RelatedItemsWidget)
    files_information = RelationList(
        title=_(u'Information documents'),
        description=_(u'TODO'),
        value_type=RelationChoice(
            title=_(u'Information document'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    form.widget('files_reference', RelatedItemsWidget)
    files_reference = RelationList(
        title=_(u'Reference documents'),
        description=_(u'TODO'),
        value_type=RelationChoice(
            title=_(u'Reference document'),
            vocabulary="plone.app.vocabularies.Catalog",
        ),
        required=False,
    )

    model.fieldset(
        'general',
        label=_(u'General'),
        fields=['start', 'end', 'address', 'meeting_type', 'files_working',
                'files_information', 'files_reference',
                ],
        )

    en_title = schema.TextLine(
        title=_(u'Meeting Name'),
        description=_(u'The name or title of the meeting'),
        required=False,
        )

    en_text = RichText(
        title=_(u'TODO'),
        description=_(u'TODO'),
        required=False,
        )

    model.fieldset(
        'en',
        label=u'English',
        fields=['en_title', 'en_text']
        )

    es_title = schema.TextLine(
        title=u'Title',
        required=False,
        )

    es_text = RichText(
        title=_(u'TODO'),
        description=_(u'TODO'),
        required=False,
        )

    model.fieldset(
        'es',
        label=u"Spanish",
        fields=['es_title', 'es_text']
        )

    fr_title = schema.TextLine(
        title=u'Title',
        required=False,
        )

    fr_text = RichText(
        title=_(u'TODO'),
        description=_(u'TODO'),
        required=False,
        )

    model.fieldset(
        'fr',
        label=u"French",
        fields=['fr_title', 'fr_text']
        )
