"""
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
"""

import unittest
import HtmlTestRunner

from Curs_9.tema_9 import Login
from Curs_10.alerts import Alerts
from Curs_10.auth import Authentication
from Curs_10.context_menu import ContextMenu
from Curs_10.key_press import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):

        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            # unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            # unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='My Report Name 2',
            report_title='My First Report Title'
        )

        runner.run(test_to_run)
