# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentProcessorInformation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'AddressInformation',
        'billing_agreement_id': 'str',
        'email': 'str'
    }

    attribute_map = {
        'address': 'address',
        'billing_agreement_id': 'billingAgreementId',
        'email': 'email'
    }

    def __init__(self, address=None, billing_agreement_id=None, email=None):  # noqa: E501
        """PaymentProcessorInformation - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._billing_agreement_id = None
        self._email = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if billing_agreement_id is not None:
            self.billing_agreement_id = billing_agreement_id
        if email is not None:
            self.email = email

    @property
    def address(self):
        """Gets the address of this PaymentProcessorInformation.  # noqa: E501


        :return: The address of this PaymentProcessorInformation.  # noqa: E501
        :rtype: AddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PaymentProcessorInformation.


        :param address: The address of this PaymentProcessorInformation.  # noqa: E501
        :type: AddressInformation
        """

        self._address = address

    @property
    def billing_agreement_id(self):
        """Gets the billing_agreement_id of this PaymentProcessorInformation.  # noqa: E501

          # noqa: E501

        :return: The billing_agreement_id of this PaymentProcessorInformation.  # noqa: E501
        :rtype: str
        """
        return self._billing_agreement_id

    @billing_agreement_id.setter
    def billing_agreement_id(self, billing_agreement_id):
        """Sets the billing_agreement_id of this PaymentProcessorInformation.

          # noqa: E501

        :param billing_agreement_id: The billing_agreement_id of this PaymentProcessorInformation.  # noqa: E501
        :type: str
        """

        self._billing_agreement_id = billing_agreement_id

    @property
    def email(self):
        """Gets the email of this PaymentProcessorInformation.  # noqa: E501

          # noqa: E501

        :return: The email of this PaymentProcessorInformation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PaymentProcessorInformation.

          # noqa: E501

        :param email: The email of this PaymentProcessorInformation.  # noqa: E501
        :type: str
        """

        self._email = email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaymentProcessorInformation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
