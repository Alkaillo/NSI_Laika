from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")
@app.route('/autre_page')
def autre_page():
    return render_template("2ndPage.html")
app.run(debug=True)