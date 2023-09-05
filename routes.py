from flask import render_template, jsonify, request, redirect, url_for, make_response
from app import app
from services import *

@app.route('/')
def index():
    entries_json = get_entries()
    return render_template('index.html', entries=entries_json)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        add_entry(time, date)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit(id):
    entry = collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        edit_entry(id, time, date)
        return redirect(url_for('index'))
    return render_template('edit.html', entry=entry)

@app.route('/delete/<string:id>', methods=['POST'])
def delete(id):
    delete_entry(id)
    return redirect(url_for('index'))
