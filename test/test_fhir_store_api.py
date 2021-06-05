"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest
from unittest.mock import patch

import nlpsandbox
from nlpsandbox.apis.fhir_store_api import FhirStoreApi  # noqa: E501


class TestFhirStoreApi(unittest.TestCase):
    """FhirStoreApi unit test stubs"""

    def setUp(self):
        self.api = FhirStoreApi()  # noqa: E501
        self.patcher = patch('nlpsandbox.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create_fhir_store(self):
        """Test case for create_fhir_store

        Create a FHIR store  # noqa: E501
        """
        self.apis.create_fhir_store(
            dataset_id="awesome-dataset",
            fhir_store_id="awesome-fhir-store",
            body={}
        )

    def test_delete_fhir_store(self):
        """Test case for delete_fhir_store

        Delete a FHIR store  # noqa: E501
        """
        self.apis.delete_fhir_store(
            dataset_id="awesome-dataset",
            fhir_store_id="awesome-fhir-store",
        )

    def test_get_fhir_store(self):
        """Test case for get_fhir_store

        Get a FHIR store  # noqa: E501
        """
        self.apis.get_fhir_store(
            dataset_id="awesome-dataset",
            fhir_store_id="awesome-fhir-store",
        )

    def test_list_fhir_stores(self):
        """Test case for list_fhir_stores

        List the FHIR stores in a dataset  # noqa: E501
        """
        self.apis.list_fhir_stores(dataset_id="awesome-dataset")


if __name__ == '__main__':
    unittest.main()
