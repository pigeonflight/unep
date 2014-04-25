# -*- coding: utf-8 -*-

from plone.app.testing import TEST_USER_ID, setRoles
from unep.testing import INTEGRATION_TESTING

import unittest2 as unittest


class SetupTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.types = self.portal.portal_types

    def test_that_new_contenttypes_exist(self):
        self.assertEqual(self.types['unep.meeting'].meta_type, 'Dexterity FTI')
        self.assertEqual(self.types['unep.file'].meta_type, 'Dexterity FTI')
        self.assertEqual(
            self.types['unep.filefolder'].meta_type,
            'Dexterity FTI'
        )

    def test_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertTrue(
            '++theme++unep.theme/styles.css' in stylesheets_ids)
