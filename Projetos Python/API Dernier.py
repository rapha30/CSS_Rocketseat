from flask import Flask
import flask
app = flask(__name__)

@   app.route('/')
def hello_world():
    return "hello world."