# -*- coding: utf-8 -*-

from plone import api
from Products.CMFPlone.interfaces import constrains


def setupVarious(context):

    if context.readDataFile('unep.marker.txt') is None:
        return

    api.content.delete(api.content.get('/news'))
    api.content.delete(api.content.get('/Members'))
    api.content.delete(api.content.get('/front-page'))
    api.content.delete(api.content.get('/events'))

    portal = api.portal.get()
    
    #check for the existence of meetings and documents
    #
    if not api.content.get('/meetings'):
        meetings = api.content.create(
            portal,
            'Folder',
            id='meetings',
            title='Meetings'
        )
        api.content.transition(meetings, transition='publish')
        behavior = constrains.ISelectableConstrainTypes(meetings)
        behavior.setConstrainTypesMode(constrains.ENABLED)
        behavior.setLocallyAllowedTypes(['unep.meeting', 'Folder'])
        behavior.setImmediatelyAddableTypes(['unep.meeting', 'Folder'])
        
    if not api.content.get('/documents'):
        documents = api.content.create(
            portal,
            'unep.filefolder',
            id='documents',
            title='Documents'
        )

        api.content.transition(documents, transition='publish')
    
