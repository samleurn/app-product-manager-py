from flask import Flask

app = Flask(__name__)


@app.route('/api/health')
def health():
    return 'Ok'

@app.route('/api/home')
def home():
    return '200'

app.run(debug=True)
