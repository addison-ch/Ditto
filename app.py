from flask import Flask, request, render_template, jsonify
from generator import gen_sentence
import json


app = Flask(__name__)

harryMarkov = json.load(open('data/harry_potter/chain/harry_chain.json'))
ronMarkov = json.load(open('data/harry_potter/chain/ron_chain.json'))
hermMarkov = json.load(open('data/harry_potter/chain/hermione_chain.json'))
dumbMarkov = json.load(open('data/harry_potter/chain/dumbledore_chain.json'))

data = {
    "harry": harryMarkov,
    "ron": ronMarkov,
    "herm": hermMarkov,
    "dumb": dumbMarkov
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hp')
def hp():
    return render_template('hp.html')


@app.route('/hp/result', methods=['POST'])
def hp_result():
    char = request.form["char"]
    sentiment = request.form["sentiment"]
    words = request.form["words"]
    count = 50
    try:
        maxWord = int(words)
        if maxWord > 0:
            count = maxWord
    except:
        pass

    quote = gen_sentence(data[char], count)

    return render_template('hp.html', quote=quote)


@app.route('/got')
def got():
    return render_template('hp.html')


@app.route('/office')
def office():
    return render_template('hp.html')


@app.route('/custom')
def custom():
    return render_template('hp.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
