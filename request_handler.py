try:
    from urllib.parse import urlparse, unquote, parse_qs
except ImportError:
     from urlparse import urlparse, unquote, parse_qs
import os

from response import Response
from http_const import ResponseCode, CONTENT_TYPES, DEFAULT_PAGE


class RequestHandler:
    def __init__(self, raw_request, root_dir):
        self.method = raw_request.split(b' ')[0].decode()
        self.headers = self.__extract_headers(raw_request)
        self.host = self.headers.get('Host', '')
        self.url, self.path, self.query_params = self.__make_url(raw_request)
        self.root_dir = root_dir

    @staticmethod
    def __extract_headers(raw_request):
        headers_dict = {}
        headers = raw_request.split(b'\r\n\r\n')[0]  # first part after split sign
        headers = headers.split(b'\r\n')[1:]  # from the second line
        for header in headers:
            header = header.decode().split(': ')
            headers_dict.update({header[0]: header[1]})
        return headers_dict

    def __make_url(self, raw_request):
        raw_url = self.host + raw_request.split(b' ')[1].decode()
        if '://' not in raw_url:
            raw_url = '//' + raw_url
        url = urlparse(raw_url)
        return url.geturl(), unquote(url.path), parse_qs(unquote(url.query))

    def handle(self):
        if self.method in ['GET', 'HEAD']:
            response = self.__make_response()
        else:
            response = Response(ResponseCode.NOT_ALLOWED)
        return response

    @staticmethod
    def __get_content_type(real_path):
        content_type = real_path.split('.')[-1]
        return CONTENT_TYPES.get(content_type, '')

    def __make_response(self):
        real_path = os.path.normpath(self.root_dir + '/' + self.path)
        print(real_path)
        response = Response(ResponseCode.NOT_FOUND)

        if os.path.commonprefix([real_path, self.root_dir]) != self.root_dir:
            return response

        if os.path.isfile(os.path.join(real_path, DEFAULT_PAGE)):
            real_path = os.path.join(real_path, DEFAULT_PAGE)
        elif os.path.exists(os.path.join(real_path)):
            response.code = ResponseCode.FORBIDDEN

        try:
            with open(real_path, 'rb') as file_reader:
                content = file_reader.read()
                response.content = content if self.method == 'GET' else b''
                response.content_length = len(content)
                response.content_type = self.__get_content_type(real_path)
                response.code = ResponseCode.OK
        except IOError as e:
            print("Error with " + e.filename)

        return response

