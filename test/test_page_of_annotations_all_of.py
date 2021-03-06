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
from nlpsandbox.model.annotation import Annotation
from nlpsandbox.model.annotation_name import AnnotationName
from nlpsandbox.model.annotation_source import AnnotationSource
from nlpsandbox.model.resource_source import ResourceSource
from nlpsandbox.model.text_date_annotation import TextDateAnnotation
globals()['Annotation'] = Annotation
from nlpsandbox.model.page_of_annotations_all_of import PageOfAnnotationsAllOf


class TestPageOfAnnotationsAllOf(unittest.TestCase):
    """PageOfAnnotationsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageOfAnnotationsAllOf(self):
        """Test PageOfAnnotationsAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PageOfAnnotationsAllOf()  # noqa: E501
        model = Annotation(
            name=AnnotationName("name"),
            annotation_source=AnnotationSource(resource_source=ResourceSource(name="foo")),
            text_date_annotations=[
                TextDateAnnotation(start=1, length=32, text='foo', confidence=95.5)
            ]
        )
        PageOfAnnotationsAllOf(
            annotations=[model]
        )


if __name__ == '__main__':
    unittest.main()
