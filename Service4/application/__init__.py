from flask import Flask, Response, request,jsonify
import uuid, requests, json
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/post/Character', methods=['POST'])
def Character():
    affinities = {"Neutral": 0, "Good": 6, "Bad": -6}
    characteristics = request.get_json()
    #characteristics_json = characteristics.json()
    #print(characteristics)
    race_dictionary = characteristics["key"]
    role_dictionary = characteristics["value"]
    #print(race_dictionary.values())
    #print(role_dictionary.values()) 
    Alignment1 = sum(race_dictionary.values())
    Alignment2 = sum(role_dictionary.values())
    Alignment  = Alignment1 + Alignment2
    print(Alignment)
    for key in affinities:
        affinity = key
        #Alignment = int(Alignment)
        if Alignment == affinities["Neutral"]:
            affinity = "Neutral" 
            return jsonify({"Moral":affinity})

        elif Alignment > affinities["Neutral"]:
            if Alignment <= affinities["Good"]:
                affinity = "Good"
                return jsonify({"Moral":affinity})

        else: 
            if Alignment < affinities["Neutral"]:
                if Alignment >= affinities["Bad"]:
                    affinity = "Bad"
                    return jsonify({"Moral":affinity})

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')