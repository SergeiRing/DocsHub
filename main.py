from app import app
import view
from Txt.blueprint import txt

app.register_blueprint(txt, url_prefix = '/Txt')

if __name__ == '__main__':
	app.run()