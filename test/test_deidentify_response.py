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
from nlpsandbox.model.annotation_set import AnnotationSet
from nlpsandbox.model.note import Note
globals()['AnnotationSet'] = AnnotationSet
globals()['Note'] = Note
from nlpsandbox.model.deidentify_response import DeidentifyResponse


class TestDeidentifyResponse(unittest.TestCase):
    """DeidentifyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeidentifyResponse(self):
        """Test DeidentifyResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeidentifyResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
