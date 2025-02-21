from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@app.route("/ngos")
def ngos():
    return render_template("ngos.html")

if __name__ == "__main__":
    app.run(debug=True)
