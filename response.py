from datetime import datetime

from http_const import ResponseCode, HTTP_VERSION, RESPONSE_STATUS, HTTP_DATE_FORMAT
from server_config import SERVER_NAME


class Response:
    def __init__(self, code, content_type='', content_length=0, content=b''):
        self.code = code
        self.content_type = content_type
        self.content_length = content_length
        self.content = content

    def build(self):
        if self.code == ResponseCode.OK:
            response = self.__response_ok()
        else:
            response = self.__response_fail()
        return response

    @staticmethod
    def __get_now_date_http_formatted(http_format):
        return datetime.utcnow().strftime(http_format)

    def __response_ok(self):
        return ('HTTP/{http_version} {http_status}\r\n'
                'Server: {server_name}\r\n'
                'Date: {date}\r\n'
                'Connection: Close\r\n'
                'Content-Length: {content_length}\r\n'
                'Content-Type: {content_type}\r\n\r\n')\
                   .format(http_version=HTTP_VERSION,
                           http_status=RESPONSE_STATUS[self.code.value],
                           server_name=SERVER_NAME,
                           date=self.__get_now_date_http_formatted(HTTP_DATE_FORMAT),
                           content_length=self.content_length,
                           content_type=self.content_type).encode() + self.content

    def __response_fail(self):
        return ('HTTP/{http_version} {http_status}\r\n'
                'Server: {server_name}\r\n'
                'Date: {date}\r\n'
                'Connection: Closed\r\n\r\n')\
            .format(http_version=HTTP_VERSION,
                    http_status=RESPONSE_STATUS[self.code.value],
                    server_name=SERVER_NAME,
                    date=self.__get_now_date_http_formatted(HTTP_DATE_FORMAT)).encode()

