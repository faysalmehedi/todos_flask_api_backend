from http import HTTPStatus
from typing import Union, List, Any, Dict 
from flask import make_response, jsonify 


class ResponseGenerator:
    @staticmethod
    def generate_response(data: Union[str, List[Any], Dict[str, Any]], code: int, error: bool = False):
        if error:
            response_data = {
                "error": {
                    "msg": data
                }
            }
        else:
            response_data = {
                "result": data
            }

        return make_response(jsonify(
            response_data
        ), code)

    @staticmethod
    def error_response(msg: str, code: int):
        return ResponseGenerator.generate_response(msg, code, True)

    @staticmethod
    def json_data_expected(msg: str = "JSON data is expected but not found!", code: int = HTTPStatus.BAD_REQUEST):
        return ResponseGenerator.error_response(msg, code)

    @staticmethod
    def mandatory_field(fields=None, code: int = HTTPStatus.BAD_REQUEST):
        if fields is None:
            fields = []

        return ResponseGenerator.error_response(",".join(fields) + " are mandatory fields!", code)

    @staticmethod
    def not_authorized(msg: str = "Unauthorized request!", code: int = HTTPStatus.UNAUTHORIZED):
        return ResponseGenerator.error_response(msg, code)

    @staticmethod
    def forbidden(msg: str = "Access forbidden!", code: int = HTTPStatus.FORBIDDEN):
        return ResponseGenerator.error_response(msg, code)

    @staticmethod
    def not_found(msg: str = "Not found!", code: int = HTTPStatus.NOT_FOUND):
        return ResponseGenerator.error_response(msg, code)

    @staticmethod
    def internal_server_error(msg: str = "Something went wrong! Try again later.", code: int = HTTPStatus.INTERNAL_SERVER_ERROR):
        return ResponseGenerator.error_response(msg, code)