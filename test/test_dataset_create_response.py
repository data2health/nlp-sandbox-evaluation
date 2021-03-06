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
from nlpsandbox.model.dataset_name import DatasetName
globals()['DatasetName'] = DatasetName
from nlpsandbox.model.dataset_create_response import DatasetCreateResponse


class TestDatasetCreateResponse(unittest.TestCase):
    """DatasetCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatasetCreateResponse(self):
        """Test DatasetCreateResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DatasetCreateResponse()  # noqa: E501
        model = DatasetCreateResponse(name=DatasetName("name"))


if __name__ == '__main__':
    unittest.main()
