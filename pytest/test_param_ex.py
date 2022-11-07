#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 0:52
# @Author  : Haorui Guo
# @File    : test_param_ex.py

import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize('a,b,expected', [[1, 1, 2], [2, 2, 4], [3, 3, 6]])
def test_addInt(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize('data', [{'a': 1, 'b': 1, 'expected': 2}, {'a': 3, 'b': 3, 'expected': 6},
                                  {'a': 2, 'b': 2, 'expected': 4}])
def test_addDict(data):
    assert add(data['a'], data['b']) == data['expected']


if __name__ == '__main__':
    pytest.main(['-vs'])
