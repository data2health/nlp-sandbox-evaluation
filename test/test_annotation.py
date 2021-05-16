"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: team@nlpsandbox.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import datanode
from datanode.model.annotation_name import AnnotationName
from datanode.model.annotation_source import AnnotationSource
from datanode.model.text_contact_annotation import TextContactAnnotation
from datanode.model.text_covid_symptom_annotation import TextCovidSymptomAnnotation
from datanode.model.text_date_annotation import TextDateAnnotation
from datanode.model.text_id_annotation import TextIdAnnotation
from datanode.model.text_person_name_annotation import TextPersonNameAnnotation
from datanode.model.text_physical_address_annotation import TextPhysicalAddressAnnotation
globals()['AnnotationName'] = AnnotationName
globals()['AnnotationSource'] = AnnotationSource
globals()['TextContactAnnotation'] = TextContactAnnotation
globals()['TextCovidSymptomAnnotation'] = TextCovidSymptomAnnotation
globals()['TextDateAnnotation'] = TextDateAnnotation
globals()['TextIdAnnotation'] = TextIdAnnotation
globals()['TextPersonNameAnnotation'] = TextPersonNameAnnotation
globals()['TextPhysicalAddressAnnotation'] = TextPhysicalAddressAnnotation
from datanode.model.annotation import Annotation


class TestAnnotation(unittest.TestCase):
    """Annotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnnotation(self):
        """Test Annotation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Annotation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
