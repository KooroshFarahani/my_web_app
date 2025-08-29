# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# صفحه اصلی
@app.route("/")
def home():
    return render_template("index.html")

# دریافت نظر کاربر
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")
    return f"<h1>Thanks, {name}!</h1><p>We got your message: <i>{message}</i></p>"

# راه‌اندازی سرور
if __name__ == "__main__":
    app.run(debug=True)