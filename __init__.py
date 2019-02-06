from flask import Flask
import cv2
app = Flask(__name__)


@app.route("/")
def hello():
    return cv2.__version__


@app.route("/idan")
def idan():
    return "Hello idan!"
