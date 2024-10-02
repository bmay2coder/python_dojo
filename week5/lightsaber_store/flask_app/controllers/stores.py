from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.store import Store


@app.route('/')
def index():
    return redirect('/stores')

@app.route('/stores')
def stores():
    stores = Store.get_all()
    return render_template("index_lightsaber_store.html",all_stores = stores)


@app.route('/create/store',methods=['POST'])
def create_store():
    Store.save(request.form)
    return redirect('/stores')

@app.route('/store/<int:id>')
def show_store(id):
    data = {
        "id": id
    }
    return render_template('store.html', store=Store.get_one_with_lightsabers(data))