from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/Land_Cruiser/')
def Land_Cruiser():
    return render_template("Land_Cruiser.html")

@app.route('/about_me/')
def about_me():
    return render_template("about_me.html")


if __name__=="__main__":
    app.run(debug=True)