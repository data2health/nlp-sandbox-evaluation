"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import annotator
from annotator.api.text_contact_annotation_api import TextContactAnnotationApi  # noqa: E501


class TestTextContactAnnotationApi(unittest.TestCase):
    """TextContactAnnotationApi unit test stubs"""

    def setUp(self):
        self.api = TextContactAnnotationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_text_contact_annotations(self):
        """Test case for create_text_contact_annotations

        Annotate contact information in a clinical note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()