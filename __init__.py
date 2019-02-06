from flask import Flask
import cv2
app = Flask(__name__)


@app.route("/")
def hello():
    return cv2.__version__


@app.route("/idan")
def idan():
    return "Hello idan!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
