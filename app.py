from flask import Flask,render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/projects_one")
def projects():
    return render_template('projects_one.html')

@app.route("/projects_two")
def project_two():
    return render_template('projects_two.html')

@app.route("/projects_three")
def project_three():
    return render_template('projects_three.html')

@app.route("/blog_one")
def blogs():
    return render_template('single-article.html')


if __name__ == "__main__":
    app.run(debug=True)