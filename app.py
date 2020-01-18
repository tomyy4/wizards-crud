from flask import Flask
from db.database import db
from db.config import config
import os
from views.wizards import wizard
from views.houses import house

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['mysql']
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)
app.register_blueprint(wizard)
app.register_blueprint(house)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)




