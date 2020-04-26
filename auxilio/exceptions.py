class AuxilioException(Exception):
    api_response = ''
    def __init__(self, api_response):
        self.api_response = api_response
        super().__init__(self)

class InvalidCode(AuxilioException):
    pass
class InvalidCPF(AuxilioException):
    pass
class InvalidResponse(AuxilioException):
    pass