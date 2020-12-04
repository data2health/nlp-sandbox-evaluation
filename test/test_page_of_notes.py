# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import datanodeclient
from datanodeclient.models.page_of_notes import PageOfNotes  # noqa: E501
from datanodeclient.rest import ApiException

class TestPageOfNotes(unittest.TestCase):
    """PageOfNotes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageOfNotes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = datanodeclient.models.page_of_notes.PageOfNotes()  # noqa: E501
        if include_optional :
            return PageOfNotes(
                offset = 56, 
                limit = 56, 
                links = datanodeclient.models.response_page_metadata_links.ResponsePageMetadata_links(
                    next = '0', ), 
                notes = [
                    datanodeclient.models.note.Note(
                        id = '0', 
                        text = 'On 12/26/2020, Ms. Chloe Price met with Dr. Prescott.', 
                        note_type = 'loinc:LP29684-5', 
                        patient_id = '507f1f77bcf86cd799439011', )
                    ]
            )
        else :
            return PageOfNotes(
                offset = 56,
                limit = 56,
                links = datanodeclient.models.response_page_metadata_links.ResponsePageMetadata_links(
                    next = '0', ),
        )

    def testPageOfNotes(self):
        """Test PageOfNotes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()