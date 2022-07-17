from string import Template

from rest_framework.exceptions import APIException


class PropertyUnavailable(APIException):
    status_code = 417
    default_detail = Template(
        "set params before using analysis algorithm, params: $property"
    )

    def __init__(self, property=None, detail=None, code=None):
        params = dict(property=property)
        self.default_detail = self.default_detail.safe_substitute(params)
        super().__init__(detail=detail, code=code)


class InvalidArgument(APIException):
    status_code = 417
    default_detail = Template(
        "set argument in an appropriate range, params: $property"
    )

    def __init__(self, property=None, detail=None, code=None):
        params = dict(property=property)
        self.default_detail = self.default_detail.safe_substitute(params)
        super().__init__(detail=detail, code=code)
