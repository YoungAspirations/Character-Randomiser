from flask import Flask, Response, jsonify
import random
app = Flask(__name__)

@app.route('/get/role', methods=['GET'])
def role():
    roles = {"Sorcerer" : 0, "Warrior": 1, "Priest": 3, "Necromancer": -3, "Rogue": -1}
    job1 = random.choice(list(roles.items()))
    job = {job1[0] : job1[1]}
    #return Response(job, mimetype='application/json')
    return jsonify(job)

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')