from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.weapon import Weapon
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id":session['user_id']})
    # catch for invalid user_id somehow being in session, clear it via logout so user can login
    if not user:
        return redirect('/user/logout')
        
    return render_template('dashboard.html', user=user, weapons=Weapon.get_all())

@app.route('/weapons/new')
def create_weapon():
    if 'user_id' not in session:
        return redirect('/user/login')

    return render_template('weapon_new.html')

@app.route('/weapons/new/process', methods=['POST'])
def process_weapon():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Weapon.validate_weapon(request.form):
        return redirect('/weapons/new')

    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_3_hours': request.form['under_3_hours'],
    }
    Weapon.save(data)
    return redirect('/dashboard')

@app.route('/weapons/<int:id>')
def view_weapon(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    return render_template('weapon_view.html',weapon=Weapon.get_by_id({'id': id}))

@app.route('/weapons/edit/<int:id>')
def edit_weapon(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    return render_template('weapon_edit.html',weapon=Weapon.get_by_id({'id': id}))

@app.route('/weapons/edit/process/<int:id>', methods=['POST'])
def process_edit_weapon(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Weapon.validate_weapon(request.form):
        return redirect(f'/weapons/edit/{id}')

    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_3_hours': request.form['under_3_hours'],
    }
    Weapon.update(data)
    return redirect('/dashboard')

@app.route('/weapons/destroy/<int:id>')
def destroy_weapon(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    Weapon.destroy({'id':id})
    return redirect('/dashboard')