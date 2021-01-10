import requests
import json


def post(url, username, password, json_body):
    headers = {'content-type': 'application/json'}
    print('_request [POST]', url, username,)
    response = requests.post(url, data=json.dumps(json_body), auth=(username, password), headers=headers, verify=True)
    print("  => ", response.status_code)
    return response


if __name__ == '__main__':
    entry = {
        'name': 'Bob',
        'date': '2021-01-07 10:00:00'
    }
    res = post('http://mockbin.com/request', '', '', entry)

    print(json.dumps(res.json(), indent=4, sort_keys=True))
