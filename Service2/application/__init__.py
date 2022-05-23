from flask import Flask, Response, jsonify
#from random import choice
import random
app = Flask(__name__)

@app.route('/get/race', methods=['GET'])
def race():
    races = {"Orc":-1, "Elf":3, "Human": 0, "Demon": -3, "Dwarf": 1 }
    #git branch
    #races = {"Orc":-1, "Elf":3}
    species1 = random.choice(list(races.items()))
    species = {species1[0]: species1[1]}
    #return Response(species, mimetype='application/json')
    return jsonify(species)

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')