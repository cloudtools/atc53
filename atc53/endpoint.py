from . import BaseAWSObject


def endpoint_type_validator(value):
    valid_endpoint_types = [
        'value',
        'cloudfront',
        'elastic-load-balancer',
        's3-website'
    ]

    if value not in valid_endpoint_types:
        raise ValueError('% is not a valid value for Endpoint')
    return value


class Endpoint(BaseAWSObject):
    props = {
        'Type': (endpoint_type_validator, False),
        'Region': (basestring, False),
        'Value': (basestring, False)
    }
