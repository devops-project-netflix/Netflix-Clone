from flask import Response
import json
from bson import json_util


def http_response(http_status_code, data):
    response = {}
    response['data'] = data
    final_response = json.dumps(response, default=json_util.default)
    return Response(final_response, status=http_status_code, mimetype='application/json')
