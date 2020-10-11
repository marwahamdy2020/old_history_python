from flask import Flask, request, redirect, url_for
# create ob from falsk can use all methods and include config instance file
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')  # include config file default

# app.config.from_pyfile('config.py') # include config instance file
# load file config depend on enviromment
# app.config.from_envvar('APP_SETTINGS')


@app.route("/")
def home_page():
    return "hello app history log"


@app.route("/about")
def about_page():
    return "hello aboutPage"


@app.route("/user/<username>")
def show_user(username):
    return "User {} ".format(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "User {} ".format(post_id)


@app.route("/path/<path:sub_bath>")
def show_path(sub_bath):
    return "subPath {} ".format(sub_bath)


@app.route("/members")
def show_user_profile():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return "<h3>First Name: {} <br> First Name: {} <h3>".format(first_name, last_name)


@app.route("/redirct/<name>")
def hello_user(name):
    if name == 'admin':
        return 'jjjjjjjjjjjjj'
    else:
        return redirect(url_for('about_page'))


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
