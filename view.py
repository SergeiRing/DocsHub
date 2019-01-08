from app import app, db
from flask import render_template
from flask import request
from forms import RegisterForm
from flask import url_for, redirect
from models import User

@app.route('/')
def main():
    return render_template('main.html', static_folder = 'static')


#@app.route('/Txt-<name>')
#def txt(name):
    #user = User.query.filter(User.name==name).first()
    #print(user.txt[0].text)
    #return render_template('docs.html')

@app.route('/docs-<email>')
def docs(email):
    user = User.query.filter(User.email==email).first()
    email = user.email
    return render_template('docs.html', email = email, static_folder = 'static', staric_url_path = '/static')



@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = User.query.filter(User.email==email).first()
            name = user.name
            surname = user.surname
        except:
            form = RegisterForm()
            error = '¥ Something was wrong'
            return render_template('log.html', error = error, email = form.email, password = form.password)
        if user.password == password:
            return redirect(url_for('docs', email = email))
            #return render_template('main.html', static_folder = 'static', name = name, surname = surname, login_or_logout = login_or_logout, slug = slug)
        else:
            form = RegisterForm()
            error = '¥ Something was wrong'
            return render_template('log.html', error = error, email = form.email, password = form.password)
    form = RegisterForm()
    email = form.email
    password = form.password
    error = ''
    return render_template('log.html', email = email, password = password, error = error)


@app.route('/register', methods = ['POST', 'GET'])
def register():  
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        db.session.rollback()
        user = User(name = name, surname = surname, email = email, password = password)
        db.session.add(user)
        db.session.commit()
    user = RegisterForm()
    name = user.name
    surname = user.surname
    email = user.email
    password = user.password
    error = '' 
    return render_template('reg.html', name = name, surname = surname, email = email, password = password, error = error)

#@app.errorhandler(Exception)
def Error(e):
        user = RegisterForm()
        name = user.name
        surname = user.surname        
        email = user.email
        password = user.password
        error = '¥ This Email is already exist'
        return render_template('reg.html', email = email, password = password, surname = surname, name = name, error = error)

