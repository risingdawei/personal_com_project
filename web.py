from flask import Flask
from flask import request
from flask import render_template
from wtforms.fields import core, html5, simple
from wtforms import Form, validators, widgets

app = Flask(__name__)


class MyValidators(object):
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        if field.data == "zhiwei":
            return None
        raise validators.ValidationError(self.message)


class LoginForm(Form):
    name = simple.StringField(
        label="user_name",
        widget=widgets.TextInput(),
        validators=[
            MyValidators(message="the user_name is your name!"),
            validators.DataRequired(message="the user_name can't be NULL"),
            validators.Length(max=8, min=3, message="the user name should beyond %(min) and low than %(max)")
        ],
        render_kw={"class": "form-control"}
    )

    pwd = simple.PasswordField(
        label="password",
        widget=widgets.PasswordInput(),
        validators=[
            validators.DataRequired(message="can't be null"),
            validators.Length(max=8, min=3, message="the user name should beyond %(min) and low than %(max)"),
            validators.Regexp(regex="\d+", message="password should be numbers")
        ],
        render_kw={"class": "form-control"}
    )


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'leguoqing' and password == '19931001':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('form.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            # return "login success!"
            return render_template('signin-ok.html', username='zhiwei')
        else:
            return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)