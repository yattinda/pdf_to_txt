from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)