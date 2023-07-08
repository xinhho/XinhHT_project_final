from flask import Flask

app = Flask(__name__)

@app.route('/greeting')
def index():
    return 'Greeting, this is version 1'

app.run(host='0.0.0.0', port=80)