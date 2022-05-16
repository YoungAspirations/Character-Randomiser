from flask import render_template, Flask
import uuid, requests
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/Character', methods=['GET'])
def Character():
    race = requests.get('http://localhost:5001/race')
    role = requests.get('http://localhost:5002/role')
    affinity = requests.get('http://localhost:5003/Character')
    
    return render_template('Character.html', alignment= affinity)

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')