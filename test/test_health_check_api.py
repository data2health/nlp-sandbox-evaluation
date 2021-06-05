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
from nlpsandbox.api.health_check_api import HealthCheckApi  # noqa: E501
from nlpsandbox.api import health_check_api


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = HealthCheckApi()  # noqa: E501
        self.nlpsandbox_api = health_check_api.HealthCheckApi()  # noqa: E501
        self.patcher = patch('nlpsandbox.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()
        self.patcher_f = patch('nlpsandbox.api_client.ApiClient.call_api')
        self.mock_annot = self.patcher_f.start()

    def tearDown(self):
        self.patcher.stop()

    def test_get_health_check(self):
        """Test case for get_health_check

        Get health check information  # noqa: E501
        """
        self.api.get_health_check()

    def test_get_nlpsandbox_health_check(self):
        """Test case for get_health_check

        Get health check information  # noqa: E501
        """
        self.nlpsandbox_api.get_health_check()

if __name__ == '__main__':
    unittest.main()
