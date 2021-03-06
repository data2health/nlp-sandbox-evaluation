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
from nlpsandbox.model.annotation_store import AnnotationStore
from nlpsandbox.models import AnnotationStoreName
globals()['AnnotationStore'] = AnnotationStore
from nlpsandbox.model.page_of_annotation_stores_all_of import PageOfAnnotationStoresAllOf


class TestPageOfAnnotationStoresAllOf(unittest.TestCase):
    """PageOfAnnotationStoresAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageOfAnnotationStoresAllOf(self):
        """Test PageOfAnnotationStoresAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PageOfAnnotationStoresAllOf()  # noqa: E501
        PageOfAnnotationStoresAllOf(
            annotation_stores=[AnnotationStore(name=AnnotationStoreName("name"))]
        )


if __name__ == '__main__':
    unittest.main()
