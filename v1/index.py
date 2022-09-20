from flask import Flask
from v1.routes.instrumentos import instrumentos_bp

app = Flask(__name__)
app.register_blueprint(instrumentos_bp)

if __name__ == "__main__":
    app.run("localhost", 4000, debug=True)
