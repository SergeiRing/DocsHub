from wtforms import Form, StringField

class RegisterForm(Form):
	name = StringField('name')
	surname = StringField('surname')
	email = StringField('email')
	password = StringField('password')