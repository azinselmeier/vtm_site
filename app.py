from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle='Estimate')


@app.route('/vtm_inputs', methods=['GET', 'POST'])
def vtm_inputs():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        print(radius)
        print(height)
        cost = (((3.14*(radius**2))+(2*3.14*radius*height))/144*25)+(((3.14*(radius**2))+(2*3.14*radius*height))/144*15)
        print(cost)
        return render_template('estimate.html', pageTitle = 'Estimate', estimate = cost)
    return render_template('estimate.html', pageTitle = "Estimate")

if __name__ == '__main__':
    app.run(debug=True)
