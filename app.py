from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sonic2504'
app.config['MYSQL_DB'] = 'JuegoArq'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        usuario = details['usuario']
        contra = details['contra']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(username, contra) VALUES (%s, %s)", (usuario, contra))
        mysql.connection.commit()
        cur.close()
        return 'Registrado Exitosamente'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()