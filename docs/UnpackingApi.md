# unpacme.UnpackingApi

All URIs are relative to *https://api.unpac.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_private_download**](UnpackingApi.md#get_private_download) | **GET** /private/download/{sample_hash} | Download sample by hash
[**get_private_history**](UnpackingApi.md#get_private_history) | **GET** /private/history | Get history
[**get_private_results**](UnpackingApi.md#get_private_results) | **GET** /private/results/{unpack_id} | Get unpack results by ID
[**get_private_searchby_hash**](UnpackingApi.md#get_private_searchby_hash) | **GET** /private/search/hash/{sample_hash} | Search for parent submission by hash
[**get_private_unpack_status**](UnpackingApi.md#get_private_unpack_status) | **GET** /private/status/{unpack_id} | Get unpack status by ID
[**post_private_upload**](UnpackingApi.md#post_private_upload) | **POST** /private/upload/ | Submit sample for unpacking


# **get_private_download**
> file_type get_private_download(sample_hash)

Download sample by hash

Downloads sample binary

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    sample_hash = "sample_hash_example" # str | SHA256 hash of sample to download

    # example passing only required values which don't have defaults set
    try:
        # Download sample by hash
        api_response = api_instance.get_private_download(sample_hash)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->get_private_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_hash** | **str**| SHA256 hash of sample to download |

### Return type

**file_type**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_history**
> History get_private_history()

Get history

Returns submission history

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from unpacme.model.history import History
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    cursor = 1 # int | Scroll history to cursor (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get history
        api_response = api_instance.get_private_history(cursor=cursor)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->get_private_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| Scroll history to cursor | [optional]

### Return type

[**History**](History.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_results**
> UnpackResults get_private_results(unpack_id)

Get unpack results by ID

Returns unpack results

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from unpacme.model.unpack_results import UnpackResults
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    unpack_id = "unpack_id_example" # str | ID of unpacking submission

    # example passing only required values which don't have defaults set
    try:
        # Get unpack results by ID
        api_response = api_instance.get_private_results(unpack_id)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->get_private_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unpack_id** | **str**| ID of unpacking submission |

### Return type

[**UnpackResults**](UnpackResults.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_searchby_hash**
> SearchResults get_private_searchby_hash(sample_hash)

Search for parent submission by hash

Returns submission history

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from unpacme.model.search_results import SearchResults
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    sample_hash = "sample_hash_example" # str | SHA256 hash of parent sample

    # example passing only required values which don't have defaults set
    try:
        # Search for parent submission by hash
        api_response = api_instance.get_private_searchby_hash(sample_hash)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->get_private_searchby_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_hash** | **str**| SHA256 hash of parent sample |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_unpack_status**
> UnpackStatus get_private_unpack_status(unpack_id)

Get unpack status by ID

Returns a submission status

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from unpacme.model.unpack_status import UnpackStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    unpack_id = "unpack_id_example" # str | ID of unpacking submission

    # example passing only required values which don't have defaults set
    try:
        # Get unpack status by ID
        api_response = api_instance.get_private_unpack_status(unpack_id)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->get_private_unpack_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unpack_id** | **str**| ID of unpacking submission |

### Return type

[**UnpackStatus**](UnpackStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_private_upload**
> InlineResponse200 post_private_upload()

Submit sample for unpacking

Queues sample for unpacking

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import unpacking_api
from unpacme.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with unpacme.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unpacking_api.UnpackingApi(api_client)
    private = False # bool | Mark sample as private (only available to PRO users) (optional) if omitted the server will use the default value of False
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit sample for unpacking
        api_response = api_instance.post_private_upload(private=private, file=file)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UnpackingApi->post_private_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private** | **bool**| Mark sample as private (only available to PRO users) | [optional] if omitted the server will use the default value of False
 **file** | **file_type**|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data:
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

