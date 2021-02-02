"""
    UnpacMe

     # Introduction Welcome to the UNPACME API! All the malware unpacking and file analysis features that you are familiar with on the [unpac.me](https://www.unpac.me/) website are available through our API. You can easily integrate our unpacker into your malware analysis pipeline and begin unpacking at scale!   # Authentication The public UNPACME API is publicly available and can be accessed without authentication.  In order to use the private UNPACME API you must sign up for an account with UNPACME. Once you have a valid user account you can view your personal API key in your user profile.   <SecurityDefinitions />  # Response Structure When interacting with the UNPACME API, if the request was correctly handled, a <b>200</b> HTTP status code will be returned. The body of the response will usually be a JSON object (except for file downloads).  ## Response Status Codes  Status Code  | Description | Notes ------------- | ------------- | - 200  | OK | The request was successful 400  | Bad Request | The request was somehow incorrect. This can be caused by missing arguments or arguments with wrong values. 401 | Unauthorized | The supplied credentials, if any, are not sufficient to access the resource 403 | Forbidden | The account does not have enough privileges to make the request. 404 | Not Found | The requested resource is not found 429  | Too Many Requests | The request frequency has exceeded one of the account quotas (minute, daily or monthly). Monthly quotas are reset on the 1st of the month at 00:00 UTC. 500 | Server Error | The server could not return the representation due to an internal server error   ## Error Response  If an error has occurred while handling the request an error status code will be returend along with a JSON error message with the following properties.   Property  | Description ------------- | ------------- Error  | The error type Description  | A more informative message  # Example Clients  The following clients can be used to interact with the UNPACME API directly and are provided as examples. These clients are community projects and are not maintained or developed by UNPACME. UNPACME makes no claim as to the safety of these clients, use at your own risk.    - [UnpacMe Python Client](https://github.com/larsborn/UnpacMeClient) (Python)   - [UnpacMe GO Client](https://github.com/kryptoslogic/unpacme-go) (Golang)   - [UnpacMe Library](https://github.com/R3MRUM/unpacme) (Python)   - [AssemblyLine](https://github.com/CybercentreCanada/assemblyline-service-unpacme) (Automation Service)     <br>   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import unpacme
from unpacme.model.deepmatch_entity import DeepmatchEntity
from unpacme.model.malware_id_short import MalwareIdShort
globals()['DeepmatchEntity'] = DeepmatchEntity
globals()['MalwareIdShort'] = MalwareIdShort
from unpacme.model.history_entity import HistoryEntity


class TestHistoryEntity(unittest.TestCase):
    """HistoryEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHistoryEntity(self):
        """Test HistoryEntity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HistoryEntity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
