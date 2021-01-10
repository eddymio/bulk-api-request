import json


def json_reader(path):
    with open(path) as json_file:
        return json.load(json_file)


def to_json(data):
    multiple = []
    for d in data:
        multiple.append(json.dumps(d, indent=4))
    return multiple


if __name__ == '__main__':
    all_data = json_reader('template.json')
    for data in all_data:
        print(data['name'])
        print(data['type'])
        print(data['amount'])
        print(data['broker']['id'])
        print(data['rights'][0]['id'])
        print(data['trader']['name'])

    all_data = to_json(all_data)
    for a in all_data:
        print(a)
