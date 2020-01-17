from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/wizards')
def wizards():
    return 'Wizards page'


if __name__ == '__main__':
    app.run(debug=True)



