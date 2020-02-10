import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'berlin_dictionary'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_words')
def get_words():
    return render_template("words.html", words=list(mongo.db.words.find()))

@app.route('/high_score_words')
def high_score_words():
    return render_template("highscorewords.html", popular_words=mongo.db.words.find({'score': {'$gt': 5}}))
    
@app.route('/score_rank')
def score_rank():
    return render_template("scorerank.html", ranked_words = mongo.db.words.find().sort('score', DESCENDING))

@app.route('/alphabetical_order')
def alphabetical_order():
    return render_template("alphabeticalorder.html", alpabetical_words = mongo.db.words.find().collation({ 'locale': "en" }).sort('word'))


@app.route('/add_word')
def add_word():
    return render_template('addword.html')


@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    req = request.form.to_dict()
    examples = req['example']
    req['example'] = examples.split('/')
    score = req['score']
    req['score'] = int(score)
    if req['author'] == "":
        req['author'] = "Anonymous"
    words.insert_one(req)
    return render_template('wordadded.html')

@app.route('/manage_word/<word_id>')
def manage_word(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    return render_template('manageword.html', word=the_word, fullUrl=request.url)

@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    return render_template('editword.html', word=the_word)

@app.route('/update_word/<word_id>', methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.replace_one({"_id": ObjectId(word_id)},
    {
        'word':request.form.get('word'),
        'definition':request.form.get('definition'),
        'example':request.form.get('example').split('/'),
        'author':request.form.get('author'),
        'score': 0
    })
    return render_template('wordadded.html')

@app.route('/upvote/<word_id>', methods=['POST'])
def upvote_word(word_id):
    words = mongo.db.words
    the_id= {"_id": ObjectId(word_id)}
    the_word = words.find_one(the_id)
    the_word['score'] = the_word['score'] + 1
    words.replace_one(the_id, the_word)
    return redirect(url_for('manage_word', word_id=the_word['_id']))


@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return render_template('worddeleted.html')


@app.route('/search')
def search():
    query = request.args.get('search_query')
    return render_template('searchresult.html', db_results = list(mongo.db.words.find( { '$text': { '$search': query } } )))

@app.route('/manage_words_page')
def manage_words_page():
    return render_template("managewordspage.html")

if __name__ == '__main__':
    app.run(host=os.getenv("IP","0.0.0.0"), 
    port=int(os.getenv("PORT","8080")), 
    debug=True)
