from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    # print(f"Exc: {exc}")
    # print(f"Context: {context}")
    response = exception_handler(exc, context)

    # print(f"ERROR Res: {response}")
    # print(f"ERROR Res data: {response.data}")
    # print(f"ERROR Res data: {response.status_code}")
    if response is not None:
        # Convert list to string
        for key in response.data:
            if type(response.data.get(key)).__name__ == "list" or type(response.data.get(key)).__name__ == "tuple":
                response.data[key] = response.data[key][0]
        # change 'detail' to 'msg'
        if response.data.get('detail'):
            response.data['msg'] = response.data.get('detail')
            del response.data['detail']
        response.data['success'] = False

    return response


