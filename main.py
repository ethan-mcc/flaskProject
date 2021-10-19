from flask import Flask, render_template, request
import db

# export FLASK_APP=main
# flash run -p 5001

db.createtable()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if db.checklogin(email, password) == "good":
            print("good login")
            return render_template('welcome.html')
        else:
            print("failed login")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db.inputregister(email, password)
        db.printtable()
    return render_template('register.html')
