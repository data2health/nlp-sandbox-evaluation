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
from nlpsandbox.models.note import Note
from nlpsandbox.models import NoteId, PatientId
globals()['Note'] = Note
from nlpsandbox.models.text_person_name_annotation_request import TextPersonNameAnnotationRequest


class TestTextPersonNameAnnotationRequest(unittest.TestCase):
    """TextPersonNameAnnotationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextPersonNameAnnotationRequest(self):
        """Test TextPersonNameAnnotationRequest"""
        TextPersonNameAnnotationRequest(
            note=Note(
                identifier=NoteId("identifier"),
                text="text", type="type",
                patient_id=PatientId('patient-1')
            )
        )


if __name__ == '__main__':
    unittest.main()
