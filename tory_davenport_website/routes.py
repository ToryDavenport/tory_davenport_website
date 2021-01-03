from flask import request, Flask, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please Try Again'
        else:
            return redirect(url_for('home'))
    return render_template('signin.html', error=error)

@app.route("/index.html", methods=['GET', 'POST'])
def home():
    return render_template('index.html', title="This is the home page")

@app.route("/about.html", methods=['GET', 'POST'])
def about():
    return render_template('index.html', title="This is the About page")

@app.route("/style.css")
def css():
    return send_from_directory(os.path.join(app.root_path, 'static/style'), 'style.css')

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')