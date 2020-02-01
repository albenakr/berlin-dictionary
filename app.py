import os
from flask import Flask, render_template, redirect, request, url_for, make_response
from flask_pymongo import PyMongo
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
    return render_template("words.html", words=mongo.db.words.find())


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
    return redirect(url_for('get_words'))

@app.route('/manage_word/<word_id>')
def manage_word(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    return render_template('manageword.html', word=the_word)

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
    return redirect(url_for('get_words'))

@app.route('/upvote/<word_id>', methods=['POST'])
def upvote_word(word_id):
    words = mongo.db.words
    the_id= {"_id": ObjectId(word_id)}
    the_word = words.find_one(the_id)
    #the_score = the_word['score']
    the_word['score'] = the_word['score'] + 1
    #print('the_score: ' + str(the_score))
    words.replace_one(the_id, the_word)
    return redirect(url_for('get_words'))



@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('get_words'))

if __name__ == '__main__':
    app.run(host=os.getenv("IP","0.0.0.0"), 
    port=int(os.getenv("PORT","8080")), 
    debug=True)
