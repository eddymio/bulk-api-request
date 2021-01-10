import argparse
import json

import template_reader
import csv_reader
import yaml
import api
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)


def merge(template_data, csv_data):
    for cd in csv_data:
        for td in template_data:
            td['type'] = cd.get('tradeType')
            td['date'] = cd.get('dateOfTrade')
            td['amount'] = cd.get('tradeAmount')
            td['trader']['id'] = cd.get('personId')
            td['trader']['name'] = cd.get('personName')

    return template_data


def get_config(args):
    with open(args.config, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger.error(exc)


def parse_cli():
    parser = argparse.ArgumentParser(description='Send CSV over to API')
    parser.add_argument('--csv', help='csv data file path', required=False, default='data.csv')
    parser.add_argument('--json', help='data template file path', required=False, default='template.json')
    parser.add_argument('--config', help='Config file path', required=False, default='config.yml')
    return parser.parse_args()


if __name__ == '__main__':

    cli_args = parse_cli()
    config = get_config(cli_args)

    data = csv_reader.read_csv(cli_args.csv)
    template = template_reader.json_reader('template.json')

    multi_json_to_post = merge(template, data)

    for json_to_post in multi_json_to_post:
        res = api.post('http://mockbin.com/request', '', '', json_to_post)
        logger.info('Results %s', json.dumps(res.json(), indent=4, sort_keys=True))
