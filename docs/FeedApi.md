# unpacme.FeedApi

All URIs are relative to *https://api.unpac.me/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_private_feed**](FeedApi.md#get_private_feed) | **GET** /private/feed/unpacked | Get full unpacked sample feed
[**get_private_feed_yara_filtered**](FeedApi.md#get_private_feed_yara_filtered) | **GET** /private/feed/unpacked/yara/{yara_rule} | Get full unpacked sample feed filtered by yara rule
[**get_private_feed_yara_tags**](FeedApi.md#get_private_feed_yara_tags) | **GET** /private/feed/unpacked/yara | Get list of yara tags in feed


# **get_private_feed**
> PrivateFeed get_private_feed()

Get full unpacked sample feed

Returns full feed of unpacked samples

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import feed_api
from unpacme.model.private_feed import PrivateFeed
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
    api_instance = feed_api.FeedApi(api_client)
    cursor = 1 # int | Scroll feed to cursor (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get full unpacked sample feed
        api_response = api_instance.get_private_feed(cursor=cursor)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling FeedApi->get_private_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| Scroll feed to cursor | [optional]

### Return type

[**PrivateFeed**](PrivateFeed.md)

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

# **get_private_feed_yara_filtered**
> PrivateFeedFiltered get_private_feed_yara_filtered(yara_rule)

Get full unpacked sample feed filtered by yara rule

Returns full feed of unpacked samples filtered by the yara rule

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import feed_api
from unpacme.model.private_feed_filtered import PrivateFeedFiltered
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
    api_instance = feed_api.FeedApi(api_client)
    yara_rule = "yara_rule_example" # str | Yara rule name used to filter feed

    # example passing only required values which don't have defaults set
    try:
        # Get full unpacked sample feed filtered by yara rule
        api_response = api_instance.get_private_feed_yara_filtered(yara_rule)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling FeedApi->get_private_feed_yara_filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yara_rule** | **str**| Yara rule name used to filter feed |

### Return type

[**PrivateFeedFiltered**](PrivateFeedFiltered.md)

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

# **get_private_feed_yara_tags**
> PrivateFeedYaraTags get_private_feed_yara_tags()

Get list of yara tags in feed

Returns list of all yara tags available for the feed

### Example

* Api Key Authentication (api_key):
```python
import time
import unpacme
from unpacme.api import feed_api
from unpacme.model.private_feed_yara_tags import PrivateFeedYaraTags
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
    api_instance = feed_api.FeedApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of yara tags in feed
        api_response = api_instance.get_private_feed_yara_tags()
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling FeedApi->get_private_feed_yara_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrivateFeedYaraTags**](PrivateFeedYaraTags.md)

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

