# save this as app.py
from flask import flask, render_template, url_for

motors = flask(__name__)

@motors.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    e-motors.run(debug=True,port=33000)