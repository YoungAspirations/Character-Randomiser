from api1.application import app, db
from flask import render_template, redirect, request, url_for
from random import choice

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/race')
def race():
    races = {'Orc':'', 'Elf':'', 'Human':'', 'Demon':'', 'Dwarf':''}
    return render_template('home.html')

@app.route('/role')
def role():
    roles = {'Sorcerer' :'', 'Warrior':'', 'Monk':'', 'Necromancer':'', 'Rogue':''}
    return render_template('home.html')

@app.route('/alignment')
def alignments():
    affinities = {'Neutral':'0', 'Good':'', 'Bad':'', 'Extreme Good':'', 'Extreme Bad':''}
    return render_template('RandomCharacter.html')