import os
from flask import Flask, render_template, redirect, request, url_for 
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
    return render_template("words.html", words=mongo.db.words.find() )

@app.route('/add_word')
def add_word():
    return render_template('addword.html')

@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    req = request.form.to_dict()
    print(req)
    examples = req['example']
    req['example'] = examples.split('/')

    if req['author'] == "":
        req['author'] = "Anonymous"

    words.insert_one(req)
    return redirect(url_for('get_words'))

@app.route('/manage_words')
def manage_words():
    return render_template('managewords.html')

@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.tasks.find_one({"_id": ObjectId(word_id)})
    return render_template('/edit_word', word=the_word)

if __name__ == '__main__':
    app.run(host=os.getenv("IP","0.0.0.0"), 
    port=int(os.getenv("PORT","8080")), 
    debug=True)