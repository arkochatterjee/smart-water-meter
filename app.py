from flask import Flask, render_template, request, send_file, flash, redirect, session, abort, url_for, jsonify
import json
import requests
import pyrebase

app = Flask(__name__)


config = {
  "apiKey": "AIzaSyBtWO4MTbJn2GuJzKr1JTTe08Wwr4DAiAk",
  "authDomain": "smart-water-2279a.firebaseapp.com",
  "databaseURL": "https://smart-water-2279a.firebaseio.com",
  "storageBucket": "smart-water-2279a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/', methods=['GET'])
def index():
    flowrate = db.child("flowrate").get()
    temp = db.child("temp").get()
    pH = db.child("pH").get()
    
    return render_template('index.html', flowrate = flowrate.val(), temp = temp.val(), pH = pH.val())


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)