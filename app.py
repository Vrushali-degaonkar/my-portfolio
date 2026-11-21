from flask import Flask, render_template

app = Flask(__name__)

# PERSONALIZE THIS SECTION before publishing.
PROFILE = {
    "name": "Vrushali Degaonkar",
    "headline": "Python Developer | FrontEnd Developer | AWS ",
    "intro": "I enjoy building practical solutions with Python and Frontend technologies.",
    "about": (
        "I am an aspiring IT professional developing my skills in Python, AWS, Linux, "
        "and Infrastructure as Code. I like learning by building projects, documenting "
        "what I learn, and solving practical technical problems."
    ),
    "location": "India",
    "email": "degaonkarvrushalis@example.com",
    "github_url": "https://github.com/Vrushali-degaonkar",
    "linkedin_url": "https://www.linkedin.com/in/vrushali-degaonkar-00bb26262/",
}

SKILLS = [
    ("Python", "Programming and scripting"),
    ("AWS", "EC2 and cloud fundamentals"),
    ("Linux", "Command line and troubleshooting"),
    ("Git & GitHub", "Version control"),
    ("HTML & CSS", "Web fundamentals"),
]




@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
    )


if __name__ == "__main__":
    # Local development only. Render runs the app with Gunicorn.
    app.run(host="127.0.0.1", port=5000, debug=True)
