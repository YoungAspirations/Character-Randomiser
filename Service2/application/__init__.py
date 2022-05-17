from flask import Flask, Response
from random import choice
app = Flask(__name__)

@app.route('/race', methods=['GET'])
def race():
    races = {'Orc':'-1', 'Elf':'3', 'Human':'0', 'Demon':'-3', 'Dwarf':'1'}
    species = choice(races)
    return Response(species, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')