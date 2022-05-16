from flask import render_template, redirect, request, url_for, Flask
import uuid, requests
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/Character', methods=['GET'])
def Character():
    race = requests.get('http://url/race')
    role = requests.get('http://url/role')
    affinities = {'Neutral':'0', 'Good':'5', 'Bad':'5'}
    Alignment=
    return render_template(url_for('Character'), race='race', role='role', alignment ='Alignment')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')