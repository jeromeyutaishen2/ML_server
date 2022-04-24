# -*- coding: utf-8 -*-
"""
Created on Apr 23 16:12:51 2022

@author: Jerome Yutai Shen

"""

from main import app
from default_settings import END_POINTS, CSV_FILENAME
import pytest


def generate_input_nums(num_lines: int = 10, num_digits: int = 2):
    import random
    input_lines = []
    str_formatter = "{:." + str(num_digits) + "f}"
    for idx in range(num_lines):
        input_lines.append(f"{str_formatter.format(random.uniform(0, 10))},{str_formatter.format(random.uniform(0, 10))},{str_formatter.format(random.uniform(0, 10))},{str_formatter.format(random.uniform(0, 5))}")

    return input_lines


def single_predict(input_line: str, if_debug: bool = False):
    if if_debug:
        print(f"input_line: {input_line} {type(input_line)}")
    response = app.test_client().post(END_POINTS[1],
                                      data={'input_line': input_line},
                                      content_type='multipart/form-data')
    return response.status_code == 200


@pytest.mark.parametrize("input_line", generate_input_nums())
def test_multiple_predicts(input_line):
    print(f"input_lines: {input_line}")
    assert single_predict(input_line)


def test_create():
    response = app.test_client().post(END_POINTS[0],
                                      data={'csv_file': CSV_FILENAME,
                                            'target': 'Species'},
                                      content_type='multipart/form-data')
    return response.status_code == 200



