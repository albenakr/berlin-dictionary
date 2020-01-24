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

if __name__ == '__main__':
    app.run(host=os.getenv("IP","0.0.0.0"), 
    port=int(os.getenv("PORT","8080")), 
    debug=True)