from flask import Flask , render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form():
    session['names'] = request.form['names']
    
    session['dojo'] = request.form['dojo']
    
    session['language'] = request.form['language']
    
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def results():
    return render_template('index2.html')

if __name__=="__main__":
    app.run(debug=True)