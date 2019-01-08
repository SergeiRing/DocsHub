from flask import Blueprint
from flask import render_template
from models import User, Text
from Txt.forms import EditTextForm
from flask import request
from app import db

txt = Blueprint('Txt', __name__, template_folder='templates', static_folder='static')

@txt.route('/User-<email>')
def txt_main(email):
    user = User.query.filter(User.email==email).first()
    print(user) 
    texts = user.texts
    return render_template('texts.html', texts = texts)

@txt.route('/Text-<id>', methods = ['POST', 'GET'])
def text(id):
    t_object = Text.query.filter(Text.id==id).first()
    if request.method == 'POST':
        form = EditTextForm(formdata = request.form, obj = t_object)
        form.populate_obj(t_object)
        db.session.commit()
    form = EditTextForm(obj=t_object)
    name = form.name
    text = form.text
    return render_template('edit_text.html', form = form, t_object = t_object, text = text, name = name)