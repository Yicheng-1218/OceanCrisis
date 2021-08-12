from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def _():
    return index()


@app.route('/seaturtle.html')
def seaturtle():
    return render_template('seaturtle.html')


@app.route('/garbagefish.html')
def garbagefish():
    return render_template('garbagefish.html')


@app.route('/right-1kg.html')
def package1KG():
    return render_template('right-1kg.html')


@app.route('/raincoat.html')
def rainCoat():
    return render_template('raincoat.html')


@app.route('/cupshare.html')
def cupshare():
    return render_template('cupshare.html')


@app.route('/beachcoin.html')
def beachcoin():
    return render_template('beachcoin.html')


@app.route('/coralreef.html')
def coralreef():
    return render_template('coralreef.html')


if __name__ == '__main__':
    app.run(debug=True)
