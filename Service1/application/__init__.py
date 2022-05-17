from flask import render_template, Flask
import uuid, requests
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/home', methods=['GET'])
def Character():
    race = requests.get('http://localhost:5001/race').text
    role = requests.get('http://localhost:5002/role').text
    components = race.update(role)
    affinity = requests.post('http://localhost:5003/Character', data=components).text
    
    return render_template('Character.html',race = race, role = role, alignment = affinity)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')