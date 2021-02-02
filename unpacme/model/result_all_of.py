"""
    UnpacMe

     # Introduction Welcome to the UNPACME API! All the malware unpacking and file analysis features that you are familiar with on the [unpac.me](https://www.unpac.me/) website are available through our API. You can easily integrate our unpacker into your malware analysis pipeline and begin unpacking at scale!   # Authentication The public UNPACME API is publicly available and can be accessed without authentication.  In order to use the private UNPACME API you must sign up for an account with UNPACME. Once you have a valid user account you can view your personal API key in your user profile.   <SecurityDefinitions />  # Response Structure When interacting with the UNPACME API, if the request was correctly handled, a <b>200</b> HTTP status code will be returned. The body of the response will usually be a JSON object (except for file downloads).  ## Response Status Codes  Status Code  | Description | Notes ------------- | ------------- | - 200  | OK | The request was successful 400  | Bad Request | The request was somehow incorrect. This can be caused by missing arguments or arguments with wrong values. 401 | Unauthorized | The supplied credentials, if any, are not sufficient to access the resource 403 | Forbidden | The account does not have enough privileges to make the request. 404 | Not Found | The requested resource is not found 429  | Too Many Requests | The request frequency has exceeded one of the account quotas (minute, daily or monthly). Monthly quotas are reset on the 1st of the month at 00:00 UTC. 500 | Server Error | The server could not return the representation due to an internal server error   ## Error Response  If an error has occurred while handling the request an error status code will be returend along with a JSON error message with the following properties.   Property  | Description ------------- | ------------- Error  | The error type Description  | A more informative message  # Example Clients  The following clients can be used to interact with the UNPACME API directly and are provided as examples. These clients are community projects and are not maintained or developed by UNPACME. UNPACME makes no claim as to the safety of these clients, use at your own risk.    - [UnpacMe Python Client](https://github.com/larsborn/UnpacMeClient) (Python)   - [UnpacMe GO Client](https://github.com/kryptoslogic/unpacme-go) (Golang)   - [UnpacMe Library](https://github.com/R3MRUM/unpacme) (Python)   - [AssemblyLine](https://github.com/CybercentreCanada/assemblyline-service-unpacme) (Automation Service)     <br>   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from unpacme.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from unpacme.model.deepmatch_entity import DeepmatchEntity
    from unpacme.model.detectit_entity import DetectitEntity
    from unpacme.model.malware_id import MalwareId
    from unpacme.model.result_all_of_analysis import ResultAllOfAnalysis
    from unpacme.model.result_all_of_hashes import ResultAllOfHashes
    from unpacme.model.result_all_of_strings import ResultAllOfStrings
    globals()['DeepmatchEntity'] = DeepmatchEntity
    globals()['DetectitEntity'] = DetectitEntity
    globals()['MalwareId'] = MalwareId
    globals()['ResultAllOfAnalysis'] = ResultAllOfAnalysis
    globals()['ResultAllOfHashes'] = ResultAllOfHashes
    globals()['ResultAllOfStrings'] = ResultAllOfStrings


class ResultAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'hashes': (ResultAllOfHashes,),  # noqa: E501
            'analysis': (ResultAllOfAnalysis,),  # noqa: E501
            'deepmatch': ([DeepmatchEntity],),  # noqa: E501
            'detectit': ([DetectitEntity],),  # noqa: E501
            'malware_id': ([MalwareId],),  # noqa: E501
            'malware_id_restricted': ([MalwareId],),  # noqa: E501
            'strings': (ResultAllOfStrings,),  # noqa: E501
            'urls': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'hashes': 'hashes',  # noqa: E501
        'analysis': 'analysis',  # noqa: E501
        'deepmatch': 'deepmatch',  # noqa: E501
        'detectit': 'detectit',  # noqa: E501
        'malware_id': 'malware_id',  # noqa: E501
        'malware_id_restricted': 'malware_id_restricted',  # noqa: E501
        'strings': 'strings',  # noqa: E501
        'urls': 'urls',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, hashes, analysis, *args, **kwargs):  # noqa: E501
        """ResultAllOf - a model defined in OpenAPI

        Args:
            hashes (ResultAllOfHashes):
            analysis (ResultAllOfAnalysis):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            deepmatch ([DeepmatchEntity]): [optional]  # noqa: E501
            detectit ([DetectitEntity]): [optional]  # noqa: E501
            malware_id ([MalwareId]): [optional]  # noqa: E501
            malware_id_restricted ([MalwareId]): [optional]  # noqa: E501
            strings (ResultAllOfStrings): [optional]  # noqa: E501
            urls ([str]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.hashes = hashes
        self.analysis = analysis
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
