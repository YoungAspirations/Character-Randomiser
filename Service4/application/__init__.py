from flask import render_template, redirect, request, url_for, Flask, Response
import uuid, requests
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/Character', methods=['GET'])
def Character():
    race = requests.get('http://localhost:5001/race')
    role = requests.get('http://localhost:5002/role')
    affinities = {'Neutral':'0', 'Good':'5', 'Bad':'5'}
    Alignment=sum()
    return Response()

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')