from flask import Flask
from routes import routes_blueprint

app = Flask(__name__)
app.secret_key = 'secretkey'


app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
