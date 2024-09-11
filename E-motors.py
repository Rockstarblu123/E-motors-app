


from flask import Flask,render_template, url_for, render_template,url_for, request, redirect
from flask import_mysqldb import MySQL
from werkzeug.security import generate_password_hash
import datetime

motors = Flask(__name__)
db      = MySQL(motors)
@motors.route("/")
def home():
    return render_template('home.html')

@motors.route("/signin")
def signin():
    return render_template('signin.html')

@motors.route('/singup')
def singup():
    if request.metod == 'POST':
        nombre       = request.form['nombre']
        correo       = request.form['correo']
        clave        = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg     = datetime.now()
        regUsuario = db.connect.cursor()
        regUsuario.execute("INSERT INTO usuarios (nombre, correo, clave, fechareg)
                           VALUES (%s, %s, %s, %s)", (nombre, correo, claveCifrada, fechareg))
                           (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)", (nombre, correo, claveCifrada, fechareg))
                           db.Connection.commit()
        render_template(home.html)
    else:
        return render_template('singnup.html') 
        
if __name__ == '__main__':
    motors.run(debug=True,port=33000)
    
    