from os import getenv, name
from flask import Flask

def create_app():

    appl = Flask(__name__)
    appl.secret_key = getenv("FLASK_API_KEY")

    from api import app
    appl.register_blueprint(app)

    return appl

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True if name.upper() == 'NT' else False)
