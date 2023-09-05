from flask import Flask

app = Flask(__name__)

# Import routes after initializing app
from routes import *

if __name__ == '__main__':
    app.run(port=5001,debug=True)
