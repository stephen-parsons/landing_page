# Stephen Parsons
# Assignment Landing Page
# 11/29/17

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')
@app.route('/dojos/new')
def dojos_new():
	return render_template('dojos.html')
@app.route('/info', methods=["POST"])
def get_info():
	print "Got Info"
	name = request.form['name']
	email = request.form['email']
	print name
	print email
	return redirect('/dojos/new')
app.run(debug=True)		