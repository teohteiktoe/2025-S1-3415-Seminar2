from flask import Flask, request, render_template
#trial
app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])

def index():
    return render_template("index.html")


@app.route("/main", methods =["GET", "POST"])
def main():
    name= str(request.form.get("name"))
    return render_template("main.html", name=name)

@app.route("/dbs", methods =["GET", "POST"])
def dbs():
    exchangeRate= float(request.form.get("exchangeRate"))
    return render_template("dbs.html", price = round((-50.6*exchangeRate)+90.229,2))

if __name__ == "__main__": 
    app.run(port= 3000)



