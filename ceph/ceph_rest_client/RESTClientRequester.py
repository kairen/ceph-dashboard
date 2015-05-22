from cephclient.wrapper import *
import json

if __name__ == '__main__':

    wrapper = CephWrapper(
        endpoint='http://10.21.10.180:5100/api/v1/',
        debug=True
    )

    response, body = wrapper.fsid(body='json')
    print(
        'Response: {0}, Body:\n{1}'.format(response, json.dumps(body, indent=4, separators=(',', ': ')))
    )

    pg_response, pg_body = wrapper.pg_dump_pools_json(body='json')
    print(
        'Response: {0}, Body:\n{1}'.format(pg_response, json.dumps(pg_body, indent=4, separators=(',', ': ')))
    )