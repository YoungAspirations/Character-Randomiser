from flask import Flask, Response
from random import choice
app = Flask(__name__)

@app.route('/role', methods=['GET'])
def role():
    roles = {'Sorcerer' :'0', 'Warrior':'1', 'Priest':'3', 'Necromancer':'-3', 'Rogue':'-1'}
    job = choice(roles)
    return Response(job, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')