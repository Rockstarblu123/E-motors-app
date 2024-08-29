# save this as app.py
from flask import Flask,render_template, url_for

motors = Flask(__name__)

@motors.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    motors.run(debug=True,port=33000)