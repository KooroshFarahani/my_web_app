from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# صفحه اصلی
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

# دریافت نظر کاربر
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")
    print(f"Received: {name} - {message}")  # چاپ در کنسول برای دیباگ
    return redirect(url_for('home'))  # هدایت به صفحه اصلی

# راه‌اندازی سرور
if __name__ == "__main__":
    app.run(debug=True)