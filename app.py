from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'

@app.get('/form')
def origin():
    return render_template('origin_form.html')

@app.post('/form')
def results():
    place_name=request.form['current_loco']
    stop=find_stop_near(place_name)
    return render_template('mbta_result.html',you=place_name,stop=stop)



if __name__ == '__main__':
    app.run(debug=True)
