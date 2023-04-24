from flask import Flask,render_template,request
import os
from app.func.pdf_to_txt import to_txt

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(to_txt(file))
        return render_template('show_result.html', result_txt = to_txt(file))
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)