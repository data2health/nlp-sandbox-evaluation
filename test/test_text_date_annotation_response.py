"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.model.text_date_annotation import TextDateAnnotation
globals()['TextDateAnnotation'] = TextDateAnnotation
from nlpsandbox.model.text_date_annotation_response import TextDateAnnotationResponse


class TestTextDateAnnotationResponse(unittest.TestCase):
    """TextDateAnnotationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextDateAnnotationResponse(self):
        """Test TextDateAnnotationResponse"""
        TextDateAnnotationResponse(
            text_date_annotations=[
                TextDateAnnotation(start=10, length=10, text="foobar", confidence=95.5)
            ]
        )


if __name__ == '__main__':
    unittest.main()
