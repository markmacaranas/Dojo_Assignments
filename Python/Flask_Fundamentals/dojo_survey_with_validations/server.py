from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "JustDoIt"
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/results', methods=['get'])
# def results():
    # return render_template('results.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comment cannot have more than 120 characters!")
        return redirect('/')

    return render_template('/results.html')

app.run(debug=True)
