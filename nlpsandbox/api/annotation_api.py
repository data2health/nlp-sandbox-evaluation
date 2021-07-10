"""
    NLP Sandbox API

    NLP Sandbox REST API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: team@nlpsandbox.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from nlpsandbox.api_client import ApiClient, Endpoint as _Endpoint
from nlpsandbox.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from nlpsandbox.model.annotation import Annotation
from nlpsandbox.model.annotation_create_request import AnnotationCreateRequest
from nlpsandbox.model.annotation_create_response import AnnotationCreateResponse
from nlpsandbox.model.annotation_id import AnnotationId
from nlpsandbox.model.annotation_store_id import AnnotationStoreId
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.error import Error
from nlpsandbox.model.fhir_store_id import FhirStoreId
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.page_of_annotations import PageOfAnnotations
from nlpsandbox.model.page_offset import PageOffset


class AnnotationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_annotation(
            self,
            dataset_id,
            annotation_store_id,
            annotation_id,
            **kwargs
        ):
            """Create an annotation  # noqa: E501

            Create an annotation  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_annotation(dataset_id, annotation_store_id, annotation_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                annotation_store_id (AnnotationStoreId): The ID of the annotation store
                annotation_id (AnnotationId): The ID of the annotation that is being created

            Keyword Args:
                annotation_create_request (AnnotationCreateRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
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
                AnnotationCreateResponse
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
            kwargs['annotation_store_id'] = \
                annotation_store_id
            kwargs['annotation_id'] = \
                annotation_id
            return self.call_with_http_info(**kwargs)

        self.create_annotation = _Endpoint(
            settings={
                'response_type': (AnnotationCreateResponse,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations',
                'operation_id': 'create_annotation',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
                    'annotation_create_request',
                ],
                'required': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
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
                    'annotation_store_id':
                        (AnnotationStoreId,),
                    'annotation_id':
                        (AnnotationId,),
                    'annotation_create_request':
                        (AnnotationCreateRequest,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'annotation_store_id': 'annotationStoreId',
                    'annotation_id': 'annotationId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'annotation_store_id': 'path',
                    'annotation_id': 'query',
                    'annotation_create_request': 'body',
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
            callable=__create_annotation
        )

        def __delete_annotation(
            self,
            dataset_id,
            annotation_store_id,
            annotation_id,
            **kwargs
        ):
            """Delete an annotation  # noqa: E501

            Deletes the annotation specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_annotation(dataset_id, annotation_store_id, annotation_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                annotation_store_id (FhirStoreId): The ID of the annotation store
                annotation_id (AnnotationId): The ID of the annotation

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
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
            kwargs['annotation_store_id'] = \
                annotation_store_id
            kwargs['annotation_id'] = \
                annotation_id
            return self.call_with_http_info(**kwargs)

        self.delete_annotation = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId}',
                'operation_id': 'delete_annotation',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
                ],
                'required': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
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
                    'annotation_store_id':
                        (FhirStoreId,),
                    'annotation_id':
                        (AnnotationId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'annotation_store_id': 'annotationStoreId',
                    'annotation_id': 'annotationId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'annotation_store_id': 'path',
                    'annotation_id': 'path',
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
            callable=__delete_annotation
        )

        def __get_annotation(
            self,
            dataset_id,
            annotation_store_id,
            annotation_id,
            **kwargs
        ):
            """Get an annotation  # noqa: E501

            Returns the annotation specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_annotation(dataset_id, annotation_store_id, annotation_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                annotation_store_id (FhirStoreId): The ID of the annotation store
                annotation_id (AnnotationId): The ID of the annotation

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
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
                Annotation
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
            kwargs['annotation_store_id'] = \
                annotation_store_id
            kwargs['annotation_id'] = \
                annotation_id
            return self.call_with_http_info(**kwargs)

        self.get_annotation = _Endpoint(
            settings={
                'response_type': (Annotation,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId}',
                'operation_id': 'get_annotation',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
                ],
                'required': [
                    'dataset_id',
                    'annotation_store_id',
                    'annotation_id',
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
                    'annotation_store_id':
                        (FhirStoreId,),
                    'annotation_id':
                        (AnnotationId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'annotation_store_id': 'annotationStoreId',
                    'annotation_id': 'annotationId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'annotation_store_id': 'path',
                    'annotation_id': 'path',
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
            callable=__get_annotation
        )

        def __list_annotations(
            self,
            dataset_id,
            annotation_store_id,
            **kwargs
        ):
            """List the annotations in an annotation store  # noqa: E501

            Returns the annotations in an annotation store  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_annotations(dataset_id, annotation_store_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                annotation_store_id (AnnotationStoreId): The ID of the annotation store

            Keyword Args:
                limit (PageLimit): Maximum number of results returned. [optional]
                offset (PageOffset): Index of the first result that must be returned. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
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
                PageOfAnnotations
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
            kwargs['annotation_store_id'] = \
                annotation_store_id
            return self.call_with_http_info(**kwargs)

        self.list_annotations = _Endpoint(
            settings={
                'response_type': (PageOfAnnotations,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations',
                'operation_id': 'list_annotations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'annotation_store_id',
                    'limit',
                    'offset',
                ],
                'required': [
                    'dataset_id',
                    'annotation_store_id',
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
                    'annotation_store_id':
                        (AnnotationStoreId,),
                    'limit':
                        (PageLimit,),
                    'offset':
                        (PageOffset,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'annotation_store_id': 'annotationStoreId',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'annotation_store_id': 'path',
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
            callable=__list_annotations
        )
