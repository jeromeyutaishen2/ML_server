# -*- coding: utf-8 -*-
"""
Created on Apr 23 16:12:51 2022

@author: Jerome Yutai Shen

"""

from flask import Flask, request, jsonify, render_template
from default_settings import MODEL_FILENAME, WARN_MODEL_FILE_NOT_EXIST, DEFAULT_PORT, END_POINTS, DEFINED_METHODS_POST, md2html
from data_model import train_model, string2array, pandas_csvreader, save_model, load_saved_model


app = Flask(__name__)


@app.route("/", methods = ["GET"])
def home_page():
    return md2html('README.md')  # markdown文件的路径


@app.route(END_POINTS[1], methods = DEFINED_METHODS_POST)
def post_predict():
    input_line = request.form.get("input_line")
    print(f"request.form: {request.form}, input_line: {input_line} {type(input_line)}")
    x_test = string2array(input_line)

    clf = load_saved_model()
    if not clf:
        return WARN_MODEL_FILE_NOT_EXIST

    return f"{http_response_ok(True)} {clf.predict(x_test)[0]}"


@app.route(END_POINTS[0], methods = DEFINED_METHODS_POST)
def post_create():
    csv_fname = request.form.get("csv_file")
    df = pandas_csvreader(csv_fname)

    target = request.args.get("target")
    x_train = df.loc[:, ~df.columns.isin([target])].values

    clf = train_model(x_train,
                      df[target].values)
    save_model(clf)
    return f"{http_response_ok(True)} SVM model is saved as {MODEL_FILENAME}"


def http_response_ok(if_success: bool = True):
    return jsonify(success = if_success)


if __name__ == "__main__":
    app.run(port = DEFAULT_PORT,
            debug = False)

