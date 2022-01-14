from flask import Flask, request, render_template, jsonify
from generator import gen_sentence
import json

app = Flask(__name__)

harryMarkov = json.load(open('data/harry_potter/chain/harry_chain.json'))
ronMarkov = json.load(open('data/harry_potter/chain/ron_chain.json'))
hermMarkov = json.load(open('data/harry_potter/chain/hermione_chain.json'))
dumbMarkov = json.load(open('data/harry_potter/chain/dumbledore_chain.json'))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
