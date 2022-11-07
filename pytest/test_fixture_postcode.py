#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 1:48
# @Author  : Haorui Guo
# @File    : test_fixture_postcode.py
import pytest


@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'


if __name__ == '__main__':
    pytest.main(['-vs', './test_fixture_postcode.py'])
