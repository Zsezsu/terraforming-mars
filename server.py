from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/design')
def design():
    return render_template('design/design.html')


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")

