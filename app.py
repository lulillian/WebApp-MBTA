from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_city, get_temp


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
    city=get_city(place_name)
    temp_far=get_temp(city)
    return render_template('mbta_result.html',you=place_name,stop=stop,city=city,temp_far=temp_far)





if __name__ == '__main__':
    app.run(debug=True)
