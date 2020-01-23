import os
from flask import Flask

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(host=os.getenv("IP","0.0.0.0"), 
    port=int(os.getenv("PORT","8080")), 
    debug=True)