


from flask import Flask,render_template, url_for

motors = Flask(__name__)

@motors.route("/")
def home():
    return render_template('home.html')

@motors.route("/signin")
def signin():
    return render_template('signin.html')

@motors.route('/singup')
def singup():
    return render_template('singnup.html') 
        
if __name__ == '__main__':
    motors.run(debug=True,port=33000)