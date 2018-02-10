from flask import Flask, jsonify, abort
#from flask_restful import Resource, Api


app = Flask(__name__)

countries = [
    {
        'name': 'Spain',
        'code': 'ES'
    },
    {
        'name': 'Ireland',
        'code': 'IE'
    },
    {
        'name': 'UK',
        'code': 'GB'
    },
    {
        'name': 'France',
        'code': 'FR'
    }
]

@app.route('/api/v1/countries/<string:country_name>')

def get_country(country_name):
    for code in countries:
        if code['name'] == country_name:
            return jsonify(code)
    return jsonify({'message': 'Country Code not found'})
#    country = [country for country in countries if country['name'] == country_name]
#    if len(country) == '':
#        abort(404)
#    return jsonify({'countries': countries[0]})


app.run(port=5000, debug=True)
