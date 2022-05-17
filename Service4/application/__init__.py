from flask import Flask, Response, request
import uuid, requests, json
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/Character', methods=['POST'])
def Character():
    affinities = {"Neutral":"0", "Good":"6", "Bad":"-6"}
    characteristics = request.data.decode('utf-8')
    dictionary = json.loads(characteristics)
    Alignment = sum(int(dictionary[item]) for item in dictionary)
    
    for key in affinities:
        affinity = key
        Alignment = int(Alignment)
        if Alignment == int(affinities["Neutral"]):
            affinity = "Neutral" 
            return Response(affinity, mimetype='text/plain')
        elif Alignment > int(affinities["Neutral"]):
            if Alignment <= int(affinities["Good"]):
                affinity = "Good"
                return Response(affinity, mimetype='text/plain')
        elif Alignment < int(affinities["Neutral"]):
            if Alignment >= int(affinities["Bad"]):
                affinity = "Bad"
                return Response(affinity, mimetype='text/plain')
        else:
            return 'error in code'

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')