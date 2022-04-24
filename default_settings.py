# -*- coding: utf-8 -*-
"""
Created on Apr 23 16:13:09 2022

@author: Jerome Yutai Shen

"""

END_POINTS = ("/create", "/predict")
DEFAULT_PORT = 5000
FONTSIZE_TITLE = ("<h1>", "</h1>")
FONTSIZE_CONTENT = ("<h3>", "</h3>")
MODEL_FILENAME = "model.pkl"
WARN_MODEL_FILE_NOT_EXIST = "No saved model file found. Please try training a model with iris.csv first."
CSV_FILENAME = "iris.csv"
DEFINED_METHODS_POST = ("POST", )
DEFINED_METHODS_GET = ("GET", )


def md2html(filename: str = 'README.md') -> str:
    md_content = ""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.readlines()

    for line in content:
        if line.startswith("#"):
            md_content += f"{FONTSIZE_TITLE[0]}{line[1:]}{FONTSIZE_TITLE[1]}"
        else:
            md_content += f"{FONTSIZE_CONTENT[0]}{line}{FONTSIZE_CONTENT[1]}"

    return md_content
