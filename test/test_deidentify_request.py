"""
    NLP Sandbox API

    NLP Sandbox REST API  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: team@nlpsandbox.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.model.deidentification_step import DeidentificationStep
from nlpsandbox.model.note import Note
globals()['DeidentificationStep'] = DeidentificationStep
globals()['Note'] = Note
from nlpsandbox.model.deidentify_request import DeidentifyRequest


class TestDeidentifyRequest(unittest.TestCase):
    """DeidentifyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeidentifyRequest(self):
        """Test DeidentifyRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeidentifyRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
