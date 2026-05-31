from flask import Flask, request, jsonify, session, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

app.secret_key = "my-super-secret-key"

class RegisterForm(FlaskForm):

    name = StringField(
        "name",
        validators=[DataRequired()]
    )

    email = StringField(
        "email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "password",
        validators=[DataRequired()]
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        return "Registration Successful"

    print(form.errors)
    
    return render_template(
        "register.html",
        form=form
    )

if __name__ == "__main__":
    app.run(debug=True)