"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: team@nlpsandbox.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from datanode.api_client import ApiClient, Endpoint as _Endpoint
from datanode.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from datanode.model.dataset_id import DatasetId
from datanode.model.error import Error
from datanode.model.fhir_store import FhirStore
from datanode.model.fhir_store_create_response import FhirStoreCreateResponse
from datanode.model.fhir_store_id import FhirStoreId
from datanode.model.page_limit import PageLimit
from datanode.model.page_of_fhir_stores import PageOfFhirStores
from datanode.model.page_offset import PageOffset


class FhirStoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_fhir_store(
            self,
            dataset_id,
            fhir_store_id,
            **kwargs
        ):
            """Create a FHIR store  # noqa: E501

            Create a FHIR store with the ID specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_fhir_store(dataset_id, fhir_store_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store that is being created.

            Keyword Args:
                body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FhirStoreCreateResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dataset_id'] = \
                dataset_id
            kwargs['fhir_store_id'] = \
                fhir_store_id
            return self.call_with_http_info(**kwargs)

        self.create_fhir_store = _Endpoint(
            settings={
                'response_type': (FhirStoreCreateResponse,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores',
                'operation_id': 'create_fhir_store',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                    'body',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dataset_id':
                        (DatasetId,),
                    'fhir_store_id':
                        (FhirStoreId,),
                    'body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_fhir_store
        )

        def __delete_fhir_store(
            self,
            dataset_id,
            fhir_store_id,
            **kwargs
        ):
            """Delete a FHIR store  # noqa: E501

            Deletes the FHIR store specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_fhir_store(dataset_id, fhir_store_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dataset_id'] = \
                dataset_id
            kwargs['fhir_store_id'] = \
                fhir_store_id
            return self.call_with_http_info(**kwargs)

        self.delete_fhir_store = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}',
                'operation_id': 'delete_fhir_store',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dataset_id':
                        (DatasetId,),
                    'fhir_store_id':
                        (FhirStoreId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_fhir_store
        )

        def __get_fhir_store(
            self,
            dataset_id,
            fhir_store_id,
            **kwargs
        ):
            """Get a FHIR store  # noqa: E501

            Returns the FHIR store specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_fhir_store(dataset_id, fhir_store_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FhirStore
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dataset_id'] = \
                dataset_id
            kwargs['fhir_store_id'] = \
                fhir_store_id
            return self.call_with_http_info(**kwargs)

        self.get_fhir_store = _Endpoint(
            settings={
                'response_type': (FhirStore,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}',
                'operation_id': 'get_fhir_store',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dataset_id':
                        (DatasetId,),
                    'fhir_store_id':
                        (FhirStoreId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_fhir_store
        )

        def __list_fhir_stores(
            self,
            dataset_id,
            **kwargs
        ):
            """List the FHIR stores in a dataset  # noqa: E501

            Returns the FHIR stores  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_fhir_stores(dataset_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset

            Keyword Args:
                limit (PageLimit): Maximum number of results returned. [optional]
                offset (PageOffset): Index of the first result that must be returned. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PageOfFhirStores
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dataset_id'] = \
                dataset_id
            return self.call_with_http_info(**kwargs)

        self.list_fhir_stores = _Endpoint(
            settings={
                'response_type': (PageOfFhirStores,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores',
                'operation_id': 'list_fhir_stores',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'limit',
                    'offset',
                ],
                'required': [
                    'dataset_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dataset_id':
                        (DatasetId,),
                    'limit':
                        (PageLimit,),
                    'offset':
                        (PageOffset,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_fhir_stores
        )
