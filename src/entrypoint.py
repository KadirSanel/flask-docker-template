from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask & Docker</h2>'

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)