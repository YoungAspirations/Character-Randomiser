from crypt import methods
from flask import Flask, Response
from random import choice
app = Flask(__name__)

@app.route('/race', methods=['GET'])
def race():
    races = {'Orc':'-1', 'Elf':'3', 'Human':'0', 'Demon':'-3', 'Dwarf':'1'}
    species = choice(races)
    race_type = species.keys()
    karma_2 = species.values()
    return Response(race_type, karma_2, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')