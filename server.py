from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']
    print(session['name'])
    return render_template('result.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)
