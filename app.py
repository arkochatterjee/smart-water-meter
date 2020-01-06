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
  


@app.route('/first', methods=['GET'])
def first():
    flowrate1 = db.child("floor1").child("flowrate").get()
    temp1 = db.child("floor1").child("temp").get()
    pH1 = db.child("floor1").child("pH").get()

    return render_template('index1.html', flowrate = flowrate1.val(), temp = temp1.val(), pH = pH1.val())
  
@app.route('/second', methods=['GET'])
def second():
    flowrate2 = db.child("floor2").child("flowrate").get()
    temp2 = db.child("floor2").child("temp").get()
    pH2 = db.child("floor2").child("pH").get()

    return render_template('index2.html', flowrate = flowrate2.val(), temp = temp2.val(), pH = pH2.val())

@app.route('/third', methods=['GET'])
def third():
    flowrate3 = db.child("floor3").child("flowrate").get()
    temp3 = db.child("floor3").child("temp").get()
    pH3 = db.child("floor3").child("pH").get()

    return render_template('index3.html', flowrate = flowrate3.val(), temp = temp3.val(), pH = pH3.val())

@app.route('/fourth', methods=['GET'])
def fourth():
    flowrate4 = db.child("floor4").child("flowrate").get()
    temp4 = db.child("floor4").child("temp").get()
    pH4 = db.child("floor4").child("pH").get()
    return render_template('index4.html', flowrate = flowrate4.val(), temp = temp4.val(), pH = pH4.val())


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)