from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'idan'


@app.route("/idan")
def idan():
    return "Hello idan!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
