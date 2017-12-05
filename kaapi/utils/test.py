"""Testing utilities for Kaapi."""

from kaapi.cli.main import KaapiTestApp
from cement.utils.test import *

class KaapiTestCase(CementTestCase):
    app_class = KaapiTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(KaapiTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(KaapiTestCase, self).tearDown()

