from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/template/<string:name>')
def temp(name):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()