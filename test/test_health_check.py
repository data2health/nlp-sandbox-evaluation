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
from nlpsandbox.model.health_check import HealthCheck
from nlpsandbox.model import health_check


class TestHealthCheck(unittest.TestCase):
    """HealthCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHealthCheck(self):
        """Test HealthCheck"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HealthCheck()  # noqa: E501
        HealthCheck(status="pass")
        health_check.HealthCheck(status="pass")


if __name__ == '__main__':
    unittest.main()
