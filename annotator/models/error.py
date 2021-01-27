# coding: utf-8

"""
    NLP Sandbox Date Annotator API

    The OpenAPI specification implemented by NLP Sandbox Date Annotators. # Overview This NLP tool detects date references in the clinical note specified and returns a list of date annotations.   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from annotator.configuration import Configuration


class Error(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'type': 'type'
    }

    def __init__(self, title=None, status=None, detail=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._status = None
        self._detail = None
        self._type = None
        self.discriminator = None

        self.title = title
        self.status = status
        if detail is not None:
            self.detail = detail
        if type is not None:
            self.type = type

    @property
    def title(self):
        """Gets the title of this Error.  # noqa: E501

        A human readable documentation for the problem type  # noqa: E501

        :return: The title of this Error.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error.

        A human readable documentation for the problem type  # noqa: E501

        :param title: The title of this Error.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501

        The HTTP status code  # noqa: E501

        :return: The status of this Error.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.

        The HTTP status code  # noqa: E501

        :param status: The status of this Error.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this Error.  # noqa: E501

        A human readable explanation specific to this occurrence of the problem  # noqa: E501

        :return: The detail of this Error.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        A human readable explanation specific to this occurrence of the problem  # noqa: E501

        :param detail: The detail of this Error.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def type(self):
        """Gets the type of this Error.  # noqa: E501

        An absolute URI that identifies the problem type  # noqa: E501

        :return: The type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error.

        An absolute URI that identifies the problem type  # noqa: E501

        :param type: The type of this Error.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
