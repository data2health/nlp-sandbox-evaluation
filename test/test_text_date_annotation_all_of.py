"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.models.text_date_annotation_all_of import TextDateAnnotationAllOf
from nlpsandbox.models import TextDateAnnotation


class TestTextDateAnnotationAllOf(unittest.TestCase):
    """TextDateAnnotationAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextDateAnnotationAllOf(self):
        """Test TextDateAnnotationAllOf"""
        TextDateAnnotationAllOf(date_format="foo")


if __name__ == '__main__':
    unittest.main()
