from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('home.html')

# User input route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return render_template('result.html', name=name, age=age)
    return render_template('submit.html')  # This is now executed only when the method is GET

if __name__ == '__main__':
    app.run(debug=True)