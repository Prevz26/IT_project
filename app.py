from flask import Flask, render_template
app = Flask(__name__)

#home page
@app.route("/")
@app.route("/home_page")
@app.route("/login")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(
        debug= True
    )