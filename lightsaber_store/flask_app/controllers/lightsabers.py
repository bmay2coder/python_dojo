from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import store, lightsaber

@app.route('/lightsabers')
def lightsabers():
    
    return render_template('lightsaber.html',stores = store.Store.get_all())


@app.route('/create/lightsaber',methods=['POST'])
def create_lightsaber():
    lightsaber.Lightsaber.save(request.form)
    return redirect('/')