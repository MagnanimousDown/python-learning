from flask import Flask, render_template

app = Flask(__name__)

@app.route("/profile", methods=["GET"])
def profile():
    return render_template(
        "profile.html",
        name = "Omkar",
        role = "Backend Developer",
        city = "Goa"
    )

@app.route("/skills", methods=["GET"])
def skills():
    skills = ["Python", "Flask", "SQL", "Docker"]

    return render_template(
        "skills.html",
        skills = skills
    )

@app.route("/age", methods=["GET"])
def age():
    return render_template(
        "age.html",
        age = 20
    )

@app.route("/homepage", methods=["GET"])
def homepage():
    return render_template(
        "homepage.html",
        is_logged_in = True
    )

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)