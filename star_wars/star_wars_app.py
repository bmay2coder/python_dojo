from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_jedi_masters():
    #return 'Hello Jedi Masters'
    return render_template('index.html', phrase="I am Master Yoda")

@app.route('/apprentice')
def hello_star_was():
    return 'Hello Jedi Apprentice'

@app.route('/students')
def student_apprentices():
    apprentices = [
       {'name' : 'Jeff', 'age' : 'unknown'},
       {'name' : 'Isaac', 'age' : 'unknown'},
       {'name' : 'Ezell', 'age' : 'unknown'},
       {'name' : 'Eduardo', 'age' : 'unknown'}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], apprentices = apprentices)

@app.route('/apprentice/<int:num>/<name>')
def apprentice_name_amount(num, name):
    return render_template("name.html", num = num, name = name.capitalize())

@app.route('/apprentice/fly/')
def apprentice_fly():
    return render_template("fly.html",num=3,color="blue")

@app.route('/apprentice/fly/<int:num>')
def apprentice_fly_amount(num):
    return render_template("fly.html",num = num,color="blue")

@app.route('/apprentice/table/game')
def apprentice_table_game():
    users = [
   {'first_name' : 'Jeff', 'last_name' : 'Marc'},
   {'first_name' : 'Ezell', 'last_name' : 'Mosley'},
   {'first_name' : 'Michael', 'last_name' : 'Casillas'},
   {'first_name' : 'Eduardo', 'last_name' : 'Cruz'},
   {'first_name' : 'Samuel', 'last_name' : 'Coulon'},
   {'first_name' : 'Isaac', 'last_name' : 'Williams'}
]
    return render_template("table_game.html", users = users)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
	



	
