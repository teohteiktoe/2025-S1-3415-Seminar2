from flask import Flask, request, render_template
#trial
app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])

def index():
    return render_template("index.html")


@app.route("/main", methods =["GET", "POST"])
def main():
    return render_template("main.html")


@app.route("/dbs", methods =["GET", "POST"])
def dbs():
    q= float(request.form.get("q"))
    return render_template("dbs.html", r = round((-50.6*q)+90.229,2))

if __name__ == "__main__": 
    app.run(port= 3000)



