#!/usr/bin/python3

import json
import urllib3

urllib3.disable_warnings()

_http = urllib3.PoolManager()
_key = ''
_default_language = 'en-ru'


def _data_request(text):
    """Data build"""
    return dict(key=_key, lang=_default_language, text=text)


def _request(text):
    return _http.request('GET', 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup', fields=_data_request(text))


def _json_response(text):
    return json.loads(_request(text).data.decode('utf-8'))


def response(text):
    """response"""
    return _json_response(text)


def translate(text):
    """make request"""
    return response(text)


w_translated = translate('time').get('def', {})[0]
definition = w_translated['tr'][0]

print(definition['text'].upper(), '. Gen:', definition['gen'], '. Noun:', definition['pos'])
