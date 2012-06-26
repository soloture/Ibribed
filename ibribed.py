# all the imports
import sqlite3
from flask import Flask, request, redirect, url_for, render_template, flash
import datetime
import shelve

DEBUG = True
SECRET_KEY = 'development key'



# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

#initializing database

entries = shelve.open('bribe.db', writeback=True)

#showing entries from the newest ones	
@app.route('/')
def show_entries():
#	if entries is not {}:
	return render_template('show_entries.html', entries=entries,)
#	else: 
#		return rendor_template('show_entries_empty.html')

#posting a entry
@app.route('/add',methods=['POST'])
def add_entry():
	datenow = str(datetime.datetime.now())
	entries[datenow]={}
	entries[datenow]['city'] = request.form['city']
	entries[datenow]['date'] = datetime.datetime.now()
	entries[datenow]['amount'] = request.form['amount']
	entries[datenow]['tags'] = request.form['tags']
	entries[datenow]['title'] = request.form['title']
	entries[datenow]['story'] = request.form['story']
	flash('New entry was succesfully posted')
	return redirect(url_for('show_entries'))


#Get the shit working
if __name__ == '__main__':
	app.run(debug=True)
	
