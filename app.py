from flask import Flask, request, render_template, jsonify
from generator import gen_sentence
import json
import random
from sentiment import analyze_sentiment

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

images = {
    "harry": ['harry1.jpg',
              'harry2.jpeg',
              'harry3.jfif'],
    "herm": ["herm1.jpg"],
    "ron": ["ron1.jpg",
            "ron2.jpg",
            "ron3.jfif"],
    "dumb": ["dumb1.jpg"]

}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hp/')
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

    img = random.choice(images[char])

    quote = ""
    loops = 0

    while loops < 1000:
        quote = gen_sentence(data[char], count)
        sentiment_data = analyze_sentiment(quote)
        compound_score = sentiment_data[3]
        if compound_score <= -0.25 and sentiment == "neg":
            break
        elif compound_score >= 0.25 and sentiment == "pos":
            break
        elif compound_score > -.025 and compound_score < 0.25 and sentiment == "neut":
            break
        loops += 1

    return render_template('hp.html', quote=quote, img=img)


@app.route('/got/')
def got():
    return render_template('hp.html')


@app.route('/office/')
def office():
    return render_template('hp.html')


@app.route('/custom/')
def custom():
    return render_template('hp.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
