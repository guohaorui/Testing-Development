#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 1:12
# @Author  : Haorui Guo
# @File    : test_Flask.py
import requests
import json
import pytest
import yaml


def read_json():
    with open('data.json', 'r', encoding='UTF-8') as f:
        return json.load(f)['item']


@pytest.mark.parametrize('data', read_json())
def test_json_login(data):
    r = requests.post(url=data['request']['url'], json=data['request']['body'])
    assert r.json() == data['response'][0]


def read_yaml():
    with open('data.yml', 'r', encoding='UTF-8') as f:
        return list(yaml.safe_load_all(f))


@pytest.mark.parametrize('data', read_yaml())
def test_yaml_login(data):
    r = requests.post(url=data['url'], json=data['body'])
    assert r.json() == data['expect']


if __name__ == '__main__':
    read_yaml
    pytest.main(['-vs', './test_Flask.py'])
