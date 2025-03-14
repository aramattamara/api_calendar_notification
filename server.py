from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/calendar_view')
def calendar_view():
    return render_template("calendar.html")

if __name__ == '__main__':
    app.run(debug=True)
