from enum import Enum

RESPONSE_STATUS = {
    200: '200 Ok',
    403: '403 Forbidden',
    404: '404 Not Found',
    405: '405 Method Not Allowed'
}

CONTENT_TYPES = {
    'css': 'text/css',
    'gif': 'image/gif',
    'html': 'text/html',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'swf': 'application/x-shockwave-flash'
}

DEFAULT_PAGE = 'index.html'
HTTP_VERSION = '1.1'
HTTP_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'


class ResponseCode(Enum):
    OK = 200
    FORBIDDEN = 403
    NOT_FOUND = 404
    NOT_ALLOWED = 405

