#!/usr/bin/env python3

import os
import re
import requests

from json import dumps

DIRECTORY = os.path.dirname(__file__)
RE_YAML = re.compile(r'\.ya?ml$')


def main():
    schemas = requests.get('http://schemastore.org/api/json/catalog.json').json()['schemas']
    schema_list = []
    for schema in schemas:
        fileMatch = schema.get('fileMatch')
        url = schema['url']
        if fileMatch:
            fileMatch = list(filter(lambda pattern: not RE_YAML.search(pattern), schema['fileMatch']))
        if fileMatch:
            schema_list.append({'fileMatch': fileMatch, 'url': url})

    with open(os.path.join(DIRECTORY, '..', 'schemas.json'), 'w') as f:
        f.write(dumps(schema_list, indent=2))


if __name__ == '__main__':
    main()
