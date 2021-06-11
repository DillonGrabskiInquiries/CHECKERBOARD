from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eightEight():
    return render_template('checker.html')

@app.route('/4')
def eightFour():
    return render_template('checker2.html')

@app.route('/(x)/(y)')
def eightFour():
    return render_template('checker3.html')

if __name__=="__main__":
    app.run(debug=True)