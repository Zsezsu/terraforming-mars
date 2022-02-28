from flask import Flask, render_template, request, url_for, redirect, jsonify


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")

