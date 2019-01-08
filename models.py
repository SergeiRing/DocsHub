from app import db

roles_users = db.Table('roles_users', 
	                   db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	                   db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
	                   extend_existing=True)

users_texts = db.Table('users_texts',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('text_id', db.Integer, db.ForeignKey('text.id')),
                     extend_existing=True)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	surname = db.Column(db.String(100))
	email = db.Column(db.String(100), unique = True)
	password = db.Column(db.String(100))

	texts = db.relationship('Text', secondary = users_texts, backref = db.backref('users', lazy = 'dynamic'))


	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(255))	


class Text(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.Text)
	name = db.Column(db.String(140))
