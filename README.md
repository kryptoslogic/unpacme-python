# unpacme

# Introduction
Welcome to the UNPACME API! All the malware unpacking and file analysis features that you are familiar with on the [unpac.me](https://www.unpac.me/) website are available through our API. You can easily integrate our unpacker into your malware analysis pipeline and begin unpacking at scale!


# Authentication
The public UNPACME API is publicly available and can be accessed without authentication.

In order to use the private UNPACME API you must sign up for an account with UNPACME. Once you have a valid user account you can view your personal API key in your user profile. 

<SecurityDefinitions />

# Response Structure
When interacting with the UNPACME API, if the request was correctly handled, a <b>200</b> HTTP status code will be returned. The body of the response will usually be a JSON object (except for file downloads).

## Response Status Codes

Status Code  | Description | Notes
------------- | ------------- | -
200  | OK | The request was successful
400  | Bad Request | The request was somehow incorrect. This can be caused by missing arguments or arguments with wrong values.
401 | Unauthorized | The supplied credentials, if any, are not sufficient to access the resource
403 | Forbidden | The account does not have enough privileges to make the request.
404 | Not Found | The requested resource is not found
429  | Too Many Requests | The request frequency has exceeded one of the account quotas (minute, daily or monthly). Monthly quotas are reset on the 1st of the month at 00:00 UTC.
500 | Server Error | The server could not return the representation due to an internal server error


## Error Response

If an error has occurred while handling the request an error status code will be returend along with a JSON error message with the following properties.


Property  | Description
------------- | -------------
Error  | The error type
Description  | A more informative message

# Example Clients

The following clients can be used to interact with the UNPACME API directly and are provided as examples. These clients are community projects and are not maintained or developed by UNPACME. UNPACME makes no claim as to the safety of these clients, use at your own risk.

  - [UnpacMe Python Client](https://github.com/larsborn/UnpacMeClient) (Python)
  - [UnpacMe GO Client](https://github.com/kryptoslogic/unpacme-go) (Golang)
  - [UnpacMe Library](https://github.com/R3MRUM/unpacme) (Python)
  - [AssemblyLine](https://github.com/CybercentreCanada/assemblyline-service-unpacme) (Automation Service)
  

<br>


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install unpacme
```
(you may need to run `pip` with root permission: `sudo pip install unpacme`)

Then import the package:
```python
import unpacme
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import unpacme
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import unpacme
from pprint import pprint
from unpacme.api import feed_api
from unpacme.model.private_feed import PrivateFeed
from unpacme.model.private_feed_filtered import PrivateFeedFiltered
from unpacme.model.private_feed_yara_tags import PrivateFeedYaraTags
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

    try:
        # Get full unpacked sample feed
        api_response = api_instance.get_private_feed(cursor=cursor)
        pprint(api_response)
    except unpacme.ApiException as e:
        print("Exception when calling FeedApi->get_private_feed: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.unpac.me/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FeedApi* | [**get_private_feed**](docs/FeedApi.md#get_private_feed) | **GET** /private/feed/unpacked | Get full unpacked sample feed
*FeedApi* | [**get_private_feed_yara_filtered**](docs/FeedApi.md#get_private_feed_yara_filtered) | **GET** /private/feed/unpacked/yara/{yara_rule} | Get full unpacked sample feed filtered by yara rule
*FeedApi* | [**get_private_feed_yara_tags**](docs/FeedApi.md#get_private_feed_yara_tags) | **GET** /private/feed/unpacked/yara | Get list of yara tags in feed
*PublicApi* | [**get_public_feed**](docs/PublicApi.md#get_public_feed) | **GET** /public/feed | Get public feed
*PublicApi* | [**get_public_results**](docs/PublicApi.md#get_public_results) | **GET** /public/results/{unpack_id} | Get unpack results by ID
*PublicApi* | [**get_public_unpack_status**](docs/PublicApi.md#get_public_unpack_status) | **GET** /public/status/{unpack_id} | Get unpack status by ID
*UnpackingApi* | [**get_private_download**](docs/UnpackingApi.md#get_private_download) | **GET** /private/download/{sample_hash} | Download sample by hash
*UnpackingApi* | [**get_private_history**](docs/UnpackingApi.md#get_private_history) | **GET** /private/history | Get history
*UnpackingApi* | [**get_private_results**](docs/UnpackingApi.md#get_private_results) | **GET** /private/results/{unpack_id} | Get unpack results by ID
*UnpackingApi* | [**get_private_searchby_hash**](docs/UnpackingApi.md#get_private_searchby_hash) | **GET** /private/search/hash/{sample_hash} | Search for parent submission by hash
*UnpackingApi* | [**get_private_unpack_status**](docs/UnpackingApi.md#get_private_unpack_status) | **GET** /private/status/{unpack_id} | Get unpack status by ID
*UnpackingApi* | [**post_private_upload**](docs/UnpackingApi.md#post_private_upload) | **POST** /private/upload/ | Submit sample for unpacking
*UserApi* | [**delete_private_user_malpedia**](docs/UserApi.md#delete_private_user_malpedia) | **DELETE** /private/user/malpedia | Remove Malpedia authentication
*UserApi* | [**get_private_user_access**](docs/UserApi.md#get_private_user_access) | **GET** /private/user/access | Get user settings
*UserApi* | [**get_private_user_malpedia**](docs/UserApi.md#get_private_user_malpedia) | **GET** /private/user/malpedia | Get user Malpedia info
*UserApi* | [**post_private_user_malpedia**](docs/UserApi.md#post_private_user_malpedia) | **POST** /private/user/malpedia | Authenticate user to Malpedia


## Documentation For Models

 - [DeepmatchEntity](docs/DeepmatchEntity.md)
 - [DeepmatchEntityAllOf](docs/DeepmatchEntityAllOf.md)
 - [DetectitEntity](docs/DetectitEntity.md)
 - [DetectitEntityAllOf](docs/DetectitEntityAllOf.md)
 - [Export](docs/Export.md)
 - [ExportAllOf](docs/ExportAllOf.md)
 - [FeedEntity](docs/FeedEntity.md)
 - [Function](docs/Function.md)
 - [FunctionAllOf](docs/FunctionAllOf.md)
 - [History](docs/History.md)
 - [HistoryEntity](docs/HistoryEntity.md)
 - [ImportEntity](docs/ImportEntity.md)
 - [ImportEntityAllOf](docs/ImportEntityAllOf.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [MalwareId](docs/MalwareId.md)
 - [MalwareIdAllOf](docs/MalwareIdAllOf.md)
 - [MalwareIdShort](docs/MalwareIdShort.md)
 - [MalwareIdShortAllOf](docs/MalwareIdShortAllOf.md)
 - [PrivateFeed](docs/PrivateFeed.md)
 - [PrivateFeedEntity](docs/PrivateFeedEntity.md)
 - [PrivateFeedEntityChildren](docs/PrivateFeedEntityChildren.md)
 - [PrivateFeedFiltered](docs/PrivateFeedFiltered.md)
 - [PrivateFeedYaraTags](docs/PrivateFeedYaraTags.md)
 - [PublicFeed](docs/PublicFeed.md)
 - [Resource](docs/Resource.md)
 - [ResourceAllOf](docs/ResourceAllOf.md)
 - [ResourceEntity](docs/ResourceEntity.md)
 - [ResourceEntry](docs/ResourceEntry.md)
 - [Result](docs/Result.md)
 - [ResultAllOf](docs/ResultAllOf.md)
 - [ResultAllOfAnalysis](docs/ResultAllOfAnalysis.md)
 - [ResultAllOfAnalysisExports](docs/ResultAllOfAnalysisExports.md)
 - [ResultAllOfAnalysisImports](docs/ResultAllOfAnalysisImports.md)
 - [ResultAllOfAnalysisMetadata](docs/ResultAllOfAnalysisMetadata.md)
 - [ResultAllOfAnalysisMetadataVersionInfo](docs/ResultAllOfAnalysisMetadataVersionInfo.md)
 - [ResultAllOfAnalysisMetadataVersionInfoStringInfo](docs/ResultAllOfAnalysisMetadataVersionInfoStringInfo.md)
 - [ResultAllOfAnalysisMetadataVersionInfoVarInfo](docs/ResultAllOfAnalysisMetadataVersionInfoVarInfo.md)
 - [ResultAllOfAnalysisRichHeaders](docs/ResultAllOfAnalysisRichHeaders.md)
 - [ResultAllOfHashes](docs/ResultAllOfHashes.md)
 - [ResultAllOfStrings](docs/ResultAllOfStrings.md)
 - [RichHeader](docs/RichHeader.md)
 - [RichHeaderAllOf](docs/RichHeaderAllOf.md)
 - [SearchEntity](docs/SearchEntity.md)
 - [SearchResults](docs/SearchResults.md)
 - [Section](docs/Section.md)
 - [SectionAllOf](docs/SectionAllOf.md)
 - [Status](docs/Status.md)
 - [UnpackResults](docs/UnpackResults.md)
 - [UnpackResultsAllOf](docs/UnpackResultsAllOf.md)
 - [UnpackStatus](docs/UnpackStatus.md)
 - [UnpackStatusAllOf](docs/UnpackStatusAllOf.md)
 - [UserAccess](docs/UserAccess.md)
 - [UserAccessAllOf](docs/UserAccessAllOf.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in unpacme.apis and unpacme.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from unpacme.api.default_api import DefaultApi`
- `from unpacme.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import unpacme
from unpacme.apis import *
from unpacme.models import *
```

