# unpacme.UserApi

All URIs are relative to *https://api.unpac.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_private_user_malpedia**](UserApi.md#delete_private_user_malpedia) | **DELETE** /private/user/malpedia | Remove Malpedia authentication
[**get_private_user_access**](UserApi.md#get_private_user_access) | **GET** /private/user/access | Get user settings
[**get_private_user_malpedia**](UserApi.md#get_private_user_malpedia) | **GET** /private/user/malpedia | Get user Malpedia info
[**post_private_user_malpedia**](UserApi.md#post_private_user_malpedia) | **POST** /private/user/malpedia | Authenticate user to Malpedia


# **delete_private_user_malpedia**
> delete_private_user_malpedia()

Remove Malpedia authentication

Removes Malpedia authentication and deletes Malpedia token

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Remove Malpedia authentication
        api_instance.delete_private_user_malpedia()
    except unpacme.ApiException as e:
        print("Exception when calling UserApi->delete_private_user_malpedia: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_user_access**
> UserAccess get_private_user_access()

Get user settings

Returns user settings

### Example

```python
import time
import unpacme
from unpacme.api import user_api
from unpacme.model.user_access import UserAccess
from pprint import pprint
# Defining the host is optional and defaults to https://api.unpac.me/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unpacme.Configuration(
    host = "https://api.unpac.me/api/v1"
)


# Enter a context with an instance of the API client
with unpacme.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user settings
        api_response = api_instance.get_private_user_access()
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UserApi->get_private_user_access: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAccess**](UserAccess.md)

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

# **get_private_user_malpedia**
> InlineResponse2001 get_private_user_malpedia()

Get user Malpedia info

Returns user Malpedia info

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import user_api
from unpacme.model.inline_response2001 import InlineResponse2001
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user Malpedia info
        api_response = api_instance.get_private_user_malpedia()
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling UserApi->get_private_user_malpedia: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **post_private_user_malpedia**
> post_private_user_malpedia()

Authenticate user to Malpedia

Authenticate user to Malpedia using API token

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import user_api
from unpacme.model.inline_object1 import InlineObject1
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
    api_instance = user_api.UserApi(api_client)
    inline_object1 = InlineObject1(
        token="token_example",
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authenticate user to Malpedia
        api_instance.post_private_user_malpedia(inline_object1=inline_object1)
    except unpacme.ApiException as e:
        print("Exception when calling UserApi->post_private_user_malpedia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

