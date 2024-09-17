from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
import datetime
from config import config  # Importa la configuración

motors = Flask(__name__)
motors.config.from_object(config['development'])  # Cargar la configuración
db = MySQL(motors)

@motors.route("/")
def home():
    return render_template('home.html')

@motors.route("/signin", methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@motors.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg = datetime.datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuarios (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)", 
                           (nombre, correo, claveCifrada, fechareg))
        db.connection.commit()
    
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    motors.run(port=33000)

