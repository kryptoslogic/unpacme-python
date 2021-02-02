# unpacme.PublicApi

All URIs are relative to *https://api.unpac.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_feed**](PublicApi.md#get_public_feed) | **GET** /public/feed | Get public feed
[**get_public_results**](PublicApi.md#get_public_results) | **GET** /public/results/{unpack_id} | Get unpack results by ID
[**get_public_unpack_status**](PublicApi.md#get_public_unpack_status) | **GET** /public/status/{unpack_id} | Get unpack status by ID


# **get_public_feed**
> PublicFeed get_public_feed()

Get public feed

Returns public feed of unpacked samples

### Example

```python
import time
import unpacme
from unpacme.api import public_api
from unpacme.model.public_feed import PublicFeed
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)


# Enter a context with an instance of the API client
with unpacme.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get public feed
        api_response = api_instance.get_public_feed()
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling PublicApi->get_public_feed: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicFeed**](PublicFeed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_results**
> UnpackResults get_public_results(unpack_id)

Get unpack results by ID

Returns unpack results

### Example

```python
import time
import unpacme
from unpacme.api import public_api
from unpacme.model.unpack_results import UnpackResults
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)


# Enter a context with an instance of the API client
with unpacme.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    unpack_id = "unpack_id_example" # str | ID of unpacking submission

    # example passing only required values which don't have defaults set
    try:
        # Get unpack results by ID
        api_response = api_instance.get_public_results(unpack_id)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling PublicApi->get_public_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unpack_id** | **str**| ID of unpacking submission |

### Return type

[**UnpackResults**](UnpackResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_unpack_status**
> UnpackStatus get_public_unpack_status(unpack_id)

Get unpack status by ID

Returns a submission status

### Example

```python
import time
import unpacme
from unpacme.api import public_api
from unpacme.model.unpack_status import UnpackStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)


# Enter a context with an instance of the API client
with unpacme.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    unpack_id = "unpack_id_example" # str | ID of unpacking submission

    # example passing only required values which don't have defaults set
    try:
        # Get unpack status by ID
        api_response = api_instance.get_public_unpack_status(unpack_id)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling PublicApi->get_public_unpack_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unpack_id** | **str**| ID of unpacking submission |

### Return type

[**UnpackStatus**](UnpackStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

