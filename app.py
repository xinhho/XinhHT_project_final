from flask import Flask

app = Flask(__name__)

@app.route('/greeting')
def index():
    return 'Greeting. This is version 2'

  app.run(host='0.0.0.0', port=80)