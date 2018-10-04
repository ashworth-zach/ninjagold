from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process_money')
def process_money():
    # farm=form.request['farm']
    # cave=form.request['cave']
    # house=form.request['house']
    # casino=form.request['casino']
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)