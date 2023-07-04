from flask import Flask, render_template, request, flash
from app.func.pdf_to_txt import to_txt, allowed_file
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('File not found')
            return render_template('index.html')
        elif not allowed_file(file.filename):
            flash("You can ONLY upload PDF")
            return render_template('index.html')
        if file:
            print(to_txt(file))
            return render_template('show_result.html', result_txt=to_txt(file))

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
