"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.models.note import Note
globals()['Note'] = Note
from nlpsandbox.models.text_id_annotation_request import TextIdAnnotationRequest


class TestTextIdAnnotationRequest(unittest.TestCase):
    """TextIdAnnotationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextIdAnnotationRequest(self):
        """Test TextIdAnnotationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TextIdAnnotationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
