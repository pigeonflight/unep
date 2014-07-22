API of the meeting product
-------------------------------

These are the most important methods from the old meeting product.
These notes should be a good starting point for migration.

This was lifted from an interactive debug session using:
::

    bin/debug debug

::

    >>> plone = app.sites['new.cep.unep.org'].plone

A meeting contains meeting document collections, some common collection names are "information documents", "working documents" and "reference documents"
::

    >>> infodocs = plone['meetings-events']['14th-igm']['information-documents']
    >>> infodocs2 = plone['meetings-events']['gomeeting']['information documents']
    >>> plone.reference_catalog.lookupObject('6aa82ea3f2148a6565193c819c9ed06c')
    >>> infodocs.getSource_documents()[0].UID()
    >>> infodocs2.setSource_documents(['6aa82ea3f2148a6565193c819c9ed06c',])
    >>> infodocs2.getSource_documents()[0].getBRefs(relationship='meeting_document')
    >>> infodocs2.getSource_documents()[0].getBRelationships()

returns the backreference relationships
::

    >>> infodocs2.getSource_documents()[0].getReferenceMap()
    >>> infodocs2.getSource_documents()[0].getRefs()
    >>> obj = infodocs.getSource_documents()[1]
    >>> infodocs2.getSource_documents()[0].addReference(obj,'meeting_document')
    >>> infodocs2.getDocuments()
