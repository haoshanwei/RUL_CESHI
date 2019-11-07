from mock import Mock
import json


def mock_test(mock_method, request_data, url, method, response_data, header):
    """
    :param mock_method:
    :param request_data:
    :param url:
    :param method:
    :param response_data:
    :return: res
    """
    mock_method = Mock(return_value=response_data)
    print('mock_method:', mock_method)
    res = mock_method(url, method, json.dumps(request_data), header)
    return res
