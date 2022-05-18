from flask import render_template, Flask
import uuid, requests, json
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def Character():
    #race = requests.get('http://localhost:5001/race').text
    #role = requests.get('http://localhost:5002/role').text
    #components = race.update(role)
    #affinity = requests.post('http://localhost:5003/Character', data=components).text

    race = requests.get('http://localhost:5001/get/race')
    role = requests.get('http://localhost:5002/get/role')
    race_json = race.json()
    role_json = role.json()
    #new_dictionary ={**race_json, **role_json}
    #new_dictionary ={**race, **role}
    affinity = requests.post('http://localhost:5003/post/Character', json={"key": race_json, "value": role_json})
    affinity1 = affinity.json()
    return render_template('Character.html',race = race_json, role = role_json, alignment = affinity1)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')