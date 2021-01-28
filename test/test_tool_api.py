# coding: utf-8

"""
    NLP Sandbox Date Annotator API

    The OpenAPI specification implemented by NLP Sandbox Date Annotators. # Overview This NLP tool detects date references in the clinical note specified and returns a list of date annotations.   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import annotator
from annotator.api.tool_api import ToolApi  # noqa: E501
from annotator.rest import ApiException


class TestToolApi(unittest.TestCase):
    """ToolApi unit test stubs"""

    def setUp(self):
        self.api = annotator.api.tool_api.ToolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_tool(self):
        """Test case for get_tool

        Get tool information  # noqa: E501
        """
        pass

    def test_get_tool_dependencies(self):
        """Test case for get_tool_dependencies

        Get tool dependencies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()