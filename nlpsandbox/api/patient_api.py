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
from nlpsandbox.model.dataset_id import DatasetId
from nlpsandbox.model.error import Error
from nlpsandbox.model.fhir_store_id import FhirStoreId
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.page_of_patients import PageOfPatients
from nlpsandbox.model.page_offset import PageOffset
from nlpsandbox.model.patient import Patient
from nlpsandbox.model.patient_create_request import PatientCreateRequest
from nlpsandbox.model.patient_create_response import PatientCreateResponse
from nlpsandbox.model.patient_id import PatientId


class PatientApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_patient(
            self,
            dataset_id,
            fhir_store_id,
            patient_id,
            **kwargs
        ):
            """Create a FHIR patient  # noqa: E501

            Create a FHIR patient  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_patient(dataset_id, fhir_store_id, patient_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store
                patient_id (PatientId): The ID of the patient that is being created

            Keyword Args:
                patient_create_request (PatientCreateRequest): [optional]
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
                PatientCreateResponse
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
            kwargs['patient_id'] = \
                patient_id
            return self.call_with_http_info(**kwargs)

        self.create_patient = _Endpoint(
            settings={
                'response_type': (PatientCreateResponse,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient',
                'operation_id': 'create_patient',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
                    'patient_create_request',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
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
                    'patient_id':
                        (PatientId,),
                    'patient_create_request':
                        (PatientCreateRequest,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                    'patient_id': 'patientId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
                    'patient_id': 'query',
                    'patient_create_request': 'body',
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
            callable=__create_patient
        )

        def __delete_patient(
            self,
            dataset_id,
            fhir_store_id,
            patient_id,
            **kwargs
        ):
            """Delete a FHIR patient  # noqa: E501

            Deletes the FHIR patient specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_patient(dataset_id, fhir_store_id, patient_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store
                patient_id (PatientId): The ID of the FHIR patient

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
            kwargs['patient_id'] = \
                patient_id
            return self.call_with_http_info(**kwargs)

        self.delete_patient = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId}',
                'operation_id': 'delete_patient',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
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
                    'patient_id':
                        (PatientId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                    'patient_id': 'patientId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
                    'patient_id': 'path',
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
            callable=__delete_patient
        )

        def __get_patient(
            self,
            dataset_id,
            fhir_store_id,
            patient_id,
            **kwargs
        ):
            """Get a FHIR patient  # noqa: E501

            Returns the FHIR patient specified  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_patient(dataset_id, fhir_store_id, patient_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store
                patient_id (PatientId): The ID of the FHIR patient

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
                Patient
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
            kwargs['patient_id'] = \
                patient_id
            return self.call_with_http_info(**kwargs)

        self.get_patient = _Endpoint(
            settings={
                'response_type': (Patient,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient/{patientId}',
                'operation_id': 'get_patient',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
                ],
                'required': [
                    'dataset_id',
                    'fhir_store_id',
                    'patient_id',
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
                    'patient_id':
                        (PatientId,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                    'patient_id': 'patientId',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
                    'patient_id': 'path',
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
            callable=__get_patient
        )

        def __list_patients(
            self,
            dataset_id,
            fhir_store_id,
            **kwargs
        ):
            """List the Patients in a FHIR store  # noqa: E501

            Returns the Patients in a FHIR store  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_patients(dataset_id, fhir_store_id, async_req=True)
            >>> result = thread.get()

            Args:
                dataset_id (DatasetId): The ID of the dataset
                fhir_store_id (FhirStoreId): The ID of the FHIR store

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
                PageOfPatients
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

        self.list_patients = _Endpoint(
            settings={
                'response_type': (PageOfPatients,),
                'auth': [],
                'endpoint_path': '/datasets/{datasetId}/fhirStores/{fhirStoreId}/fhir/Patient',
                'operation_id': 'list_patients',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'fhir_store_id',
                    'limit',
                    'offset',
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
                    'limit':
                        (PageLimit,),
                    'offset':
                        (PageOffset,),
                },
                'attribute_map': {
                    'dataset_id': 'datasetId',
                    'fhir_store_id': 'fhirStoreId',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'dataset_id': 'path',
                    'fhir_store_id': 'path',
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
            callable=__list_patients
        )
