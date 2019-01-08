from wtforms import Form, StringField, TextAreaField
class EditTextForm(Form):
	name = StringField('name')
	text = TextAreaField('text')